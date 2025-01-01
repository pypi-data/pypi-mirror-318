class _Databases:
    name = 'DATABASES'
    new = """DATABASES = {{
    'default': {{
        'ENGINE': '{database}',
        'NAME': get_env("DB_NAME"),
        'USER': get_env("DB_USER"),
        'PASSWORD': get_env("DB_PASSWORD"),
        'HOST': get_env("DB_HOST"),
        'PORT': get_env("DB_PORT"),
    }}
}}"""


class _AsgiApplication:
    new = """ASGI_APPLICATION = '{project_name}.asgi.application'

CHANNEL_LAYERS = {{
    'default': {{
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {{
            "hosts": [(get_env('REDIS_HOST'), get_env('REDIS_PORT'))],
        }},
    }},
}}"""


class _Asgi:
    old = """\nfrom django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{project_name}.settings')

application = get_asgi_application()"""

    new = """from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
# from some_app import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{project_name}.settings')

application = ProtocolTypeRouter({{
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
}})"""


class _AppUrls:
    new = """from django.urls import path
from .views import *

app_name = '{app_name}'

urlpatterns = [
    # path('example/', example, name='example'),
]
"""


class _Templates:
    name = 'TEMPLATES'
    new = """TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]"""


class _Languages:
    new = """LANGUAGES = [
    ('en', 'English'),
    ('zh-hans', '中文（简体）'),
]"""


class _Accounts:
    new = """LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/{app_name}/login/'

AUTH_USER_MODEL = '{app_name}.CustomUser'"""


class T:
    Databases = _Databases
    AsgiApplication = _AsgiApplication
    Asgi = _Asgi
    AppUrls = _AppUrls
    Templates = _Templates
    Languages = _Languages
    Accounts = _Accounts
