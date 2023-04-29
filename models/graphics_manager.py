

class GraphicsManager:
    def __init__(self, manager):
        self.__manager = manager

    def load(self):
        pass

    @property
    def manager(self):
        return self.__manager
