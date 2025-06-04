from fastapi import FastAPI
from app.routes import operations, users
from app.database import init_db
from app.middleware import LoggingMiddleware
from app.routes import logs
from fastapi.responses import RedirectResponse

app = FastAPI(
    title="IIITH API",
    description="A FastAPI-based REST API with authentication and database integration",
    version="1.0.0"
)

# Initialize DB
init_db()

# Add logging middleware
app.add_middleware(LoggingMiddleware)

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Welcome to IIITH API",
        "documentation": "Visit /docs for API documentation",
        "endpoints": {
            "operations": ["/add", "/multiply", "/check-even-odd"],
            "authentication": ["/token"],
            "admin": ["/logs"]
        }
    }

# Routes
app.include_router(users.router, tags=["Authentication"])
app.include_router(operations.router, tags=["Operations"])
app.include_router(logs.router, tags=["Admin"])
