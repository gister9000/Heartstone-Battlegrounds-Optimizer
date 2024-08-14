from minions.minion import Minion


class DeflectOBot(Minion):
    def __init__(self, taunt=False):
        super().__init__(health=6, attack=3, divine_shield=True, taunt=taunt)

    def on_minion_summon(self):
        if not self.divine_shield:
            print(f"{self.__class__.__name__} regained Divine Shield")
            self.divine_shield = True
        self.attack += 2
        print(f"{self.__class__.__name__} gained +2 attack")
