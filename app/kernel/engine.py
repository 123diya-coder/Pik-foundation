from app.ethics.firewall import EthicsFirewall
from app.kernel.registry import EngineRegistry

class KernelBrain:
    def __init__(self, ethics_rules):
        self.version = "v0.1-ultra"
        self.ethics = EthicsFirewall(ethics_rules)
        self.registry = EngineRegistry()

        # default engine
        self.registry.register("default", self._basic_engine)

    async def think(self, prompt: str, identity_vector):
        ethics_ok = self.ethics.check(prompt)

        engine = self.registry.get("default")
        thought = engine(prompt)

        return {
            "thought": thought,
            "identity_influence": identity_vector,
            "ethics_passed": ethics_ok
        }

    def _basic_engine(self, prompt):
        return f"[Kernel v0.1-ultra] Thinking on: {prompt}"
