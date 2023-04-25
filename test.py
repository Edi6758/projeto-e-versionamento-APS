races = [('human', 30, 1500, 21, 150), ('elf', 40, 1333, 17, 220), ('dwarve', 10, 2000, 30, 135), ('orc', 20, 1866, 50, 100), ('gnome', 50, 1000, 10, 350)]
classes = [('warrior', 1.15, 2.2361, 1.15, 1.3), ('assassin', 1.25, 1.25, 1.7, 2.0), ('fighter', 1.35, 1.6, 1.35, 1.2), ('arcanist', 1.1, 1.0, 2.236, 3.0), ('ranger', 1.4125, 1.15, 1.25, 1.5)]
elements = [('flame', 1.25, 1.15, 2.236, 1.4), ('sea', 1.35, 1.25, 1.25, 1.8), ('terra', 1.1, 2.2361, 1.35, 1.6), ('electric', 1.4125, 1.1, 1.7, 1.2), ('nature', 1.15, 1.6, 1.15, 2.3809)]
agile = []
tanker = []
lethal = []
manar = []
for race in races:
    for classe in classes:
        for element in elements:
            titles = f'{race[0]}, {classe[0]}, {element[0]}'
            agility = round(race[1] * classe[1] * element[1])
            health = round(race[2] * classe[2] * element[2])
            damage = round(race[3] * classe[3] * element[3])
            mana = round(race[4] * classe[4] * element[4])

            print(f'{titles}:\n\t agility: {agility}\n\t health: {health}\n\t damage: {damage}\n\t mana: {mana}\n')
