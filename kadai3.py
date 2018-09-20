n = int(input('n<'))
parity_dict = {}
for i in range(n):
    if i % 2 == 0:
        parity_dict[i] ={'en':'even','ja':'偶数'}
    else:
        parity_dict[i] ={'en':'odd','ja':'奇数'}
print(parity_dict)
