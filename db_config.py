import os


DB_CONFIG = {
    "host": os.environ.get("DB_HOST", "localhost"),
    "port": int(os.environ.get("DB_PORT", "3306")),
    "user": os.environ.get("DB_USER", "inventory_user"),
    "password": os.environ.get("DB_PASSWORD", ""),
    "database": os.environ.get("DB_NAME", "inventory_portfolio"),
    "ssl_disabled": False,
}

if os.environ.get("DB_SOCKET"):
    DB_CONFIG["unix_socket"] = os.environ["DB_SOCKET"]

if os.environ.get("DB_SSL_CA"):
    DB_CONFIG.update({
        "ssl_ca": os.environ["DB_SSL_CA"],
        "ssl_verify_cert": True,
        "ssl_verify_identity": True,
    })
