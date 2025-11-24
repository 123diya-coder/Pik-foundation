from fastapi import APIRouter
from app.kernel.identity import IdentityGenome

router = APIRouter()
identity = IdentityGenome()

@router.get("/identity/get")
def get_identity():
    return identity.get()
