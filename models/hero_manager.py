from random import choice
from models.hero import Hero
from json import load


class HeroManager:
    def __init__(self, manager):
        self.__manager = manager
        self.__stats = {'titles': load(open('assets/titles.json', 'r')),
                        'names': load(open('assets/names.json', 'r')),
                        'stats': load(open('assets/stats.json', 'r'))}

    def create_heroes(self, builds: list):
        heroes = []
        for build in builds:
            title = f'{choice(self.stats["names"][build[0]])}, ' \
                    f'{choice(self.stats["titles"][build[2]][build[1]])}'
            race, classe, element = \
                self.stats['stats']['races'][build[0]], \
                self.stats['stats']['classes'][build[1]], \
                self.stats['stats']['elements'][build[2]]
            agility = round(race['agl'] * classe['agl'] * element['agl'])
            damage = round(race['dmg'] * classe['dmg'] * element['dmg'])
            health = round(race['hp'] * classe['hp'] * element['hp'])
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

            skills = {'basic attack': basic_attack, 'power attack': power_attack, 'special attack': special_attack}

            hero = Hero(title=title, damage=damage, health=health, agility=agility,
                        mana=mana, skills=skills, build=build)
            heroes.append(hero)
        return heroes

    @property
    def manager(self):
        return self.__manager

    @property
    def stats(self):
        return self.__stats
