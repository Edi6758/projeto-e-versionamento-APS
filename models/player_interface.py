from screens.window_manager import WindowManager
from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor
from models.server_manager import ServerManager


class PlayerInterface(DogPlayerInterface):
    def __init__(self):
        super().__init__()
        self.__dog_server_interface = DogActor()
        self.__server_manager = ServerManager(self)
        self.__window_manager = WindowManager(player_interface=self)
        self.server_manager.conect_to_server()
        self.window_manager.window.mainloop()

    def start_match(self):
        start_status = self.dog_server_interface.start_match(2)
        message = start_status.get_message()
        self.window_manager.popup(message)

    @property
    def window_manager(self):
        return self.__window_manager

    @property
    def dog_server_interface(self):
        return self.__dog_server_interface

    @property
    def server_manager(self):
        return self.__server_manager
