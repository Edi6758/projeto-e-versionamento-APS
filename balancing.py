import heapq
from collections import defaultdict
from json import load, dump
from random import choice, sample
from copy import copy, deepcopy
from itertools import combinations
from math import comb
from fractions import Fraction
from models.hero import Hero


def create_hero(race, classe, element, build: tuple):
    agility = round(race['agl'] * classe['agl'] * element['agl'])
    damage = round(race['dmg'] * classe['dmg'] * element['dmg'])
    health = round(race['hp'] * classe['hp'] * element['hp'])
    mana = round(race['man'] * classe['man'] * element['man'])

    titles_json = load(open('assets/titles.json', 'r'))
    names_json = load(open('assets/names.json', 'r'))
    title = f'{choice(names_json[build[0]])}, {choice(titles_json[build[2]][build[1]])}'

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


def execute_turns_x1(hero1, hero2):
    action_point_heap = [(-hero.agility, hero) for hero in [hero1, hero2]]
    heapq.heapify(action_point_heap)

    while hero1.health > 0 and hero2.health > 0:
        # Update action points for all characters
        for priority, hero in action_point_heap:
            hero.action_points += -priority

        # Find the character with the highest action points
        current_hero = max(action_point_heap, key=lambda x: x[1].action_points)[1]

        if current_hero.action_points >= 100:
            target_hero = hero1 if current_hero == hero2 else hero2
            dmg, is_elemental = current_hero.choose_skill()
            current_hero.attack(target=target_hero, elemental=is_elemental, skill_dmg=dmg)
            current_hero.action_points -= 100

    winner = hero1 if hero1.health > 0 else hero2
    return winner


def calculate_turn_order(team1, team2, num_turns=666):
    all_heroes = team1 + team2

    # Generate a list of tuples with time and hero
    time_hero_tuples = []
    for hero in all_heroes:
        time = Fraction(0)
        while time < 1:
            time += Fraction(1, hero.agility)
            heapq.heappush(time_hero_tuples, (time, hero))

    turns = []

    for _ in range(num_turns):
        while True:
            time, hero = heapq.heappop(time_hero_tuples)
            if hero.alive:
                turns.append(hero)
                next_turn_time = time + Fraction(1, hero.agility)
                heapq.heappush(time_hero_tuples, (next_turn_time, hero))
                break

    return turns


def execute_turns_x3(blue, red):
    turns = calculate_turn_order(blue, red)
    alive_blue_heroes, alive_red_heroes = 3, 3

    while alive_blue_heroes and alive_red_heroes:
        if not len(turns):
            turns = calculate_turn_order([hero for hero in blue if hero.alive], [hero for hero in red if hero.alive])
        current_hero = turns.pop(0)
        enemy_team = red if current_hero.team == 'blue' else blue
        opponents = [hero for hero in enemy_team if hero.alive]

        target_hero = min(opponents, key=lambda hero: hero.health)
        dmg, is_elemental = current_hero.choose_skill()
        defeated = current_hero.attack(target=target_hero, elemental=is_elemental, skill_dmg=dmg)
        if defeated:
            turns = [hero for hero in turns if hero is not target_hero]
            if current_hero.team == 'red':
                alive_blue_heroes -= 1
            else:
                alive_red_heroes -= 1

    return (blue, red) if alive_blue_heroes else (red, blue)


def unique_pairs_DEEPCOPY(teams):
    for i, team1 in enumerate(teams):
        for team2 in teams[i+1:]:
            yield deepcopy(team1), deepcopy(team2)


def round_robin_tournament_x3(heroes):
    teams = list(combinations(heroes, 3))
    common_winners = defaultdict(int)
    common_losers = defaultdict(int)
    counter = 0
    max_battles = comb(len(teams), 2)

    for attackers, defenders in unique_pairs_DEEPCOPY(teams):
        for attacker, defender in zip(attackers, defenders):
            attacker.team, defender.team = 'blue', 'red'
        winning_team, losing_team = execute_turns_x3(attackers, defenders)
        for hero in winning_team:
            common_winners[hero.build] += 1
            hero.reset()
        for hero in losing_team:
            common_losers[hero.build] += 1
            hero.reset()
        if counter % 10000 == 0:
            print(max_battles - counter)

        counter += 1

    win_percentages = {
        hero.build: common_winners[hero.build] / (common_winners[hero.build] + common_losers[hero.build]) * 100
        for hero in heroes
    }
    sorted_win_percentages = {item[0]: item[1] for item in
                              sorted(win_percentages.items(), key=lambda item: item[1], reverse=True)}

    with open(f'sorted_win_percentages_{len(heroes)}.json', 'w') as json_file:
        dump(sorted_win_percentages, json_file, indent=4)


def round_robin_tournament_x1(heroes, battle_function):
    wins = {hero: 0 for hero in heroes}

    for i in range(len(heroes)):
        for j in range(i + 1, len(heroes)):
            attacker = copy(heroes[i])
            defender = copy(heroes[j])
            winner = battle_function(attacker, defender)
            wins[winner] += 1

    sorted_wins = sorted(wins.items(), key=lambda item: item[1], reverse=True)
    sorted_wins_dict = {hero: win_count for hero, win_count in sorted_wins}
    with open('x1_wins.json', 'w') as json_file:
        dump(wins, json_file, indent=4)
    with open('x1_wins_sorted.json', 'w') as json_file:
        dump(sorted_wins_dict, json_file, indent=4)


def need_nerf(is_individual: bool, sample_size=125):
    stats_json = load(open('assets/stats.json', 'r'))
    heroes = []
    for race in stats_json['races'].keys():
        for classe in stats_json['classes'].keys():
            for element in stats_json['elements'].keys():
                heroes.append(create_hero(
                    stats_json['races'][race],
                    stats_json['classes'][classe],
                    stats_json['elements'][element],
                    (race, classe, element))
                )
    if is_individual:
        round_robin_tournament_x1(heroes, execute_turns_x1)
    else:
        round_robin_tournament_x3(sample(heroes, sample_size))


def stronger_team(build_1, build_2, build_3):
    stats_json = load(open('assets/stats.json', 'r'))
    races, classes, elements = stats_json['races'], stats_json['classes'], stats_json['elements']
    champions = []
    for build in (build_1, build_2, build_3):
        champions.append(create_hero(races[build[0]], classes[build[1]], elements[build[2]], build))
    heroes = []
    for race in races.keys():
        for classe in classes.keys():
            for element in elements.keys():
                heroes.append(create_hero(
                    races[race],
                    classes[classe],
                    elements[element],
                    (race, classe, element))
                )
    teams = list(combinations(heroes, 3))
    common_winners = defaultdict(int)
    common_losers = defaultdict(int)
    counter = 0
    for losers in teams:
        for attacker, defender in zip(champions, losers):
            attacker.team, defender.team = 'blue', 'red'
        winning_team, losing_team = execute_turns_x3(champions, list(losers))
        for hero in winning_team:
            common_winners[hero.build] += 1
            hero.reset()
        for hero in losing_team:
            common_losers[hero.build] += 1
            hero.reset()
        if counter % 1000 == 0:
            print(325520 - counter)

        counter += 1

    win_percentages = {
        hero.build: common_winners[hero.build] / (common_winners[hero.build] + common_losers[hero.build]) * 100
        for hero in heroes
    }
    sorted_win_percentages = {item[0]: item[1] for item in
                              sorted(win_percentages.items(), key=lambda item: item[1], reverse=True)}

    with open(f'sorted_win_percentages_againts_tank.json', 'w') as json_file:
        dump(sorted_win_percentages, json_file, indent=4)


# need_nerf(is_individual=False, sample_size=8)
stronger_team(['Dwarf', 'Warrior', 'Terra'], ['Dwarf', 'Warrior', 'Terra'], ['Dwarf', 'Warrior', 'Terra'])
