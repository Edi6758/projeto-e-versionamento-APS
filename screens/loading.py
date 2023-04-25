


class LoadingScreen:
    def __init__(self, manager):
        self.__manager = manager

    def load(self):
        self.manager.window.title("Loading")
        self.manager.window.geometry("800x600")
        self.manager.hero_creator.open()

    @property
    def manager(self):
        return self.__manager
