from fastapi import FastAPI
from .rate_limiter.app import app as limit_app
from .timer.app import app as timer_app
from .header_validation.app import app as header_validator_app

app = FastAPI()

app.mount("/limit", limit_app)
app.mount("/timer", timer_app)
app.mount("/validator", header_validator_app)