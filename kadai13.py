def isiterable(word):
    try:
        word.__iter__(self)
        print('イテラブルです。')
    except:
        print('イテラブルではありません。')

def isiterator(word):
    #try:
        first=word[0],
        for i in word:
            pass
        if first==word[0]:
            print('イテレーターではありません。')
        elif first!=word[0]:
            printe('イテレーターです。')
    except :
        print('イテレーターではありません。')

list0=[1,2,3,4]
list1=[1,2,3,4,5,6]
word1='a'
word2=1
iter1=iter(list0)
iter2=iter(list1)
'''isiterable(list0)
isiterator(list0)
isiterable(word1)
isiterator(word1)
isiterable(word2)
isiterator(word2)
isiterable(list1)
isiterator(list1)
isiterable(iter1)'''
isiterator(iter2)
