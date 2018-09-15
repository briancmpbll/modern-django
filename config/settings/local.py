from config.settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g77#sm-u*hb7du3s&*@cwo_%@_k1)yaac+(^8q7w3n4xz^f6ti'
DEBUG = env.bool('DJANGO_DEBUG', default=True)
