import random
import math

class Warrior:
    def __init__(self, name="Warrior", health=0, attMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attMax = attMax
        self.blockMax = blockMax

    def attack(self):
        attAmt = self.attMax * (random.random() + .5)

        return attAmt

    def block(self):
        blockAmt = self.blockMax * (random.random() + .5)

        return blockAmt

class Battle:
    def startFight(self, warrior1, warrior2):
        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break
            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break

    @staticmethod
    def getAttackResult(warriorA, warriorB):
        warriorAAttAmt = warriorA.attack()
        warriorBBlockAmt = warriorB.block()

        damage2warriorB = math.ceil(warriorAAttAmt - warriorBBlockAmt)

        warriorB.health = warriorB.health = damage2warriorB
        print("{} attacks {} and inflicts with {} damages".format(warriorA.name, warriorB.name, damage2warriorB))
        print("{} is down to {} health".format(warriorB.name, warriorB.health))
        if warriorB.health <= 0:
            print("{} has died and {} is Victorious".format(warriorB.name, warriorA.name))
            return "Game Over"
        else:
            return "Fight Again"

def main():
    maximus = Warrior("Maximus", 50, 20, 10)
    galaxon = Warrior("Galaxon", 50, 20, 10)

    battle = Battle()

    battle.startFight(maximus, galaxon)

main()