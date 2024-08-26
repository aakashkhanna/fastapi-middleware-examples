from collections import defaultdict
from time import time
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, HTTPException, Response

class HeaderValidatorMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Response:
        if "X-Custom-Header" not in request.headers:
            raise HTTPException(status_code=400, detail="X-Custom-Header missing")

        response = await call_next(request)
        return response