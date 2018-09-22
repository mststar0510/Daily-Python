# 文字列のリスト
strings = [1, 2, 3]
iter=iter(strings)
#print(getattr(strings,'__next__'))
try:
    getattr(iter,'__next__')
    print('ok')
except:
    print('No')
