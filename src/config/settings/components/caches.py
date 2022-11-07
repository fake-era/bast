from decouple import config

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{config("BROKER_HOST")}:{config("BROKER_PORT", cast=int)}/',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient'
            # 'PASSWORD': config("BROKER_PASSWORD")
        },
    },
}
