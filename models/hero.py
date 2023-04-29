from random import choice


class Hero:
    def __init__(self, title: str, damage: int, health: int, agility: int, mana: int, skills: dict, build: tuple):
        self.__full_name = title
        self.__damage = damage
        self.__max_health = health
        self.__health = health
        self.__agility = agility
        self.__team = None
        self.__max_mana = mana
        self.__mana = mana
        self.__build = ' / '.join(build)
        self.__alive = True
        self.__basic_attack = skills['basic attack']
        self.__power_attack = skills['power attack']
        self.__special_attack = skills['special attack']
        self.__element = build[2]

    def element_multiplier(self, defender_element: str):
        strong, weak, critical, null, same = 1.4, .7, 2.0, .5, .9
        element_combinations = {
            'Flame': {'Sea': null, 'Terra': strong, 'Electric': weak, 'Nature': critical, 'Flame': same},
            'Sea': {'Flame': critical, 'Terra': weak, 'Electric': null, 'Nature': strong, 'Sea': same},
            'Terra': {'Sea': strong, 'Flame': weak, 'Electric': critical, 'Nature': null, 'Terra': same},
            'Electric': {'Sea': critical, 'Terra': null, 'Flame': strong, 'Nature': weak, 'Electric': same},
            'Nature': {'Sea': weak, 'Terra': critical, 'Electric': strong, 'Flame': null, 'Nature': same},
        }
        return element_combinations[self.element][defender_element]

    def attack(self, skill_dmg, target, elemental: bool):
        if elemental:
            multiplier = self.element_multiplier(target.element)
            skill_dmg = round(skill_dmg * multiplier)
        if target.health - skill_dmg <= 0:
            target.alive = False
            target.health = 0
            return True
        else:
            target.health -= skill_dmg
            return False

    def auto_skill_selection(self):
        elemental = False
        if not self.special_attack['cd'] and self.mana >= self.special_attack['man_cost']:
            skill_dmg = self.special_attack['dmg']
            elemental = True
            self.mana -= self.special_attack['man_cost']
            self.special_attack['cd'] = self.special_attack['cd_rate']
        elif not self.power_attack['cd'] and self.mana >= self.power_attack['man_cost']:
            skill_dmg = self.power_attack['dmg']
            self.mana -= self.power_attack['man_cost']
            self.power_attack['cd'] = self.power_attack['cd_rate']
        else:
            skill_dmg = self.basic_attack['dmg']
            self.power_attack['cd'] = self.power_attack['cd_rate']
        return skill_dmg, elemental

    def refresh_cooldown(self):
        for skill in (self.basic_attack, self.power_attack, self.special_attack):
            if skill['cd'] > 0:
                skill['cd'] -= 1

    def reset(self):
        self.health, self.mana, self.alive, self.team = \
            self.max_health, self.max_mana, True, None
        self.basic_attack['cd'], self.power_attack['cd'], self.special_attack['cd'] = \
            self.basic_attack['cd_rate'], self.power_attack['cd_rate'], self.special_attack['cd_rate']

    def __lt__(self, other):
        if self.agility == other.agility:
            return choice((True, False))
        return self.agility > other.agility

    def __repr__(self):
        return f"{self.build} Agility {self.agility} Health {self.max_health} " \
               f"Damage {self.damage} Mana {self.max_mana}"

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

    @property
    def agility(self):
        return self.__agility

    @property
    def team(self):
        return self.__team

    @property
    def max_mana(self):
        return self.__max_mana

    @property
    def mana(self):
        return self.__mana

    @property
    def build(self):
        return self.__build

    @property
    def alive(self):
        return self.__alive

    @property
    def basic_attack(self):
        return self.__basic_attack

    @property
    def power_attack(self):
        return self.__power_attack

    @property
    def special_attack(self):
        return self.__special_attack

    @property
    def element(self):
        return self.__element

    @full_name.setter
    def full_name(self, full_name):
        self.__full_name = full_name

    @damage.setter
    def damage(self, damage):
        self.__damage = damage

    @max_health.setter
    def max_health(self, max_health):
        self.__max_health = max_health

    @health.setter
    def health(self, health):
        self.__health = health

    @agility.setter
    def agility(self, agility):
        self.__agility = agility

    @team.setter
    def team(self, team):
        self.__team = team

    @max_mana.setter
    def max_mana(self, max_mana):
        self.__max_mana = max_mana

    @mana.setter
    def mana(self, mana):
        self.__mana = mana

    @build.setter
    def build(self, build):
        self.__build = build

    @alive.setter
    def alive(self, alive):
        self.__alive = alive

    @basic_attack.setter
    def basic_attack(self, basic_attack):
        self.__basic_attack = basic_attack

    @power_attack.setter
    def power_attack(self, power_attack):
        self.__power_attack = power_attack

    @special_attack.setter
    def special_attack(self, special_attack):
        self.__special_attack = special_attack

    @element.setter
    def element(self, element):
        self.__element = element
