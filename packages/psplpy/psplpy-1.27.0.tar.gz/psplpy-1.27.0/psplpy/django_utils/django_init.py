import shutil
from .templates import T
from .settings import *
from .utils import *
from psplpy.file_utils import get_file_paths


class DjangoInit:
    def __init__(self, project_dir: str | Path = None, database: str = None, env_file: Path | str = None,
                 show_info: bool = True):
        self.s = Settings(project_dir, show_info)

        get_env.env_file = self.s.project_dir.parent / '.env'
        if env_file:
            get_env.env_file = Path(env_file)
        self.database = database
        self.show_info = show_info
        self.rc_dir = Path(__file__).resolve().parent / 'resources'
        self._python = self._check_python()

    @staticmethod
    def _check_python() -> str:
        if os.system('python3 --version') == 0:
            return 'python3'
        return 'python'

    def _new_file(self, path: Path, content: str = None) -> None:
        if not path.exists():
            path.write_text(content, encoding='utf-8')
            self.s.sp._show_info(f'New: {content}')

    def _mkdir(self, dir_path: Path) -> None:
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)
            self.s.sp._show_info(f'Make dir: {dir_path}')

    def _replace_file(self, file_path: Path, old: str, new: str, not_in: str = '') -> None:
        if not file_path.exists():
            raise ValueError(f'File does not exist: {file_path}')
        content = file_path.read_text(encoding='utf-8')
        if not_in and not_in in content:
            return
        if old in content:
            file_path.write_text(content.replace(old, new), encoding='utf-8')
            self.s.sp._show_info(f'Change: {old}')
            self.s.sp._show_info(f'To: {new}')

    def asgi(self) -> 'DjangoInit':
        self.s.add_installed_apps('channels')
        self.s.sp.add_before('MIDDLEWARE', T.AsgiApplication.new.format(project_name=self.s.project_name))

        self._replace_file(self.s.project_app_dir / 'asgi.py',
                           T.Asgi.old.format(project_name=self.s.project_name),
                           T.Asgi.new.format(project_name=self.s.project_name))
        return self

    def create_db(self):
        create_db(self.database)

    def basic_init(self) -> 'DjangoInit':
        # set .env file
        s = ('from psplpy.other_utils import get_env\n'
             'get_env.env_file = Path(__file__).resolve().parent.parent.parent / ".env"')
        self.s.sp.add_before("BASE_DIR", s)
        # make global templates dir
        templates_dir = self.s.project_dir / 'templates'
        self._mkdir(templates_dir)
        self.s.sp.sub(T.Templates.name, T.Templates.new)
        shutil.copy2(self.rc_dir / 'templates' / 'base.html', templates_dir / 'base.html')
        # make global static dir
        self._mkdir(self.s.project_dir / 'static')
        self.s.sp.add_after('STATIC_URL', "STATICFILES_DIRS = [BASE_DIR / 'static',]")
        # make global media dir
        self._mkdir(self.s.project_dir / 'media')
        self.s.sp.add_before('STATIC_URL', "MEDIA_URL = '/media/'\nMEDIA_ROOT = BASE_DIR / 'media'")
        # modify allowed hosts
        self.s.sp.sub('ALLOWED_HOSTS', "ALLOWED_HOSTS = ['*']")
        # set database
        if self.database and self.database != DbBackend.SQLITE3:
            self.s.sp.sub(T.Databases.name, T.Databases.new.format(database=self.database))
        # import django.urls.include
        new = 'from django.urls import path, include'
        self._replace_file(self.s.project_app_dir / 'urls.py', 'from django.urls import path', new, not_in=new)
        return self

    def i18n(self) -> 'DjangoInit':
        self.s.add_middleware('django.middleware.locale.LocaleMiddleware')
        self.s.sp.add_after('USE_I18N', 'USE_L10N = True')
        self.s.sp.add_after('USE_TZ', "LOCALE_PATHS = [BASE_DIR / 'locale',]")
        self.s.sp.add_before('LANGUAGE_CODE', T.Languages.new)
        new = "path('i18n/', include('django.conf.urls.i18n'))"
        self._replace_file(self.s.project_app_dir / 'urls.py', ',\n]',
                           f",\n    {new},\n]", not_in=new)
        return self

    def startapp(self, name: str) -> 'DjangoInit':
        os.system(f'{self._python} manage.py startapp {name}')
        self.s.add_installed_apps(name)
        # modify project urls.py
        new = f"path('{name}/', include('{name}.urls', namespace='{name}'))"
        self._replace_file(self.s.project_app_dir / 'urls.py', ',\n]',
                           f",\n    {new},\n]", not_in=new)
        app_path = self.s.project_dir / name
        # create urls.py
        self._new_file(app_path / 'urls.py', T.AppUrls.new.format(app_name=name))
        # create commands dir
        self._mkdir(app_path / 'management' / 'commands')
        return self

    def _cp_dir(self, src_dir: Path, dst_dir: Path) -> None:
        dst_dir.mkdir(parents=True, exist_ok=True)

        rel_src_paths = get_file_paths(src_dir, relative=True, generator=True)
        for rel_src_path in rel_src_paths:
            src_path = src_dir / rel_src_path
            dst_path = dst_dir / rel_src_path
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_path, dst_path)
            self.s.sp._show_info(f'Copy file: {src_path} to {dst_path}')

    def accounts_app(self) -> 'DjangoInit':
        app_name = 'accounts'
        self.startapp(app_name)
        self.s.sp.add_after("AUTH_PASSWORD_VALIDATORS", T.Accounts.new.format(app_name=app_name))
        self._cp_dir(self.rc_dir / 'templates' / 'registration', self.s.project_dir / 'templates' / 'registration')
        self._cp_dir(self.rc_dir / 'apps' / 'accounts', self.s.project_dir / app_name)
        return self
