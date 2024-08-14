from minions.minion import Minion
from minions.mechanized_gift_horse import MechanizedGiftHorse
from minions.deflectobot import DeflectOBot
from optimize import optimize


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

print(optimize(candidates=[no_taunts, deflectobot_taunts], opposition=opposition))
