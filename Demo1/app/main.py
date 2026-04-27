# from fastapi import FastAPI

# app = FastAPI(title="Demo1")

# @app.get("/health")
# def health():
#     return {"status": "ok"}

# Day1.3
# from fastapi import FastAPI
# from core.config import get_settings

# settings = get_settings()
# app = FastAPI(title=settings.app_name, debug=settings.debug)


# @app.get("/health")
# def health():
#     return {"status": "ok", "env": settings.app_env}

# Day1.4
from fastapi import FastAPI
from core.config import get_settings
from api.router import api_router

settings = get_settings()
app = FastAPI(title=settings.name, debug=settings.debug)

app.include_router(api_router, prefix=settings.api_prefix)


@app.get("/health")
def health():
    return {"status": "ok", "env": settings.env}
