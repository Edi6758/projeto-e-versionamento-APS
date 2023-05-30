from dog.dog_actor import DogActor
from dog.dog_interface import DogPlayerInterface
from dog.start_status import StartStatus


class ServerManager(DogPlayerInterface):
    def __init__(self, player_interface):
        super().__init__()
        self.__dog_server_interface = DogActor()
        self.__main = player_interface
        self.__player_name = ''

    def connect_to_server(self):
        self.player_name = self.main.window.input_popup(title='Player Identification',
                                                        message='Como você se chama?')
        if self.player_name is None:
            exit()
        self.try_server_connection()

    def try_server_connection(self):
        message = self.dog_server_interface.initialize(self.player_name, self)
        if message == 'Conectado a Dog Server':
            self.main.window.menu.open()
        else:
            self.main.window.root.after(3000, self.try_server_connection)

    def receive_start(self, start_status: StartStatus):
        code = start_status.get_code()
        if code == '2':
            self.main.heroes_manager.turn_order_tiebreaker = False
            self.main.window.swap_to_teambuilder()

    def receive_attack(self, attack: dict):
        self.main.battle.target_slot(attack['target_slot'])
        self.main.battle.skill_slot(attack['skill_slot'])
        self.main.battle.execute_attack()

    def receive_team(self, builds: dict):
        self.main.heroes_manager.create_heroes(builds=builds, enemy_team=True)
        response = self.main.try_to_prepare_battle()
        if response:
            self.main.prepare_battle()

    def start_match(self):
        self.main.window.menu.start_button['state'] = 'disabled'
        self.try_start()

    def try_start(self):
        start_status = self.dog_server_interface.start_match(2)
        code = start_status.get_code()
        if code == '2':
            self.main.heroes_manager.turn_order_tiebreaker = True
            self.main.window.swap_to_teambuilder()
        else:
            self.main.window.root.after(2000, self.try_start)

    def send_attack(self, attack: dict):
        move = {}
        if self.main.battle.finished:
            match_status = 'finished'
        else:
            match_status = 'progress'
        move['match_status'] = match_status
        move['function'] = 'attack'
        move['attack'] = attack
        self.dog_server_interface.send_move(move)

    def send_team(self, builds: dict):
        move = {'function': 'send_team', 'builds': builds, 'match_status': 'progress'}
        self.dog_server_interface.send_move(move)

    def receive_move(self, a_move: dict):
        if a_move['function'] == 'send_team':
            self.receive_team(a_move['builds'])
        elif a_move['function'] == 'attack':
            self.receive_attack(a_move['attack'])

    def receive_withdrawal_notification(self):
        self.main.battle.finished = True
        self.main.battle.prepare_next_turn()

    @property
    def dog_server_interface(self):
        return self.__dog_server_interface

    @property
    def main(self):
        return self.__main

    @property
    def player_name(self):
        return self.__player_name

    @player_name.setter
    def player_name(self, player_name):
        self.__player_name = player_name
