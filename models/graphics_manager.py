from json import load


class GraphicsManager:
    def __init__(self, manager):
        self.__manager = manager
        self.__heroes_data_assets = {}

    def load(self):
        self.load_heroes_data_assets()

    def load_heroes_data_assets(self):
        self.heroes_data_assets = {'titles': load(open('assets/titles.json', 'r')),
                                   'names': load(open('assets/names.json', 'r')),
                                   'stats': load(open('assets/stats.json', 'r'))}

    @property
    def manager(self):
        return self.__manager

    @property
    def heroes_data_assets(self):
        return self.__heroes_data_assets

    @heroes_data_assets.setter
    def heroes_data_assets(self, heroes_data_assets):
        self.__heroes_data_assets = heroes_data_assets
