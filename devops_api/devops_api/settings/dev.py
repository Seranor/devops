import os
import sys
import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# 增加apps的路径识别
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))

SECRET_KEY = 'django-insecure-h@$4s!nyo5$14d#o1nj=4f$e(1=)dttq)7z(tx5cbc&m%o=u3p'

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'corsheaders',
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_beat',
    'rest_framework',
    'channels',
    'home',
    'host',
    'users',
    'mtask',
    'conf_center',
    'release',
    'schedule',
    'monitor',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'devops_api.middlewares.logs.LogMiddleWare',
]

ROOT_URLCONF = 'devops_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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
]

WSGI_APPLICATION = 'devops_api.wsgi.application'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": "127.0.0.1",
        "PORT": 3306,
        "USER": "root",
        "PASSWORD": "asd123...",
        "NAME": "devops",
    }
}
# 配置channel的通道层
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

# 在host应用下面创建一个routing.py文件
ASGI_APPLICATION = 'devops_api.routing.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = False

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')  # static文件夹的路径
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    # 自定义异常处理
    'EXCEPTION_HANDLER': 'devops_api.utils.exceptions.custom_exception_handler',
    # 自定义认证
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # jwt认证
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        # session认证
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
    ),
}

JWT_AUTH = {
    # jwt的有效时间
    'JWT_EXPIRATION_DELTA': datetime.timedelta(weeks=1),
    'JWT_ALLOW_REFRESH': True,
}

DEFAULT_KEY_NAME = "global"

# 跨域问题处理
# 允许简单请求，所有地址 相当于CORS_ORIGIN_ALLOW_ALL="*"
CORS_ALLOW_ALL_ORIGINS = True
# 运行的请求
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

# 允许的请求头
CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',  # jwt
    'content-type',  # json
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
)

AUTH_USER_MODEL = 'users.User'

# gitlab配置信息
GITLAB = {
    "url": "http://192.168.150.22:8076/",
    "token": "aajUzz7t1AbNZBQsc5Ny",
}

# jenkins配置信息
JENKINS = {
    "server_url": 'http://192.168.150.21:8080/',
    "username": 'admin',
    "password": '119f34391f13b9de5ab6a6976cbfa42881',
}
# 发送邮件配置
EMAIL_HOST_USER = "13928835901@163.com"
EMAIL_HOST_PASSWORD = "XOLWYFIMEREAWCOU"
EMAIL_HOST = "smtp.163.com"
EMAIL_PORT = 465
EMAIL_USE_SSL = True

# 监控脚本的路径
MONITOR_SCRIPT = BASE_DIR.parent / "scripts/monitor.py"
REMOTE_MONITOR_SCRIPT_PATH = "~/monitor.py"

# 日志配置
LOGGING = {
    # 使用的python内置的logging模块，那么python可能会对它进行升级，所以需要写一个版本号，目前就是1版本
    'version': 1,
    # 是否去掉目前项目中其他地方中以及使用的日志功能，但是将来我们可能会引入第三方的模块，里面可能内置了日志功能，所以尽量不要关闭，肯定False
    'disable_existing_loggers': False,
    # 日志的处理格式
    'formatters': {
        # 详细格式，往往用于记录日志到文件/其他第三方存储设备
        'verbose': {
            # levelname等级，asctime记录时间，module表示日志发生的文件名称，lineno行号，message错误信息
            'format': '{levelname} {asctime} {module}:{lineno:d} {message}',
            # 日志格式中的，变量分隔符
            'style': '{',
        },
        'simple': {  # 简单格式，往往用于终端
            'format': '{levelname} {module}:{lineno} {message}',
            'style': '{',
        },
    },
    'filters': {  # 日志的过滤设置，可以对日志进行输出时的过滤用的
        # 在debug=True下产生的一些日志信息，要不要记录日志，需要的话就在handlers中加上这个过滤器，不需要就不加
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {  # 日志的处理方式
        'console': {  # 终端下显示
            'level': 'DEBUG',  # 日志的最低等级
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',  # 处理日志的核心类
            'formatter': 'simple'
        },
        'file': {  # 文件中记录日志
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            # 日志位置,日志文件名,日志保存目录必须手动创建
            'filename': BASE_DIR.parent / "logs/devops.log",
            # 单个日志文件的最大值,这里我们设置300M
            'maxBytes': 300 * 1024 * 1024,
            # 备份日志文件的数量,设置最大日志数量为10
            'backupCount': 10,
            # 日志格式:详细格式
            'formatter': 'verbose',
            # 设置默认编码，否则打印出来汉字乱码
            'encoding': 'utf-8',
        },
    },
    # 日志实例对象
    'loggers': {
        'django': {  # 固定名称，将来django内部也会有异常的处理，只会调用django下标的日志对象
            'handlers': ['console', 'file'],
            'propagate': True,  # 是否让日志信息继续冒泡给其他的日志处理系统
        },
        "DRF": {
            'handlers': ['file'],
            'propagate': True,  # 是否让日志信息继续冒泡给其他的日志处理系统
        }
    }
}
