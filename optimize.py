from simulate import simulate_battle
from minions.minion import Minion
from minions.mechanized_gift_horse import MechanizedGiftHorse
from minions.deflectobot import DeflectOBot

simulations_count = 1000

opposition = [Minion(health=20, attack=20) for _ in range(7)]

no_taunts = [
    MechanizedGiftHorse(),
    MechanizedGiftHorse(),
    Minion(health=10, attack=10),
    Minion(health=10, attack=10),
    Minion(health=10, attack=10),
    DeflectOBot(),
    DeflectOBot()
]

deflectobot_taunts = [
    MechanizedGiftHorse(),
    MechanizedGiftHorse(),
    Minion(health=10, attack=10),
    Minion(health=10, attack=10),
    Minion(health=10, attack=10),
    DeflectOBot(taunt=True),
    DeflectOBot(taunt=True)
]

no_taunts_points = 0
deflectobot_taunts_point = 0

# draw yields 0 points
# win yields 1 point
# lose yielads -1 point

for i in range(simulations_count):
    result = simulate_battle(no_taunts, opposition)
    if result == 1:
        no_taunts_points += 1
    elif result == 2:
        no_taunts_points -= 1

    result = simulate_battle(deflectobot_taunts, opposition)
    if result == 1:
        deflectobot_taunts_point += 1
    elif result == 2:
        deflectobot_taunts_point -= 1

print(f"Taunts: {deflectobot_taunts_point}")
print(f"No taunts: {no_taunts_points}")

# Taunts: 1000
# No taunts: -1
