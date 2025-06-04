from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class LogEntry(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    path = Column(String)
    method = Column(String)
    request_body = Column(Text)
    response_status = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
