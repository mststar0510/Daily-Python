import random
class Cat:

    def __init__(self,name):
        self.eat=False
        self.sleepy=False
        self.name=name

    def sleeping(func):
        def wrapper(self,*args,**kwargs):
            if self.sleepy==True:
                return 'zzz'
            return func(self,*args,**kwargs)
        return wrapper

    @sleeping
    def mew(self,times=True):
        if self.eat==True:
            return 'PURR'
        else:
            return 'MEW! ' * times

    @sleeping
    def eat(self,food='cat_food'):
        self.eat=True
    @sleeping
    def jump(self):
        half=random.randint(0,1)
        if half==0:
            cat=Cat()
            return cat.mew()
        else:
            return 'BUMP!'

    @sleeping
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
