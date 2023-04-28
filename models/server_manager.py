from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor


class ServerManager(DogPlayerInterface):
    def __init__(self, player_interface):
        super().__init__()
        self.__dog_server_interface = DogActor()
        self.__player_interface = player_interface
        self.__player_name = ''

    def connect_to_server(self):
        self.player_name = self.player_interface.window_manager.input_popup(title='Player Identification',
                                                                            message='Como você se chama?')
        print(self.trying_connection())

    def trying_connection(self):
        message = self.dog_server_interface.initialize(self.player_name, self)
        if message != 'Conectado a Dog Server':
            print('tentando novamente em 3 segundos')
            self.player_interface.window_manager.window.after(3000, self.trying_connection())
        else:
            return message

    def start_match(self):
        start_status = self.dog_server_interface.start_match(2)
        message = start_status.get_message()
        print(message)
        code = start_status.get_code()
        print(code)
        if code == '2':
            self.player_interface.window_manager.swap_to_hero_creator()
        elif code == '1':
            print('tentando novamente em 3 segundos')
            self.player_interface.window_manager.window.after(3000, self.start_match)

    def receive_start(self, start_status):
        message = start_status.get_message()
        print(message)
        if start_status.get_code == '2':
            self.player_interface.window_manager.swap_to_hero_creator()

    @property
    def player_interface(self):
        return self.__player_interface

    @property
    def dog_server_interface(self):
        return self.__dog_server_interface

    @property
    def player_name(self):
        return self.__player_interface

    @player_name.setter
    def player_name(self, player_name):
        self.__player_name = player_name
