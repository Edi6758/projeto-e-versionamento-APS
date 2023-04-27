


class BattleManager():
    def __init__(self, player_interface):
        self.__player_interface = player_interface
        self.__team = {}

    @property
    def team(self):
        return self.__team

    @team.setter
    def team(self, team):
        self.__team = team

    @property
    def manager(self):
        return self.__player_interface
