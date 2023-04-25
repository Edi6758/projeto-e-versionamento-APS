from screens.window_manager import WindowManager
from dog.dog_interface import DogPlayerInterface


class PlayerInterface(DogPlayerInterface):
    def __init__(self):
        super().__init__()
        self.__window_manager = WindowManager()

    @property
    def window_manager(self):
        return self.__window_manager
