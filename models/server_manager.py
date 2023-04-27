

class ServerManager:
    def __init__(self, player_interface):
        self.__player_interface = player_interface

    def connect_to_server(self):
        message = None
        player_name = self.player_interface.window_manager.input_popup(title='Player Identification',
                                                                       message='Como você se chama?')
        try:
            message = self.player_interface.dog_server_interface.initialize(player_name, self.player_interface)
            print(message)
        except Exception as error_message:
            self.player_interface.window_manager.popup(message=error_message)
        finally:
            if message != 'Conectado a Dog Server':
                self.player_interface.window_manager.popup(message=message)

    def start_match(self):
        start_status = self.player_interface.dog_server_interface.start_match(2)
        message = start_status.get_message()
        print(message)
        if message == 'Partida iniciada':
            self.player_interface.window_manager.swap_to_hero_creator()

    @property
    def player_interface(self):
        return self.__player_interface
