from manage.graphics_manager import GraphicsManager
from screen.menu_screen import MenuScreen
from screen.teambuilder_screen import TeamBuilderScreen
from screen.battle_screen import BattleScreen
from screen.results_screen import ResultsScreen

from tkinter import messagebox, simpledialog, Tk


class WindowManager:
    def __init__(self, player_interface):
        self.__main = player_interface
        self.__root = Tk()
        self.root.geometry('0x0')
        self.root.overrideredirect(True)
        self.__graphics = GraphicsManager(manager=self)
        self.__menu = MenuScreen(window_manager=self)
        self.__battle = BattleScreen(window_manager=self)
        self.__teambuilder = TeamBuilderScreen(window_manager=self)
        self.__results = ResultsScreen(window_manager=self)

    def popup_message(self, message: str, title: str):
        pass

    def input_popup(self, title: str, message: str):
        return simpledialog.askstring(title, message)

    def clear_screen(self):
        for frame in self.root.winfo_children():
            frame.destroy()

    def swap_to_menu(self):
        self.clear_screen()
        self.menu.open()

    def swap_to_teambuilder(self):
        self.clear_screen()
        self.teambuilder.open()

    def swap_to_battle(self):
        self.clear_screen()
        self.battle.open()

    def swap_to_results(self, victory: bool):
        self.clear_screen()
        self.results.open(victory)

    @property
    def main(self):
        return self.__main

    @property
    def root(self):
        return self.__root

    @property
    def graphics(self):
        return self.__graphics

    @property
    def menu(self):
        return self.__menu

    @property
    def battle(self):
        return self.__battle

    @property
    def teambuilder(self):
        return self.__teambuilder

    @property
    def results(self):
        return self.__results
