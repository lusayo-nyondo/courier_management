from .base import *

MIDDLEWARE.extend([
    'config.middleware.NoCacheMiddleware',
])
