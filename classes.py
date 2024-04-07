import random
class Hero():
    def __init__(self, name, hero_class, strength, dexterity, intelligence, hp):

            self.name = name
            self.hero_class = hero_class
            self.strength = strength
            self.dexterity = dexterity
            self.intelligence = intelligence
            self.hp = hp

    def hero_attack(self, opponent):
        damage = self.strength * random.randint(0.75, 1.50)
        print(f"{self.name} attacks and inflicted {int(damage)} points of damage to {opponent.name}")
        opponent.hp -= damage

    def hero_evade(self, opponent):
        negation = self.dexterity * self.strength * self.intelligence * random.uniform(0.010, 0.020)
        if negation < 18:
            print(f"{self.name} blocked the attack of {opponent.name}!")
        else:
            print(f"{self.name} failed to block the attack of {opponent.name} and took {int(opponent.strength)} points of damage")
            self.hp -= opponent.strength  
            
    def hero_cast_skill(self, opponent):
        damage = self.intelligence * random.uniform( 1.25, 3) 
        print(f"{self.name} used a skill inlficting {int(damage)} points of damage to {opponent.name}")
        opponent.hp -= damage

class Warrior(Hero):
    def __init__ (self, name):
        super().__init__(name, hero_class= 'Warrior',hp= 100, strength = 20, dexterity = 10, intelligence= 6)

class Mage(Hero):
    def __init__ (self, name):
        super().__init__(name, hero_class= 'Mage',hp= 100, strength = 8, dexterity = 6, intelligence= 20)

class Archer(Hero):
    def __init__ (self, name):
        super().__init__(name, hero_class= 'Hero',hp= 100, strength = 10, dexterity = 20, intelligence= 12)

    

class Monster():
    def __init__(self, name=None, hp=None, strength=None):
        self.name = name or random.choice(['Goblin', 'Orc', 'Zombie'])
        self.hp = hp or random.randint(90, 120)
        self.strength = strength or random.randint(12, 20)

    def monster_attack(self, opponent):
        damage = self.strength * random.uniform(0.75, 1.25)
        print(f"{self.name} attacks {opponent.name} inflicting {int(damage)} points of damage!")
        opponent.hp -= damage

    def is_alive(self):
        if self.hp <= 0:
            print(f"{self.name} has been slained")
    



    

        