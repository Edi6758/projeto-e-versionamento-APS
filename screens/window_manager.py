from ttkthemes import ThemedTk
from screens.hero_creator import HeroCreatorScreen
from screens.loading import LoadingScreen


class WindowManager:
    def __init__(self):
        self.__window = ThemedTk(theme="equilux")
        self.__loading = LoadingScreen(self)
        self.__hero_creator = HeroCreatorScreen(self)
        self.__battle = None
        self.loading.load()

    @property
    def window(self):
        return self.__window

    @property
    def loading(self):
        return self.__loading

    @property
    def hero_creator(self):
        return self.__hero_creator
