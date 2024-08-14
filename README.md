# Heartstone-Battlegrounds-Optimizer
Heartstone battlegrounds monte carlo simulator created to optimize Deflectobot order and taunts in combination with Mechanized Gift Horse.

For example, after running 1000 simulations with these setups:
```
no_taunts = [
    MechanizedGiftHorse(),
    MechanizedGiftHorse(),
    Minion(health=10, attack=10),
    Minion(health=10, attack=10),
    Minion(health=10, attack=10),
    DeflectOBot(),
    DeflectOBot()
]
```

```
deflectobot_taunts = [
    MechanizedGiftHorse(),
    MechanizedGiftHorse(),
    Minion(health=10, attack=10),
    Minion(health=10, attack=10),
    Minion(health=10, attack=10),
    DeflectOBot(taunt=True),
    DeflectOBot(taunt=True)
]
```

Win == +1 point
Lose == -1 point
Draw == 0 points

against `opposition = [Minion(health=15, attack=15) for _ in range(7)]`, it shows that taunts score 979 points, while no taunts score -499 points.  
