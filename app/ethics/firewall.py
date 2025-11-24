class EthicsFirewall:
    def __init__(self, rules):
        self.rules = rules

    def check(self, prompt: str) -> bool:
        for rule in self.rules:
            if not rule(prompt):
                return False
        return True
