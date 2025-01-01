# -*- coding: utf-8 -*-

import os

import uvicorn

from core_apis.api.entry import create_application


def run():
    application = create_application(
        name=os.environ.get("API_NAME", "API-Service"),
        debug=True if os.environ.get("DEBUG", False) == "1" else False,
        add_cors_middleware=True)

    uvicorn.run(
        application,
        host=os.environ.get("HOST", "0.0.0.0"),
        port=int(os.environ.get("PORT", 3500)),
        log_level=os.getenv("LOG_LEVEL", "info")
    )
