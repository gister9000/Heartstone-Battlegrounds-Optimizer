from minions.minion import Minion


class Mechapony(Minion):
    def __init__(self):
        super().__init__(health=2, attack=2)

    def deathrattle(self):
        print(f"{self} summons 1-1 minion")
        return [Minion(health=1, attack=1)]
