import random

class animal:
        def __init__(self, is_alive=True, energy=10):
            self.is_alive = is_alive
            self.energy = energy

        def status(self):
            return {'is_alive' : self.is_alive, 'energy' : self.energy}

def live(method):
    def wrapper(self, *args, **kwargs):
        if animal.is_alive:
            return method(self, *args, **kwargs)
    return wrapper


class Lion(animal):
    def __init__(self, is_alive=True, energy=10):
        super().__init__(is_alive,energy)
        super().status()
        self.is_hunting = False

    @live
    def hunt(self):
        if self.energy - 3 >= 0:
            self.energy -= 3
            self.is_hunting= True
        else:
            self.is_hunting = False

    @live
    def eat(self, animal):
        catch = random.randint(0, 1)
        if all((animal.is_alive, self.is_hunting, catch)):
            self.energy += animal.energy
            animal.energy = 0
            animal.is_alive = False

class Zebra(animal):
    def __init__(self, is_alive=True, energy=10):
        super().__init__(is_alive,energy)
        super().status()
    @live
    def eat(self):
        self.energy += 1

lion = Lion()
zebra = Zebra()

print('lion status :', lion.status())
print('zebra status :', zebra.status())

print('_'*40)
lion.hunt()
lion.eat(zebra)

print('lion status :', lion.status())
print('zebra status :', zebra.status())
