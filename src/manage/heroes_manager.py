from model.hero import Hero
from json import load
from random import choice


class HeroesManager:
    def __init__(self, player_interface):
        self.__main = player_interface
        self.__stats = {
            'titles': load(open('assets/titles.json', 'r')),
            'names': load(open('assets/names.json', 'r')),
            'stats': load(open('assets/stats.json', 'r'))
        }
        self.__target_hero = None
        self.__turn_hero = None
        self.__turn_order_tiebreaker = False
        self.__team = {}
        self.__enemy_team = {}

    def create_heroes(self, builds: dict, enemy_team: bool):
        heroes = {}
        slot = 0
        for build in builds:
            slot += 1
            race = self.stats['stats']['races'][builds[build]['race']]
            classe = self.stats['stats']['classes'][builds[build]['classe']]
            element = self.stats['stats']['elements'][builds[build]['element']]
            title = f'{choice(self.stats["names"][builds[build]["race"]])}, {choice(self.stats["titles"][builds[build]["element"]][builds[build]["classe"]])}'
            agility = round(race['agl'] * classe['agl'] * element['agl'])
            health = round(race['hp'] * classe['hp'] * element['hp'])
            damage = round(race['dmg'] * classe['dmg'] * element['dmg'])
            mana = round(race['man'] * classe['man'] * element['man'])
            basic_attack_dmg = round(damage * race['skill']['dmg'])
            basic_attack = race['skill'].copy()
            basic_attack['dmg'] = basic_attack_dmg
            power_attack_dmg = round(damage * classe['skill']['dmg'])
            power_attack = classe['skill'].copy()
            power_attack['dmg'] = power_attack_dmg
            special_attack_dmg = round(damage * element['skill']['dmg'])
            special_attack = element['skill'].copy()
            special_attack['dmg'] = special_attack_dmg
            tiebreaker = self.turn_order_tiebreaker
            skills = {'basic attack': basic_attack, 'power attack': power_attack, 'special attack': special_attack}
            hero = Hero(title=title, damage=damage, health=health, agility=agility, tiebreaker=tiebreaker,
                        mana=mana, skills=skills, build=builds[build], slot=slot, enemy_team=enemy_team)
            heroes[slot] = hero
            if enemy_team:
                self.enemy_team = heroes
            else:
                self.team = heroes
                return heroes

    def predict_attack(self):
        if not self.turn_hero.special_attack['cd'] and self.turn_hero.special_attack['cost'] <= self.turn_hero.mana:
            skill_slot = 3
        elif not self.turn_hero.power_attack['cd'] and self.turn_hero.power_attack['cost'] <= self.turn_hero.mana:
            skill_slot = 2
        else:
            skill_slot = 1
        target_slot = min(self.enemy_team, key=lambda k: self.enemy_team[k].health)
        print(target_slot)
        return skill_slot, target_slot

    def refresh_cooldown(self):
        self.turn_hero.refresh_cooldown()

    def discount_attack(self, skill_slot: int):
        hero = self.turn_hero
        element = ''
        if skill_slot == 1:
            skill_dmg = hero.basic_attack['dmg']
            mana_cost = hero.basic_attack['cost']
        elif skill_slot == 2:
            skill_dmg = hero.power_attack['dmg']
            hero.power_attack['cd'] = hero.power_attack['cdr']
            mana_cost = hero.power_attack['cost']
        else:
            skill_dmg = hero.special_attack['dmg']
            element = hero.element
            hero.special_attack['cd'] = hero.special_attack['cdr']
            mana_cost = hero.special_attack['cost']
        self.target_hero.receive_attack(skill_dmg, element)

    def update_turn_hero(self, hero_id: dict):
        hero_slot = hero_id['slot']
        if hero_id['enemy_team']:
            hero_team = self.enemy_team
        else:
            hero_team = self.team
        hero = hero_team[hero_slot]
        self.turn_hero = hero

    def clear_attributes(self):
        self.turn_hero = None
        self.team = {}
        self.enemy_team = {}

    @property
    def main(self):
        return self.__main

    @property
    def stats(self):
        return self.__stats

    @property
    def target_hero(self):
        return self.__target_hero

    @target_hero.setter
    def target_hero(self, target_hero):
        self.__target_hero = target_hero

    @property
    def turn_hero(self):
        return self.__turn_hero

    @turn_hero.setter
    def turn_hero(self, turn_hero):
        self.__turn_hero = turn_hero

    @property
    def turn_order_tiebreaker(self):
        return self.__turn_order_tiebreaker

    @turn_order_tiebreaker.setter
    def turn_order_tiebreaker(self, turn_order_tiebreaker):
        self.__turn_order_tiebreaker = turn_order_tiebreaker

    @property
    def team(self):
        return self.__team

    @team.setter
    def team(self, team):
        self.__team = team

    @property
    def enemy_team(self):
        return self.__enemy_team

    @enemy_team.setter
    def enemy_team(self, enemy_team):
        self.__enemy_team = enemy_team
