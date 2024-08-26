# FastAPI Middleware Examples

This repository provides a collection of custom middleware examples for FastAPI. Middleware in FastAPI allows you to process requests and responses before they reach your endpoints or before they are sent back to clients. The examples provided here demonstrate how to implement common middleware functionalities such as authentication, logging, CORS, Gzip compression, and request validation. This repository contains examples of custom middleware for FastAPI, including a Header Validator, Rate Limiting, and Timing middleware. These middlewares demonstrate how to add functionality to your FastAPI application to enforce custom request headers, limit the rate of incoming requests, and measure the time taken to process requests.

## Table of Contents

- [Installation](#installation)
- [Middlewares](#middlewares)
  - [Header Validator Middleware](#header-validator-middleware)
  - [Rate Limiting Middleware](#rate-limiting-middleware)
  - [Timing Middleware](#timing-middleware)
- [Usage](#usage)
- [Contributing](#contributing)
## Installation

To use these middleware examples in your FastAPI project, clone this repository and install FastAPI and Starlette:

```bash
git clone https://github.com/your-username/fastapi-middleware-examples.git
cd fastapi-middleware-examples
poetry install
```

## Example Middlewares

### Header Validator Middleware

The `HeaderValidatorMiddleware` ensures that all incoming requests contain a specific header (`X-Custom-Header`). If the header is missing, the middleware returns a `400 Bad Request` response.

### Rate Limiting Middleware

The `RateLimitingMiddleware` limits the number of requests a client can make within a specified time window. If a client exceeds the allowed number of requests, the middleware returns a `429 Too Many Requests` response. The middleware tracks requests by client IP address.

### Timing Middleware

The `TimingMiddleware` measures the time taken to process each request. It prints the time taken for each request in the console and optionally adds this time to a response header specified by the `header_name` parameter.

## Usage

To use any of these middlewares in your FastAPI application:

1. Import the middleware class from the module where it is defined.
2. Add the middleware to your FastAPI application using the `add_middleware` method or by attaching it to a specific router.

### Example Usage

```python
from fastapi import FastAPI
from middlewares import HeaderValidatorMiddleware, RateLimitingMiddleware, TimingMiddleware

app = FastAPI()

# Add Header Validator Middleware
app.add_middleware(HeaderValidatorMiddleware)

# Add Rate Limiting Middleware
app.add_middleware(RateLimitingMiddleware, max_requests=10, time_window=60)

# Add Timing Middleware
app.add_middleware(TimingMiddleware, header_name="X-Processing-Time")

@app.get("/")
async def read_root():
    return {"message": "Hello World"}
```

## Contributing

Contributions are welcome! If you have additional middleware examples, improvements, or bug fixes, please submit a pull request.

