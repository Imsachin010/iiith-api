from fastapi import FastAPI
from app.routes import operations

app = FastAPI()

# Register arithmetic routes
app.include_router(operations.router, tags=["Operations"])
