

class GraphicsManager:
    def __init__(self, manager):
        self.__manager = manager
        self.__assets = None

    def load(self):
        pass

    def generete_hero(self, build: tuple):
        pass

    @property
    def manager(self):
        return self.__manager

    @property
    def assets(self):
        return self.__assets

    @assets.setter
    def assets(self, assets):
        self.__assets = assets
