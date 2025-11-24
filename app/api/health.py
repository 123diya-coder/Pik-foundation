from fastapi import APIRouter

health_router = APIRouter()

@health_router.get("/health")
async def health():
    return {"status": "ok", "service": "PIK", "version": "0.1.0"}
