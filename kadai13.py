def isiterable(word):
    return hasattr(word,'__iter__')
def isiterator(word):
    return hasattr(word,'__next__')

list=[1,2,3,4]
word1='a'
word2=1
iter=iter(list)
print(isiterable(word1))
print(isiterator(word1))
print('--------------------')
print(isiterable(list))
print(isiterator(list))
print('--------------------')
print(isiterable(word2))
print(isiterator(word2))
print('--------------------')
print(isiterable(iter))
print(isiterator(iter))
print('--------------------')
print(isiterable(map(int,[])))
print(isiterator(map(int,[])))
print('--------------------')
