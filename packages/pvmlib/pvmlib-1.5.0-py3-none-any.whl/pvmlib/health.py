from fastapi import APIRouter, HTTPException
from .database import database_manager
import os

health_router = APIRouter()

@health_router.get("/healthcheck/liveness")
async def liveness():
    return {"status": "UP"}

@health_router.get("/healthcheck/readness")
async def readiness():
     return {"status": "UP"}