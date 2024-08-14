from minions.minion import Minion
from minions.small_horse import Mechapony


class MechanizedGiftHorse(Minion):
    def __init__(self):
        super().__init__(health=4, attack=4)

    def deathrattle(self):
        print(f"{self} summons 2 small deathrattle horses.")
        return [Mechapony(), Mechapony()]
