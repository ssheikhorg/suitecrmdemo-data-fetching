from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

db_config = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.mysql",
            "credentials": {
                "host": "localhost",
                "port": "3306",
                "user": "root",
                "password": "root",
                "database": "mydb",
            },
        },
    },
    "apps": {
        "models": {
            "models": ["app.models.tortoise_models"],
            "default_connection": "default",
        },
    },
    "use_tz": False,
    "timezone": "UTC",
}


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url="mysql://root:root@localhost:3306/mydb",
        modules={"models": ["app.models.tortoise_models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
