SWAGGER_SETTINGS = {
    "USE_SESSION_AUTH": True,
    "LOGIN_URL": "/v1/auth/login",
    "LOGOUT_URL": "/v1/auth/logout",
    "SECURITY_DEFINITIONS": {
        "API_KEY": {"type": "apiKey", "name": "Authorization", "in": "header"}
    },
    "DEEP_LINKING": True,
}
