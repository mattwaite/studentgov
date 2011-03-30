DEBUG = True
TEMPLATE_DEBUG = DEBUG
ADMINS = (
)
MANAGERS = ADMINS
DATABASES = {
   'default': {
       'ENGINE': 'sqlite3',
       'NAME': 'studentgov',
       'USER': '',
       'PASSWORD': '',
       'HOST': '',
       'PORT': '',
   }
}

TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
MEDIA_ROOT = ''
MEDIA_URL = ''
ADMIN_MEDIA_PREFIX = ''
SECRET_KEY = '1z23lse*74dhsw2zkxmox-2jjvj*4*ei*z3=k5%u!QZ6!*5t9('
TEMPLATE_LOADERS = (
   'django.template.loaders.filesystem.Loader',
   'django.template.loaders.app_directories.Loader',
)
TEMPLATE_CONTEXT_PROCESSORS = (
   "django.core.context_processors.auth",
   "django.core.context_processors.request",
)
MIDDLEWARE_CLASSES = (
   'django.middleware.common.CommonMiddleware',
   'django.contrib.sessions.middleware.SessionMiddleware',
   'django.middleware.csrf.CsrfViewMiddleware',
   'django.contrib.auth.middleware.AuthenticationMiddleware',
   'django.contrib.messages.middleware.MessageMiddleware',
   'django.contrib.redirects.middleware.RedirectFallbackMiddleware'
)

ROOT_URLCONF = 'studentgov.urls'
TEMPLATE_DIRS = (
   '',
)

INSTALLED_APPS = (
   'django.contrib.auth',
   'django.contrib.contenttypes',
   'django.contrib.sessions',
   'django.contrib.sites',
   'django.contrib.admin',
   'django.contrib.sitemaps',
   'django.contrib.redirects',
   'government',
   'people',
)