import random
class Cat:
    def __init__(self,name):
        self.flag=0
        self.sleepy=0
        self.name=name

    def mew(self,times=1):
        if self.sleepy==0:
            if self.flag==1:
                return 'PURR'
            elif self.flag==0:
                return 'MEW! ' * times
        elif self.sleepy==1:
            return 'zzz'

    def eat(self,food='cat_food'):
        self.flag=1
        if self.sleepy==1:
            self.flag==0
            return 'zzz'

    def jump(self):
        self.flag=0
        half=random.randint(0,1)
        if self.sleepy==0:
            if half==0:
                cat=Cat()
                return cat.mew()
            else:
                return 'BUMP!'
        elif self.sleepy==1:
            return 'zzz'

    def hear(self,noise):
        if self.sleepy==0:
            if noise==self.name:
                return 'MEW?'
            else:
                return '...'
        else:
            return 'zzz'

    def sleep(self):
        self.sleepy=1
        return 'zzz'

    def wake(self):
        self.sleepy=0
        return 'MEW!'

bella = Cat('bella')
print(bella.sleep())
print(bella.jump())
print(bella.hear('bella'))
print(bella.wake())
print(bella.mew())
print(bella.hear('bella'))
