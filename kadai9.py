import random
class Cat:
    def __init__(self):
        self.flag=0
    def mew(self,times=1):
        if self.flag==1:
            return 'PURR'
        else:
            return 'MEW! ' * times
    def eat(self,food='cat_food'):
        self.flag=1
    def jump(self):
        self.flag=0
        half=random.randint(0,1)
        if half==0:
            cat=Cat()
            return cat.mew()
        else:
            return 'BUMP!'
        print(self.flag)
bella = Cat()
print(bella.mew(3))
bella.eat('cheese')
print(bella.mew(3))
print(bella.jump())
print(bella.jump())
print(bella.jump())
print(bella.mew(3))
