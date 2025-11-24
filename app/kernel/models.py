from pydantic import BaseModel

class ThinkRequest(BaseModel):
    prompt: str

class ThoughtResponse(BaseModel):
    thought: str
    identity_influence: dict
    ethics_passed: bool
