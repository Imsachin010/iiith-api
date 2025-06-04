from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from app.database import SessionLocal
from app.models.log import LogEntry
import json
from datetime import datetime

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Capture request body
        body = await request.body()
        try:
            request_data = body.decode()
        except:
            request_data = str(body)

        # Get user from token if available
        username = "anonymous"
        if "authorization" in request.headers:
            token = request.headers["authorization"].split(" ")[1]
            from app.auth import get_current_user, SECRET_KEY, ALGORITHM
            from jose import jwt
            try:
                payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
                username = payload.get("sub", "unknown")
            except:
                pass

        # Get response
        response: Response = await call_next(request)

        # Log the info
        db = SessionLocal()
        log = LogEntry(
            username=username,
            path=request.url.path,
            method=request.method,
            request_body=request_data,
            response_status=response.status_code,
            timestamp=datetime.utcnow()
        )
        db.add(log)
        db.commit()
        db.close()

        return response
