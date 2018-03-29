"""
Django settings for keycloakexample project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(2x0uy0ztn04n#dr9x^x!km^cg#cdbk$k1bseqn!xmm^s$07^d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'demo',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'djangooidc.backends.OpenIdConnectBackend',
)

LOGIN_URL='openid'

# Information used when registering the client, this may be the same for all OPs
# Ignored if auto registration is not used.
OIDC_DYNAMIC_CLIENT_REGISTRATION_DATA = {
    "application_type": "web",
    "contacts": ["ops@example.com"],
    "redirect_uris": ["http://localhost:8000/openid/callback/login/", ],
    "post_logout_redirect_uris": ["http://localhost:8000/openid/callback/logout/", ]
}

# Default is using the 'code' workflow, which requires direct connectivity from your website to the OP.
OIDC_DEFAULT_BEHAVIOUR = {
    "response_type": "code",
    "scope": ["openid", "profile", "email", "address", "phone"],
}
OIDC_PROVIDERS = {
    # Test OP - webfinger supported on non-standard URL, no client self registration.
    "keycloak": {
        "srv_discovery_url": "http://localhost:8080/auth/realms/sample",
        "behaviour": OIDC_DEFAULT_BEHAVIOUR,
        "client_registration": {
            'client_id': "webapp",
            "client_secret": "47728e99-7893-4864-b4c6-1a3b79b2a780",
            "redirect_uris": ["http://localhost:8000/openid/callback/login/"],
            "post_logout_redirect_uris": ["http://localhost:8000/openid/callback/logout/"],
            "token_endpoint_auth_method": "client_secret_post"

        }
    },
}

ROOT_URLCONF = 'keycloakexample.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'keycloakexample.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
