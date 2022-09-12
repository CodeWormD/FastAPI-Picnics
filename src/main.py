from fastapi import FastAPI, HTTPException


def create_app():
    app_ = FastAPI(
        docs_url='/',
        debug=True
    )
    _include_routers(app_)

    return app_


def _include_routers(app_: FastAPI):
    """Include one router which include all need routers"""

    from routers.router import router

    app_.include_router(router)


app = create_app()

