# 文字列のリスト
strings = ["1", "2", "3"]
iter=iter(strings)
print(getattr(strings,'__iter__'))
print(getattr(iter,'__iter__'))
