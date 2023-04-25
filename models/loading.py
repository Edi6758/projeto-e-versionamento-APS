from json import load


class Loading:
    def __init__(self, manager):
        self.__manager = manager
        self.__heroes_data_assets = {}

    def load(self):
        self.conect_to_server()
        self.load_heroes_data_assets()

    def load_heroes_data_assets(self):
        self.heroes_data_assets = {'titles': load(open('assets/titles.json', 'r')),
                                   'names': load(open('assets/names.json', 'r')),
                                   'stats': load(open('assets/stats.json', 'r'))}

    def conect_to_server(self):
        message = None
        player_name = self.manager.input_popup(title='Player Identification', message='Como você se chama?')
        try:
            message = self.manager.player_interface.dog_server_interface.initialize(player_name,
                                                                                    self.manager.player_interface)
        except Exception as error_message:
            self.manager.popup(message=error_message)
        if message is not None:
            if message != 'Conectado a Dog Server':
                self.manager.popup(message=message)

    @property
    def manager(self):
        return self.__manager

    @property
    def heroes_data_assets(self):
        return self.__heroes_data_assets

    @heroes_data_assets.setter
    def heroes_data_assets(self, heroes_data_assets):
        self.__heroes_data_assets = heroes_data_assets
