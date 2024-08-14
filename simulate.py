import random


from minions.minion import Minion
from minions.deflectobot import DeflectOBot
from minions.mechanized_gift_horse import MechanizedGiftHorse


def select_target(team):
    taunts = [minion for minion in team if minion.taunt]
    if taunts:
        return random.choice(taunts)
    else:
        return random.choice([minion for minion in team])


def summon_minion(minion, team, index):
    if len(team) == 7:
        print(f"{minion} not summoned due to full board")
    print(f"{minion} was summoned!")
    team.insert(index, minion)
    for minion in team:
        if isinstance(minion, DeflectOBot):
            minion.on_minion_summon()


def simulate_attack(attacker_team, defender_team, attacker_index):
    attacker = attacker_team[attacker_index % len(attacker_team)]
    defender = select_target(defender_team)

    print(f"{attacker} attacks {defender}")
    attacker.attack_minion(defender)

    if not attacker.is_alive():
        print(f"{attacker} dies")
        attacker_team = [minion for minion in attacker_team if minion.is_alive()]
        for minion in attacker.deathrattle():
            summon_minion(minion=minion, team=attacker_team, index=attacker_index)

    if not defender.is_alive():
        print(f"{str(defender)} dies")
        dead_defender_index = defender_team.index(defender)
        defender_team = [minion for minion in defender_team if minion.is_alive()]
        for minion in defender.deathrattle():
            summon_minion(minion=minion, team=defender_team, index=dead_defender_index)

    next_attacker_index = (attacker_index + 1) % len(attacker_team) if attacker_team else 0
    return next_attacker_index, attacker_team, defender_team


def print_board(team1, team2):
    str_team1 = [str(minion) for minion in team1]
    str_team2 = [str(minion) for minion in team2]
    print("Team 1 Board: " + " | ".join(str_team1))
    print("Team 2 Board: " + " | ".join(str_team2))


def simulate_battle(team1, team2):
    attacker_index1 = 0
    attacker_index2 = 0
    round_number = 0
    attacker_team = random.choice([0, 1])
    while any(minion.is_alive() for minion in team1) and any(minion.is_alive() for minion in team2):
        if round_number > 0:
            attacker_team = (attacker_team + 1) % 2
        print(f"\n--- Round {round_number} ---")
        print_board(team1, team2)
        round_number += 1

        if attacker_team == 0:
            attacker_index1, team1, team2 = simulate_attack(attacker_team=team1, defender_team=team2, attacker_index=attacker_index1)
        else:
            attacker_index2, team2, team1 = simulate_attack(attacker_team=team2, defender_team=team1, attacker_index=attacker_index2)

    if any(minion.is_alive() for minion in team1):
        print("\nTeam 1 wins!")
        return 1
    elif any(minion.is_alive() for minion in team2):
        print("\nTeam 2 wins!")
        return 2
    else:
        print("\nIt's a tie!")
        return 0


def test_tie():
    team1 = [Minion(health=10, attack=10) for _ in range(7)]
    team2 = [Minion(health=10, attack=10) for _ in range(7)]
    assert simulate_battle(team1, team2) == 0


def test_win1():
    team1 = [Minion(health=10, attack=10, divine_shield=True)]
    team2 = [Minion(health=10, attack=10)]
    assert simulate_battle(team1, team2) == 1


def test_win2():
    team1 = [Minion(health=10, attack=10, divine_shield=True) for _ in range(3)]
    team2 = [Minion(health=10, attack=10) for _ in range(7)]
    assert simulate_battle(team1, team2) == 2


def test_mechanized_gift_horse():
    team1 = [Minion(health=10, attack=10)]
    team2 = [MechanizedGiftHorse()]
    assert simulate_battle(team1, team2) == 0


def test_deflectobot():
    team1 = [Minion(health=10, attack=10) for _ in range(3)]
    team2 = [MechanizedGiftHorse(), DeflectOBot()]
    simulate_battle(team1, team2)
    # not deterministic anymore :)


if __name__ == '__main__':
    # test_tie()
    # test_win1()
    # test_win2()
    # test_mechanized_gift_horse()
    test_deflectobot()
