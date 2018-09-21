import random
class Cat:
    def __init__(self,name):
        self.flag=False
        self.sleepy=False
        self.name=name

    def mew(self,times=True):
        if self.flag==True:
            return 'PURR'
        elif self.flag==False:
            return 'MEW! ' * times
        if self.sleepy=True:
            return 'zzz'

    def eat(self,food='cat_food'):
        self.flag=True

    def jump(self):
        self.flag=False
        half=random.randint(0,1)
        if half==0:
            cat=Cat()
            return cat.mew()
        else:
            return 'BUMP!'
    def hear(self,noise):
        if noise==self.name:
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
