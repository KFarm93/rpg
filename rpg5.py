"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time
import sys

class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 0
        self.armor = 0
        self.evade = 0
        self.evadeChance = self.evade * .1

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s!" % (self.name, enemy.name)
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        if random.random() > self.evadeChance:
            points -= self.armor
            self.health -= points
            if points < 1:
                points = 1
            print "%s received %d damage." % (self.name, points)
        else:
            print "%s avoided the attack!" % self.name
            pass


    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)

class Hero(Character):
    def __init__(self):
        self.name = 'Hero'
        self.health = 10
        self.power = 5
        self.coins = 0
        self.armor = 0
        self.evade = 0
        self.evadeChance = self.evade * .1


    def buy(self, item):
        while True:
            if item.cost > self.coins:
                print "You don't have enough coins."
                break
            else:
                self.coins -= item.cost
                item.apply(hero)
                break


    def attack(self, enemy):
        if not self.alive():
            return
        if random.random() < 0.2:
            print "%s prepares a critical hit!" % self.name
            self.power *= 2
            super(Hero, self).attack(enemy)
            self.power /= 2
        else:
            print "%s attacks %s!" % (self.name, enemy.name)
            enemy.receive_damage(self.power)
            time.sleep(1.5)


class Shadow(Character):
    def __init__(self):
        self.name = 'Shadow'
        self.health = 2
        self.power = 3
        self.coins = 8
        self.armor = 0
        self.evade = 9
        self.evadeChance = self.evade * .1


class Zombie(Character):
    def __init__(self):
        self.name = 'Zombie'
        self.health = 20
        self.power = 1
        self.coins = 5
        self.armor = 0
        self.evade = 0
        self.evadeChance = self.evade * .1


    def alive(self):
        return self.health >= 0 or self.health <= 0

class Demon_Hunter(Character):
    def __init__(self):
        self.name = 'Demon Hunter'
        self.health = 10
        self.power = 4
        self.coins = 8
        self.armor = 0
        self.evade = 4
        self.evadeChance = self.evade * .1


    def receive_damage(self, points):
        if random.random() < 0.5:
            self.health -= points
            print "%s received %d damage." % (self.name, points)
            if self.health <= 0:
                print "%s is dead." % self.name
        else:
            print "Demon Hunter avoided the attack!"
            pass

    def attack(self, enemy):
        if not self.alive():
            return
        if random.random() < 0.2:
            print "Demon Hunter's attack power increased!"
            self.power *= 2
        else:
            print "%s attacks %s!" % (self.name, enemy.name)
            enemy.receive_damage(self.power)
            time.sleep(1.5)

class Electrode(Character):
    def __init__(self):
        self.name = 'Electrode'
        self.health = 20
        self.power = 50
        self.coins = 10
        self.armor = 0
        self.evade = 0
        self.evadeChance = self.evade * .1


    def attack(self, enemy):
        if not self.alive():
            return
        if random.random() < 0.15:
            print "%s uses SelfDestruct!" % self.name
            enemy.receive_damage(self.power)
            self.receive_damage(self.power)
        else:
            print "Electrode is charging its SelfDestruct!"
            pass
        time.sleep(1.5)

class Goblin(Character):
    def __init__(self):
        self.name = 'Goblin'
        self.health = 6
        self.power = 2
        self.coins = 10
        self.armor = 0
        self.evade = 0
        self.evadeChance = self.evade * .1


class Wizard(Character):
    def __init__(self):
        self.name = 'Wizard'
        self.health = 8
        self.power = 1
        self.coins = 8
        self.armor = 0
        self.evade = 0
        self.evadeChance = self.evade * .1


    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print "%s swaps its power with %s!" % (self.name, enemy.name)
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Medic(Character):
    def __init__(self):
        self.name = 'Medic'
        self.health = 8
        self.power = 2
        self.coins = 7
        self.armor = 0
        self.evade = 0
        self.evadeChance = self.evade * .1


    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if random.random() > 0.2 and self.health > 0:
            self.health += 2
            print "Medic restored a bit of its health!"





class Battle(object):
    def do_battle(self, hero, enemy):
        print "====================="
        print "Hero faces the %s!" % enemy.name
        print "====================="
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print "-----------------------"
            print "What do you want to do?"
            print "1. Fight %s" % enemy.name
            print "2. Do nothing"
            print "3. Exit Game"
            print "> ",
            input = int(raw_input())
            if input == 1:
                hero.attack(enemy)
            elif input == 2:
                pass
            elif input == 3:
                print "Goodbye!"
                exit(0)
            else:
                print "Invalid input %r" % input
                continue
            enemy.attack(hero)
        if hero.alive():
            print "Enemy %s died!" % enemy.name
            print "You defeated the %s!" % enemy.name
            hero.coins = hero.coins + enemy.coins
            print "You looted %d coins! You now have %d coins." % (enemy.coins, hero.coins)
            return True
        else:

            return False

class Tonic(object):
    cost = 5
    name = 'Tonic'
    def apply(self, character):
        character.health += 2
        if character.health >= 10:
            character.health = 10
        print "%s's health increased to %d." % (character.name, character.health)

class Sword(object):
    cost = 10
    name = 'Sword'
    def apply(self, hero):
        hero.power += 2
        print "%s's power increased to %d." % (hero.name, hero.power)

class Super_Tonic(object):
    cost = 15
    name = 'Super Tonic'
    def apply(self, character):
        character.health += 10
        if character.health >= 10:
            character.health = 10
        print "Hero's health restored to 10."

class Armor(object):
    cost = 8
    name = 'Armor'
    def apply(self, character):
        character.armor += 2
        print "%s's armor level increased to %d." % (hero.name, hero.armor)

class Smoke_Grenade(object):
    cost = 7
    name = 'Smoke Grenade'
    def apply(self, character):
        if character.evade <= 8:
            character.evade += 2
            print "Evasion chance increased."
        else:
            print "It won't have any effect."

class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, Sword, Super_Tonic, Armor, Smoke_Grenade]
    def do_shopping(self, hero):
        while True:
            print "====================="
            print "Welcome to the store!"
            print "====================="
            print "You have %d coins." % hero.coins
            print "What do you want to do?"
            for i in xrange(len(Store.items)):
                item = Store.items[i]
                print "%d. Buy %s (%d)" % (i + 1, item.name, item.cost)

            print "9. Exit Game"
            print "10. Leave"
            input = int(raw_input("> "))


            if input == 9:
                print "Goodbye!"
                sys.exit()
            if input == 10:
                break

            else:
                ItemToBuy = Store.items[input - 1]
                item = ItemToBuy()
                hero.buy(item)

hero = Hero()
enemies = [Goblin(), Medic(), Shadow(), Electrode(), Demon_Hunter(), Zombie(), Goblin(), Wizard()]
battle_engine = Battle()
shopping_engine = Store()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print "YOU LOSE!"
        exit(0)
    shopping_engine.do_shopping(hero)

print "YOU WIN!"
