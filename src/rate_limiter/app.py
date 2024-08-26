from fastapi import FastAPI

from .limiter import RateLimitingMiddleware

app = FastAPI()

app.add_middleware(RateLimitingMiddleware, max_requests = 10, time_window = 60)

@app.get("/limit-sample")
def protected_route():
    return {"message": "Hello World!"}