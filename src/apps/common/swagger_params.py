from drf_yasg import openapi

token_params = openapi.Parameter(
    name="token",
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_STRING,
    description="Token"
)

limit_params = openapi.Parameter(
    'limit',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_INTEGER,
    description="Pagination Limit parameter",
)

offset_params = openapi.Parameter(
    'offset',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_INTEGER,
    description="Pagination Offset parameter",
)