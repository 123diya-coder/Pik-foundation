class IdentityGenome:
    def __init__(self):
        self.vector = {
            "kindness": 0.71,
            "logic": 0.88,
            "creativity": 0.95,
            "alignment": 1.0,
            "stability": 0.92,
            "risk_factor": 0.12,
        }

    def get(self):
        return self.vector

    def evolve(self, feedback: dict):
        for k, v in feedback.items():
            if k in self.vector:
                self.vector[k] = (self.vector[k] + v) / 2
