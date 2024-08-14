# Heartstone-Battlegrounds-Optimizer
Heartstone battlegrounds simulator created to optimize Deflectobot order and taunts in combination with Mechanized Gift Horse.

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

against `opposition = [Minion(health=20, attack=20) for _ in range(7)]`, it shows that taunts score 1000/1000 wins, while no taunts draw on average (one loss more than win, many ties).
