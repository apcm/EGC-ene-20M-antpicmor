ALLOWED_HOSTS = ["*"]

# Modules in use, commented modules that you won't use
MODULES = [
    'authentication',
    'base',
    'booth',
    'census',
    'mixnet',
    'postproc',
    'store',
    'visualizer',
    'voting',
]

APIS = {
    'authentication': 'BASEURL',
    'base': 'BASEURL',
    'booth': 'BASEURL',
    'census': 'BASEURL',
    'mixnet': 'BASEURL',
    'postproc': 'BASEURL',
    'store': 'BASEURL',
    'visualizer': 'BASEURL',
    'voting': 'BASEURL',
}

BASEURL = 'https://herokuestudiaregc.herokuapp.com'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': '5432',
    }
}

# number of bits for the key, all auths should use the same number of bits
KEYBITS = 256

import django_heroku
django_heroku.settings(locals())
