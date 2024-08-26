from collections import defaultdict
from time import time
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, HTTPException, Response

class TimingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, header_name: str):
        super().__init__(app)
        self.header_name = header_name

    async def dispatch(self, request: Request, call_next) -> Response:
        client_ip = request.client.host
        pre_request_time = time()
        response = await call_next(request)
        post_request_time = time()
        time_taken = post_request_time-pre_request_time
        print(f"Request from {client_ip} took {time_taken} seconds.")
        
        # Proceed with the request
        response = await call_next(request)
        response.headers.append(self.header_name, f"{time_taken}")
        return response