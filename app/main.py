from fastapi import FastAPI
from app.api.kernel_routes import router as kernel_router
from app.api.identity_routes import router as identity_router

app = FastAPI(
    title="PIK Ultra Kernel",
    version="0.1-ultra",
)

app.include_router(kernel_router)
app.include_router(identity_router)

@app.get("/health")
def health():
    return {"status": "alive", "kernel": "0.1-ultra"}
