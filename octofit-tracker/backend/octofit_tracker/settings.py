# Django settings for octofit_tracker project

INSTALLED_APPS = [
    # ...existing apps...
    'corsheaders',
    'rest_framework',
    'djongo',
    'octofit_tracker',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # ...existing middleware...
]

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
    }
}

CORS_ALLOW_ALL_ORIGINS = True
ALLOWED_HOSTS = ['*']
