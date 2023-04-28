from ttkthemes import ThemedTk
from tkinter import messagebox, simpledialog
from screens.hero_creator import HeroCreatorScreen
from screens.battle_screen import BattleScreen
from screens.main_menu import MainMenuScreen
from models.graphics_manager import GraphicsManager


class WindowManager:
    def __init__(self, player_interface):
        self.__player_interface = player_interface
        self.__window = ThemedTk(theme="equilux")
        self.window.geometry('0x0')
        self.window.overrideredirect(True)
        self.__graphics_manager = GraphicsManager(manager=self)
        self.__main_menu = MainMenuScreen(manager=self)
        self.graphics_manager.load()
        self.__hero_creator = HeroCreatorScreen(self, hero_data_assets=self.graphics_manager.heroes_data_assets)
        self.__battle = BattleScreen(manager=self)

    def popup(self, message: str):
        messagebox.showinfo(message=message)

    def input_popup(self, title: str, message: str):
        return simpledialog.askstring(title=title, prompt=message)

    def swap_to_hero_creator(self):
        for frame in self.window.winfo_children():
            frame.destroy()
        self.hero_creator.open()

    def swap_to_battle(self):
        for frame in self.window.winfo_children():
            frame.destroy()
        self.battle.open()

    def swap_to_main_menu(self):
        for frame in self.window.winfo_children():
            frame.destroy()
        self.main_menu.open()

    @property
    def player_interface(self):
        return self.__player_interface

    @property
    def battle(self):
        return self.__battle

    @property
    def window(self):
        return self.__window

    @property
    def graphics_manager(self):
        return self.__graphics_manager

    @property
    def hero_creator(self):
        return self.__hero_creator

    @property
    def main_menu(self):
        return self.__main_menu
