

class BattleScreen:
    def __init__(self, window_manager):
        self.__manager = window_manager
        self.__frame = None
        self.__skill_slot = 0
        self.__target_slot = 0

    def open(self):
        pass

    def create_widgets(self):
        pass

    def create_header(self):
        pass

    def square(self):
        pass

    def add_png_image(self):
        pass

    def update_turn_hero(self, hero_id: dict, player_turn: bool):
        pass

    def update_header(self, sequence: list):
        pass

    def lock_attack_options(self):
        pass

    def unlock_attack_options(self):
        pass

    @property
    def manager(self):
        return self.__manager

    @property
    def frame(self):
        return self.__frame

    @frame.setter
    def frame(self, frame):
        self.__frame = frame

    @property
    def skill_slot(self):
        return self.__skill_slot

    @skill_slot.setter
    def skill_slot(self, skill_slot):
        self.__skill_slot = skill_slot

    @property
    def target_slot(self):
        return self.__target_slot

    @target_slot.setter
    def target_slot(self, target_slot):
        self.__target_slot = target_slot
