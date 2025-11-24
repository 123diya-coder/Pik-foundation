from fastapi import APIRouter
from app.kernel.engine import KernelBrain
from app.kernel.identity import IdentityGenome
from app.ethics.rules import GLOBAL_ETHICS
from app.kernel.models import ThinkRequest

router = APIRouter()
brain = KernelBrain(GLOBAL_ETHICS)
identity = IdentityGenome()

@router.post("/kernel/think")
async def think_route(payload: ThinkRequest):
    return await brain.think(payload.prompt, identity.get())
