from fastapi import FastAPI

from .timer import TimingMiddleware

app = FastAPI()

app.add_middleware(TimingMiddleware, header_name = "x-Timer")

@app.get("/timer")
def protected_route():
    return {"message": "Hello World!"}