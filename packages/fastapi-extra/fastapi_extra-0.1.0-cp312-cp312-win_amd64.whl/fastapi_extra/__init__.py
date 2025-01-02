__version__ = "0.1.0"


def install():
    try:
        from fastapi import routing

        from fastapi_extra import routing as native_routing  # type: ignore
        
        routing.APIRouter = native_routing.BaseRouter  # type: ignore

    except ImportError:  # pragma: nocover
        pass
