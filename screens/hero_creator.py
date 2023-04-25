from json import load
from models.hero import Hero
from tkinter import StringVar, Text, WORD, END
from tkinter.ttk import Label, Combobox, Button
from random import choice


class HeroCreatorScreen:
    def __init__(self, manager):
        self.__manager = manager
        self.__generate_button = None
        self.__race_vars = []
        self.__class_vars = []
        self.__element_vars = []
        self.__hero_text = None
        self.__stats = {'titles': load(open('assets/titles.json', 'r')),
                        'names': load(open('assets/names.json', 'r')),
                        'stats': load(open('assets/stats.json', 'r'))}

    def open(self):
        self.manager.window.title("Mount your team")
        self.create_widgets()

    def create_widgets(self):
        for i in range(3):
            race_var = StringVar(value=list(self.__stats['stats']['races'].keys())[0])
            class_var = StringVar(value=list(self.__stats['stats']['classes'].keys())[0])
            element_var = StringVar(value=list(self.__stats['stats']['elements'].keys())[0])

            self.__race_vars.append(race_var)
            self.__class_vars.append(class_var)
            self.__element_vars.append(element_var)

            Label(self.manager.window, text=f"Hero {i + 1}").grid(row=i, column=0, pady=10)

            race_combobox = Combobox(self.manager.window, textvariable=race_var,
                                     values=list(self.__stats['stats']['races'].keys()), state="readonly")
            race_combobox.grid(row=i, column=1)
            race_combobox.current(0)

            class_combobox = Combobox(self.manager.window, textvariable=class_var,
                                      values=list(self.__stats['stats']['classes'].keys()), state="readonly")
            class_combobox.grid(row=i, column=2)
            class_combobox.current(0)

            element_combobox = Combobox(self.manager.window, textvariable=element_var,
                                        values=list(self.__stats['stats']['elements'].keys()), state="readonly")
            element_combobox.grid(row=i, column=3)
            element_combobox.current(0)

        self.__generate_button = Button(self.manager.window, text="Generate Heroes", command=self.generate_heroes)
        self.__generate_button.grid(row=3, column=0, columnspan=4, pady=20)

        self.__hero_text = Text(self.manager.window, wrap=WORD, width=80, height=10, bg='gray15', fg='white')
        self.__hero_text.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

    def create_hero(self, build: tuple):
        title = f'{choice(self.__stats["names"][build[0]])}, {choice(self.__stats["titles"][build[2]][build[1]])}'

        race, classe, element = \
            self.__stats['stats']['races'][build[0]], \
            self.__stats['stats']['classes'][build[1]], \
            self.__stats['stats']['elements'][build[2]]
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
        return Hero(title=title, damage=damage, health=health, agility=agility, mana=mana, skills=skills, build=build)

    def generate_heroes(self):
        heroes = []
        for i in range(3):
            build = (self.__race_vars[i].get(), self.__class_vars[i].get(), self.__element_vars[i].get())
            hero = self.create_hero(build)
            heroes.append(hero)
            self.__hero_text.insert(END, f'Hero {i + 1}:\n{hero.full_name}\n{hero.build}\n\n')
        return heroes

    # Getters
    @property
    def manager(self):
        return self.__manager

    @property
    def race_vars(self):
        return self.__race_vars

    @property
    def class_vars(self):
        return self.__class_vars

    @property
    def element_vars(self):
        return self.__element_vars

    @property
    def generate_button(self):
        return self.__generate_button

    @property
    def hero_text(self):
        return self.__hero_text

    # Setters
    @race_vars.setter
    def race_vars(self, race_vars):
        self.__race_vars = race_vars

    @class_vars.setter
    def class_vars(self, class_vars):
        self.__class_vars = class_vars

    @element_vars.setter
    def element_vars(self, element_vars):
        self.__element_vars = element_vars

    @generate_button.setter
    def generate_button(self, generate_button):
        self.__generate_button = generate_button

    @hero_text.setter
    def hero_text(self, hero_text):
        self.__hero_text = hero_text
