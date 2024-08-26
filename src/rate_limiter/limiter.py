from collections import defaultdict
from time import time
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, HTTPException, Response

class RateLimitingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, max_requests: int, time_window: int):
        super().__init__(app)
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = defaultdict(list)

    async def dispatch(self, request: Request, call_next) -> Response:
        client_ip = request.client.host
        current_time = time()
        
        # Get the list of request times for the client IP
        request_times = self.requests[client_ip]
        
        # Remove outdated requests outside the time window
        request_times = [timestamp for timestamp in request_times if timestamp > current_time - self.time_window]
        self.requests[client_ip] = request_times
        
        # Check if the client exceeds the max request limit
        if len(request_times) >= self.max_requests:
            return Response(status_code=429)
        
        # Add the current request time to the list
        request_times.append(current_time)
        
        # Proceed with the request
        response = await call_next(request)
        return response