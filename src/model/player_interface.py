from manage.window_manager import WindowManager
from manage.battle_manager import BattleManager
from manage.server_manager import ServerManager
from manage.heroes_manager import HeroesManager


class PlayerInterface:
    def __init__(self):
        self.__server = ServerManager(player_interface=self)
        self.__heroes_manager = HeroesManager(player_interface=self)
        self.__window = WindowManager(player_interface=self)
        self.__battle = None

    def initialize(self):
        self.server.connect_to_server()

    def build_team(self):
        self.window.teambuilder.confirm_button['state'] = 'disabled'
        builds = {}
        for slot in range(3):
            race = self.window.teambuilder.race_vars[slot].get()
            classe = self.window.teambuilder.class_vars[slot].get()
            element = self.window.teambuilder.element_vars[slot].get()
            build = {'race': race, 'classe': classe, 'element': element}
            builds[slot] = build
        heroes = self.heroes_manager.create_heroes(builds, enemy_team=False)
        self.window.teambuilder.display_team(heroes)
        self.server.send_team(builds)
        response = self.try_to_prepare_battle()
        if response:
            self.prepare_battle()

    def prepare_battle(self):
        self.battle = BattleManager(player_interface=self)
        self.battle.create_turn_order(self.heroes_manager.team, self.heroes_manager.enemy_team)
        self.window.swap_to_battle()
        self.battle.prepare_next_turn()

    def try_to_prepare_battle(self):
        if self.heroes_manager.team and self.heroes_manager.enemy_team:
            return True
        return False

    @property
    def server(self):
        return self.__server

    @property
    def window(self):
        return self.__window

    @property
    def heroes_manager(self):
        return self.__heroes_manager

    @property
    def battle(self):
        return self.__battle

    @battle.setter
    def battle(self, battle: BattleManager):
        self.__battle = battle
