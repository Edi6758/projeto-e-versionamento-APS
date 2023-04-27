from screens.window_manager import WindowManager
from models.server_manager import ServerManager
from models.battle_manager import BattleManager


class PlayerInterface:
    def __init__(self):
        self.__server_manager = ServerManager(player_interface=self)
        self.__window_manager = WindowManager(player_interface=self)
        self.__battle_manager = BattleManager(player_interface=self)
        self.server_manager.connect_to_server()

    @property
    def window_manager(self):
        return self.__window_manager

    @property
    def server_manager(self):
        return self.__server_manager

    @property
    def battle_manager(self):
        return self.__battle_manager
