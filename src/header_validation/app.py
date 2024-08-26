from fastapi import FastAPI

from .validator import HeaderValidatorMiddleware

app = FastAPI()

app.add_middleware(HeaderValidatorMiddleware)

@app.get("/identifier")
def protected_route():
    return {"message": "Hello World!"}