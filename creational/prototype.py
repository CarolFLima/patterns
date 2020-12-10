import copy
import random

class Attacker():
    def __init__(self, strength, color):
        self.strength = strength
        self.color = color

    def shoot(self):
        print(f'{self.color} shoots at {random.randint(0, 180)} degrees')

class Prototype:
    def __init__(self):
        self.objects = dict()
    
    def register(self, identifier, obj):
        self.objects[identifier] = obj
    
    def unregister(self, identifier):
        del self.objects[identifier]
 
    def clone(self, identifier, **attr):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError('Incorrect object identifier: {}'.format(identifier))
        obj = copy.deepcopy(found)
        obj.__dict__.update(attr)
        return obj

if __name__ == "__main__":
    print("ALLLLLLLOOOOOOOOOOO")
    blue_villain = Attacker(10, 'blue')
    blue_villain.shoot()

    prototype = Prototype()
    prototype.register('blue', blue_villain)

    green_villain = prototype.clone('blue', color='green')
    green_villain.shoot()