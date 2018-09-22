def isiterable(word):
    return print(hasattr(word,'__iter__'))
def isiterator(word):
    return print(hasattr(word,'__next__'))

list=[1,2,3,4]
word1='a'
word2=1
iter=iter(list)
isiterable(word1)
isiterator(word1)
print('--------------------')
isiterable(list)
isiterator(list)
print('--------------------')
isiterable(word2)
isiterator(word2)
print('--------------------')
isiterable(iter)
isiterator(iter)
print('--------------------')
isiterable(map(int,[]))
isiterator(map(int,[]))
print('--------------------')
