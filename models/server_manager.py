from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor


class ServerManager(DogPlayerInterface):
    def __init__(self, player_interface):
        super().__init__()
        self.__dog_server_interface = DogActor()
        self.__player_interface = player_interface
        self.__player_name = ''
        self.starter = 'not starter'

    def connect_to_server(self):
        self.player_name = self.player_interface.window_manager.input_popup(title='Player Identification',
                                                                            message='Como você se chama?')
        print(self.trying_connection())
        self.player_interface.window_manager.main_menu.open()

    def trying_connection(self):
        message = self.dog_server_interface.initialize(self.player_name, self)
        if message != 'Conectado a Dog Server':
            print('tentando novamente em 3 segundos')
            self.player_interface.window_manager.window.after(3000, self.trying_connection())
        else:
            return message

    def start_match(self):
        start_status = self.dog_server_interface.start_match(2)
        message = start_status.get_message()
        code = start_status.get_code()
        print(message)
        print(code)
        if code == '2':
            self.starter = 'esse é o starter'
            print(self.starter)
            self.player_interface.window_manager.swap_to_hero_creator()
        elif code == '1':
            print('tentando novamente em 3 segundos')
            self.player_interface.window_manager.window.after(3000, self.start_match)

    def receive_start(self, start_status):
        code = start_status.get_code()
        message = start_status.get_message()
        print(message)
        print(code)
        if code == '2':
            print(self.starter)
            self.player_interface.window_manager.swap_to_hero_creator()

    def send_attack(self, move: tuple):
        match_status = 'next'  # reforma necessaria
        attack = {'skill_dmg': move[0], 'is_elemental': move[1]}
        move = {'attack': attack, 'rematch': move[2], 'function': 'attack', 'match_status': match_status}
        self.dog_server_interface.send_move(move)

    def send_team(self, builds: list):
        move = {'function': 'send_team', 'team': builds, 'match_status': 'next'}
        self.dog_server_interface.send_move(move)
        if self.player_interface.battle_manager.enemy_team:
            self.player_interface.battle_manager.prepare_battle()

    def receive_move(self, a_move):
        if a_move['function'] == 'attack':
            self.receive_attack(move=a_move)
        elif a_move['function'] == 'send_team':
            self.receive_team(move=a_move)

    def receive_team(self, move):
        print(move)
        heroes = self.player_interface.battle_manager.hero_manager.create_heroes(builds=move['team'])
        self.player_interface.battle_manager.enemy_team = {f'{index}': hero for hero, index in enumerate(heroes)}
        if self.player_interface.battle_manager.team:
            self.player_interface.battle_manager.prepare_battle()

    def receive_attack(self, move):
        print(move)

    def receive_withdrawal_notification(self):
        self.starter = 'nao starter'
        self.player_interface.window_manager.popup('O oponente abandonou a partida')
        self.player_interface.window_manager.swap_to_main_menu()
        self.player_interface.postmatch_cleanup()

    @property
    def player_interface(self):
        return self.__player_interface

    @property
    def dog_server_interface(self):
        return self.__dog_server_interface

    @property
    def player_name(self):
        return self.__player_interface

    @player_name.setter
    def player_name(self, player_name):
        self.__player_name = player_name
