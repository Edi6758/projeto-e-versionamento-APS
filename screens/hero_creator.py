from tkinter import StringVar, Text, WORD, END, Frame
from tkinter.ttk import Combobox, Button


class HeroCreatorScreen:
    def __init__(self, manager):
        self.__manager = manager
        self.__stats = self.manager.player_interface.battle_manager.hero_manager.stats
        self.__generate_button = None
        self.__race_vars = []
        self.__class_vars = []
        self.__element_vars = []
        self.__hero_text = None
        self.__frame = None

    def open(self):
        self.frame = Frame(self.manager.window)
        self.manager.window.geometry("700x400")
        self.manager.window.resizable(False, False)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.tkraise()
        self.create_widgets()

    def create_widgets(self):
        for i in range(3):
            race_var = StringVar(value=list(self.stats['stats']['races'].keys())[0])
            class_var = StringVar(value=list(self.stats['stats']['classes'].keys())[0])
            element_var = StringVar(value=list(self.stats['stats']['elements'].keys())[0])

            self.__race_vars.append(race_var)
            self.__class_vars.append(class_var)
            self.__element_vars.append(element_var)

            race_combobox = Combobox(self.frame, textvariable=race_var,
                                     values=list(self.stats['stats']['races'].keys()), state="readonly")
            race_combobox.grid(row=i, column=1)
            race_combobox.current(0)

            class_combobox = Combobox(self.frame, textvariable=class_var,
                                      values=list(self.stats['stats']['classes'].keys()), state="readonly")
            class_combobox.grid(row=i, column=2)
            class_combobox.current(0)

            element_combobox = Combobox(self.frame, textvariable=element_var,
                                        values=list(self.stats['stats']['elements'].keys()), state="readonly")
            element_combobox.grid(row=i, column=3)
            element_combobox.current(0)

        self.__generate_button = Button(
            self.frame, text="Criar time",
            command=self.manager.player_interface.battle_manager.establish_team
        )
        self.__generate_button.grid(row=3, column=0, columnspan=4, pady=20)

        self.__hero_text = Text(self.frame, wrap=WORD, width=80, height=10, bg='gray15', fg='white')
        self.__hero_text.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

    def display_team(self, heroes):
        for hero in heroes:
            self.__hero_text.insert(END, f'{hero.full_name}\nhp {hero.max_health}; dmg {hero.damage}; '
                                         f'agl {hero.agility}; mana {hero.max_mana};\n\n')

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
    def stats(self):
        return self.__stats

    @property
    def hero_text(self):
        return self.__hero_text

    @property
    def frame(self):
        return self.__frame

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

    @frame.setter
    def frame(self, frame):
        self.__frame = frame
