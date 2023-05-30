from model.hero import Hero
from fractions import Fraction
from functools import reduce
from math import gcd


class TurnOrder:
    class Turn:
        def __init__(self, hero: Hero):
            self.__hero = hero
            self.__next = None

        @property
        def hero(self):
            return self.__hero

        @hero.setter
        def hero(self, hero: Hero):
            self.__hero = hero

        @property
        def next(self):
            return self.__next

        @next.setter
        def next(self, next):
            self.__next = next

    def __init__(self, heroes: list):
        self.__first = None
        self.__turn = 0
        self.__current = None
        self.__length = 0
        self.ordenize(heroes=heroes)

    def ordenize(self, heroes: list):
        gcd_of_n_int = lambda *numbers: reduce(gcd, numbers)
        agiliest_hero_agility = max(heroes, key=lambda hero: hero.agility).agility
        heroes_agility_gcd = gcd_of_n_int(*[hero.agility for hero in heroes])
        addition_waves = range(agiliest_hero_agility // heroes_agility_gcd)
        addition_tracker = {hero: 0 for hero in heroes}
        for _addition_wave in addition_waves:
            current_wave = []
            for hero in addition_tracker:
                addition_tracker[hero] += Fraction(hero.agility, agiliest_hero_agility)
                if addition_tracker[hero] >= 1:
                    addition_tracker[hero] -= 1
                    current_wave.append(hero)
                current_wave.sort(key=lambda hero: addition_tracker[hero], reverse=True)
                for added_hero in current_wave:
                    if self.first is None:
                        self.first = self.Turn(hero)
                        self.length += 1
                    else:
                        current = self.first
                        while current.next is not None:
                            current = current.next
                        current.next = self.Turn(added_hero)
                        self.length += 1

    def next_hero_to_attack(self):
        while self.turn <= self.length + 1:
            if self.turn == self.length:
                self.current = None
                self.turn = 0
            if self.current is None:
                self.current = self.first
                self.turn += 1
                slot_n_team = {'slot': self.current.hero.slot, 'enemy_team': self.current.hero.enemy_team}
                return slot_n_team
            if self.current.hero.alive:
                slot_n_team = {'slot': self.current.hero.slot, 'enemy_team': self.current.hero.enemy_team}
                self.current = self.current.next
                self.turn += 1
                return slot_n_team

    def predict_available_turns(self, quantity: int):
        checkpoint = {'turn': self.turn, 'current': self.current}
        next_heroes_to_attack = [self.next_hero_to_attack() for _available_turn in range(quantity)]
        self.turn = checkpoint['turn']
        self.current = checkpoint['current']
        return next_heroes_to_attack

    @property
    def first(self):
        return self.__first

    @first.setter
    def first(self, first):
        self.__first = first

    @property
    def turn(self):
        return self.__turn

    @turn.setter
    def turn(self, turn):
        self.__turn = turn

    @property
    def current(self):
        return self.__current

    @current.setter
    def current(self, current):
        self.__current = current

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        self.__length = length
