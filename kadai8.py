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
bella = Cat()
print(bella.mew(3))
bella.eat('cheese')
print(bella.mew(3))
print(bella.mew(2))
