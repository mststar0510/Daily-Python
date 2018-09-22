import random
class Cat:
    def __init__(self,name):
        self.eat=False
        self.sleepy=False
        self.name=name

    def mew(self,times=True):
        if self.sleepy==True:
            return 'zzz'
        elif self.eat==True:
            return 'PURR'
        elif self.eat==False:
            return 'MEW! ' * times

    def eat(self,food='cat_food'):
        if self.sleepy==True:
            return self.mew()
        self.eat=True

    def jump(self):
        if self.sleepy==True:
            return self.mew()
        half=random.randint(0,1)
        if half==0:
            cat=Cat()
            return cat.mew()
        else:
            return 'BUMP!'
    def hear(self,noise):
        if self.sleepy==True:
            return self.mew()
        elif noise==self.name:
            return 'MEW?'
        else:
            return '...'
    def sleep(self):
        self.sleepy=True
        return 'zzz'

    def wake(self):
        self.sleepy=False
        return 'MEW!'

bella = Cat('bella')
print(bella.sleep())
print(bella.jump())
print(bella.hear('bella'))
print(bella.wake())
print(bella.mew())
print(bella.hear('bella'))
