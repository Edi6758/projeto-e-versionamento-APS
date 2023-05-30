from model.turn_order import TurnOrder


class BattleManager:
    def __init__(self, player_interface):
        self.__main = player_interface
        self.__turn_order = None
        self.__finished = False
        self.__victory = False
        self.__target_slot = None
        self.__skill_slot = None
        self.__player_turn = True
        self.__turn_hero_id = {}

    def create_turn_order(self, team: dict, enemy_team: dict):
        team = list(team.values())
        enemy_team = list(enemy_team.values())
        heroes = team + enemy_team
        self.turn_order = TurnOrder(heroes)

    def avaliate_win_condition(self):
        if not self.__finished:
            remaining_heroes = 3
            remaining_enemy_heroes = 3
            if self.main.heroes_manager.turn_hero is None:
                for hero, enemy_hero in zip(self.main.heroes_manager.team.values(),
                                            self.main.heroes_manager.enemy_team.values()):
                    if not hero.alive:
                        remaining_heroes -= 1
                    if not enemy_hero.alive:
                        remaining_enemy_heroes -= 1
                if not remaining_heroes or not remaining_enemy_heroes:
                    self.finished = True
                    if remaining_heroes:
                        self.victory = True

    def prepare_next_turn(self):
        self.avaliate_win_condition()
        if not self.finished:
            self.update_turn_hero()
            self.update_subsequent_turns()
            self.main.heroes_manager.refresh_cooldown()
            if self.player_turn:
                self.skill_slot, self.target_slot = self.main.heroes_manager.predict_attack()
                self.main.window.battle.unlock_attack_options()
        else:
            self.main.heroes_manager.clear_attributes()
            self.main.window.swap_to_results(self.victory)

    def update_turn_hero(self):
        self.turn_hero_id = self.turn_order.next_hero_to_attack()
        print(self.turn_hero_id)
        self.main.heroes_manager.update_turn_hero(self.turn_hero_id)
        self.main.window.battle.update_turn_hero(self.turn_hero_id, self.player_turn)

    def update_subsequent_turns(self):
        next_turns = self.turn_order.predict_available_turns(10)
        self.main.window.battle.update_header(next_turns)

    def execute_attack(self):
        self.main.heroes_manager.discount_attack(self.skill_slot)
        self.main.window.battle.display_attack(self.skill_slot, self.target_slot)
        self.prepare_next_turn()

    def attack_confirmed(self, skill_slot: int, target_slot: int):
        self.main.window.battle.lock_attack_options()
        self.skill_slot = skill_slot
        self.target_slot = target_slot
        self.main.server.send_attack({'skill_slot': self.skill_slot, 'target_slot': self.target_slot})
        self.execute_attack()

    @property
    def main(self):
        return self.__main

    @property
    def turn_order(self):
        return self.__turn_order

    @turn_order.setter
    def turn_order(self, turn_order: TurnOrder):
        self.__turn_order = turn_order

    @property
    def finished(self):
        return self.__finished

    @finished.setter
    def finished(self, finished: bool):
        self.__finished = finished

    @property
    def victory(self):
        return self.__victory

    @victory.setter
    def victory(self, victory: bool):
        self.__victory = victory

    @property
    def target_slot(self):
        return self.__target_slot

    @target_slot.setter
    def target_slot(self, target_slot: int):
        self.__target_slot = target_slot

    @property
    def skill_slot(self):
        return self.__skill_slot

    @skill_slot.setter
    def skill_slot(self, skill_slot: int):
        self.__skill_slot = skill_slot

    @property
    def player_turn(self):
        return self.__player_turn

    @player_turn.setter
    def player_turn(self, player_turn: bool):
        self.__player_turn = player_turn

    @property
    def turn_hero_id(self):
        return self.__turn_hero_id

    @turn_hero_id.setter
    def turn_hero_id(self, turn_hero_id: dict):
        self.__turn_hero_id = turn_hero_id
