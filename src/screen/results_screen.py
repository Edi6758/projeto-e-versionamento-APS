

class ResultsScreen:
    def __init__(self, window_manager):
        self.__manager = window_manager
        self.__frame = None

    def open(self, victory: bool):
        pass

    def create_victory_widgets(self):
        pass

    def create_defeat_widgets(self):
        pass

    def button(self):
        pass

    def statistics(self):
        pass

    @property
    def manager(self):
        return self.__manager

    @property
    def frame(self):
        return self.__frame

    @frame.setter
    def frame(self, frame):
        self.__frame = frame
