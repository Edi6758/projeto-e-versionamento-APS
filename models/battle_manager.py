from models.hero_manager import HeroManager


class BattleManager:
    def __init__(self, player_interface):
        self.__player_interface = player_interface
        self.__hero_manager = HeroManager(manager=self)
        self.__team = {}
        self.__enemy_team = {}

    def prepare_battle(self):
        self.player_interface.window_manager.swap_to_battle()

    def establish_team(self):
        builds = []
        for i in range(3):
            race = self.player_interface.window_manager.hero_creator.race_vars[i].get()
            classe = self.player_interface.window_manager.hero_creator.class_vars[i].get()
            element = self.player_interface.window_manager.hero_creator.element_vars[i].get()
            build = (race, classe, element)
            builds.append(build)
        heroes = self.hero_manager.create_heroes(builds)
        self.player_interface.window_manager.hero_creator.display_team(heroes)
        heroes = {f'{hero_index}': hero for hero, hero_index in enumerate(heroes)}
        self.team = heroes
        self.player_interface.server_manager.send_team(builds)

    @property
    def player_interface(self):
        return self.__player_interface

    @property
    def hero_manager(self):
        return self.__hero_manager

    @property
    def team(self):
        return self.__team

    @property
    def enemy_team(self):
        return self.__enemy_team

    @team.setter
    def team(self, team):
        self.__team = team

    @enemy_team.setter
    def enemy_team(self, enemy_team):
        self.__enemy_team = enemy_team
