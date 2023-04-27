from screens.window_manager import WindowManager
from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor
from models.server_manager import ServerManager
from models.battle_manager import BattleManager


class PlayerInterface(DogPlayerInterface):
    def __init__(self):
        super().__init__()
        self.__dog_server_interface = DogActor()
        self.__server_manager = ServerManager(player_interface=self)
        self.__window_manager = WindowManager(player_interface=self)
        self.__battle_manager = BattleManager(player_interface=self)
        self.server_manager.connect_to_server()

    def receive_start(self, start_status):
        message = start_status.get_message()
        print(message)
        if message == 'Partida iniciada':
            self.window_manager.swap_to_hero_creator()

    @property
    def window_manager(self):
        return self.__window_manager

    @property
    def dog_server_interface(self):
        return self.__dog_server_interface

    @property
    def server_manager(self):
        return self.__server_manager

    @property
    def battle_manager(self):
        return self.__battle_manager
