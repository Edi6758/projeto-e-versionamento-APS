class Hero:
    def __init__(self, title: str, damage: int, health: int, agility: int,
                 mana: int, skills: dict, build: dict, tiebreaker: bool, enemy_team: bool, slot: int):
        self.__full_name = title
        self.__damage = damage
        self.__max_health = health
        self.__health = health
        self.__agility = agility
        self.__max_mana = mana
        self.__mana = mana
        self.__alive = True
        self.__build = build
        self.__basic_attack = skills['basic attack']
        self.__power_attack = skills['power attack']
        self.__special_attack = skills['special attack']
        self.__element = build['element']
        self.__enemy_team = enemy_team
        self.__slot = slot
        self.__tiebreaker = tiebreaker

    def refresh_cooldown(self):
        for skill in (self.basic_attack, self.power_attack, self.special_attack):
            if skill['cd']:
                skill['cd'] -= 1

    # talvez não esteja sendo usada

    # def auto_skill_selection(self):
    #     elemental = False
    #     if not self.special_attack['cd'] and self.mana >= self.special_attack['man_cost']:
    #         skill_dmg = self.special_attack['dmg']
    #         elemental = True
    #         self.mana -= self.special_attack['man_cost']
    #         self.special_attack['cd'] = self.special_attack['cd_rate']
    #     elif not self.power_attack['cd'] and self.mana >= self.power_attack['man_cost']:
    #         skill_dmg = self.power_attack['dmg']
    #         self.mana -= self.power_attack['man_cost']
    #         self.power_attack['cd'] = self.power_attack['cd_rate']
    #     else:
    #         skill_dmg = self.basic_attack['dmg']
    #         self.power_attack['cd'] = self.power_attack['cd_rate']
    #     return skill_dmg, elemental

    def receive_attack(self, dmg: int, element=''):
        if element:
            dmg = self.element_multiplier(element)
        self.health -= dmg
        print(f'-{dmg} de vida -- {self}')
        if self.health < 1:
            self.alive = False

    def element_multiplier(self, attacker_element: str):
        strong, weak, critical, null, same = 1.4, .7, 2.0, .5, .9
        element_combinations = {
            'Flame': {'Sea': null, 'Terra': strong, 'Electric': weak, 'Nature': critical, 'Flame': same},
            'Sea': {'Flame': critical, 'Terra': weak, 'Electric': null, 'Nature': strong, 'Sea': same},
            'Terra': {'Sea': strong, 'Flame': weak, 'Electric': critical, 'Nature': null, 'Terra': same},
            'Electric': {'Sea': critical, 'Terra': null, 'Flame': strong, 'Nature': weak, 'Electric': same},
            'Nature': {'Sea': weak, 'Terra': critical, 'Electric': strong, 'Flame': null, 'Nature': same},
        }
        return element_combinations[attacker_element][self.element]

    def __lt__(self, other):
        if self.agility == other.agility:
            if self.tiebreaker == other.tiebreaker:
                return self.slot > other.slot
            return self.tiebreaker
        return self.agility > other.agility

    @property
    def full_name(self):
        return self.__full_name

    @property
    def damage(self):
        return self.__damage

    @property
    def max_health(self):
        return self.__max_health

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, health):
        self.__health = health

    @property
    def agility(self):
        return self.__agility

    @property
    def max_mana(self):
        return self.__max_mana

    @property
    def mana(self):
        return self.__mana

    @mana.setter
    def mana(self, mana):
        self.__mana = mana

    @property
    def alive(self):
        return self.__alive

    @alive.setter
    def alive(self, alive):
        self.__alive = alive

    @property
    def build(self):
        return self.__build

    @property
    def basic_attack(self):
        return self.__basic_attack

    @basic_attack.setter
    def basic_attack(self, basic_attack):
        self.__basic_attack = basic_attack

    @property
    def power_attack(self):
        return self.__power_attack

    @power_attack.setter
    def power_attack(self, power_attack):
        self.__power_attack = power_attack

    @property
    def special_attack(self):
        return self.__special_attack

    @special_attack.setter
    def special_attack(self, special_attack):
        self.__special_attack = special_attack

    @property
    def element(self):
        return self.__element

    @property
    def enemy_team(self):
        return self.__enemy_team

    @property
    def slot(self):
        return self.__slot

    @property
    def tiebreaker(self):
        return self.__tiebreaker
