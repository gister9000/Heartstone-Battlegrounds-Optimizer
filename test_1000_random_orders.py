import copy
import random

from minions.minion import Minion
from minions.mechanized_gift_horse import MechanizedGiftHorse
from minions.deflectobot import DeflectOBot
from optimize import optimize


opposition = [Minion(health=15, attack=15) for _ in range(7)]

baseline = [
    MechanizedGiftHorse(),
    MechanizedGiftHorse(),
    Minion(health=10, attack=10),
    Minion(health=10, attack=10),
    Minion(health=10, attack=10),
    DeflectOBot(),
    DeflectOBot()
]

candidates = list()
for i in range(1000):
    random.shuffle(baseline)
    candidates.append(copy.deepcopy(baseline))

points = optimize(candidates=candidates, opposition=opposition)
best = max(points)
best_index = points.index(best)
str_candidates = [str(minion) for minion in candidates[best_index]]
print(" | ".join(str_candidates))
