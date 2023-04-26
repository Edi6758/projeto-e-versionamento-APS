

class ServerManager:
    def __init__(self, manager):
        self.__manager = manager

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
