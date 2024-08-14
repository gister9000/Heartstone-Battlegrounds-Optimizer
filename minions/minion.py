

class Minion:
    def __init__(self, health, attack, taunt=False, divine_shield=False):
        self.health = health
        self.attack = attack
        self.taunt = taunt
        self.divine_shield = divine_shield

    def deathrattle(self):
        return list()

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        if self.divine_shield:
            self.divine_shield = False  # Divine shield blocks the first damage
            print(f"{self} blocked the damage with Divine Shield!")
        else:
            self.health -= damage

    def attack_minion(self, other_minion):
        other_minion.take_damage(self.attack)
        self.take_damage(other_minion.attack)

    def __str__(self):
        return f"({self.__class__.__name__} {self.attack} {self.health}: {'Taunt' if self.taunt else ''}, {'Divine' if self.divine_shield else ''})"
