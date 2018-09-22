import random
class Cat:
    def __init__(self,name):
        self.flag=True
        self.name=name

    def mew(self,times=1):
        if self.flag==True:
            return 'PURR'
        else:
            return 'MEW! ' * times

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
        print(self.flag)

    def hear(self,noise):
        if noise==self.name:
            return 'MEW?'
        else:
            return '...'
bella = Cat('bella')
print(bella.hear('bella'))
print(bella.hear('tigger'))
