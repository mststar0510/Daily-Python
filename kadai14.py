def isiterable(word):
    return print(hasattr(word,'__iter__'))

def isiterator(word):
    return print(hasattr(word,'__next__'))

def three_gen():
    i=0
    while(True):
        if '3' in str(i) or i%3==0:
            yield i
        i+=1
g=three_gen()
while(True):
    print(next(g))
    isiterable(g)
    isiterator(g)
