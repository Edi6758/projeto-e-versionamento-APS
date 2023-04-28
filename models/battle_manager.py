


class BattleManager():
    def __init__(self, player_interface):
        self.__player_interface = player_interface
        self.__team = {}
        self.__enemy_team = {}

    @property
    def manager(self):
        return self.__player_interface

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
