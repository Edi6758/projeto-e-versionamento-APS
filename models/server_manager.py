

class ServerManager:
    def __init__(self, player_interface):
        self.__player_interface = player_interface

    def connect_to_server(self):
        message = None
        player_name = self.player_interface.window_manager.input_popup(title='Player Identification',
                                                                       message='Como você se chama?')
        disconnected = True
        while disconnected:
            message = self.player_interface.dog_server_interface.initialize(player_name, self.player_interface)
            print(message)
            if message != 'Conectado a Dog Server':
                break
        self.player_interface.window_manager.popup(message=message)

    def start_match(self):
        opponent_unavailable = True
        while opponent_unavailable:
            start_status = self.player_interface.dog_server_interface.start_match(2)
            message = start_status.get_message()
            print(message)
            if message == 'Partida iniciada':
                break
            print('tentando novamente')
        self.player_interface.window_manager.swap_to_hero_creator()

    @property
    def player_interface(self):
        return self.__player_interface
