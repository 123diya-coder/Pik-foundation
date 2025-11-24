class EngineRegistry:
    def __init__(self):
        self.modules = {}

    def register(self, name, engine):
        self.modules[name] = engine

    def get(self, name):
        return self.modules.get(name)
