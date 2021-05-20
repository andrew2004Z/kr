import sys
import copy

nums = []
for line in sys.stdin:
    nums.append(line.rstrip())
sp_p = []
for j, i in enumerate(nums):
    if i == '':
        nums.pop(nums.index(''))
        sp_p.append(j)
sp_ras = []
for j, i in enumerate(sp_p):
    if j != 0:
        sp_ras.append(nums[sp_p[j - 1] +  1:i])
    else:
        sp_ras.append(nums[1:i])
sp_ras1 = []

for i in sp_ras:
    for j in i:
        sp_ras1.append(j)
sp = []
[sp.append(item) for item in sp_ras1 if item not in sp]
sp2 = []
for i in sp:
    ind = i[::-1].index(' ')
    sp1 = [i[:len(i) - ind - 1], i[len(i) - ind:]]
    sp2.append(sp1)
dict1 = {}
for i in sp2:
    if i[1] not in dict1:
        dict1[i[1]] = i[0]
    else:
        dict1[i[1]] = dict1[i[1]] + ', ' + i[0]
sp_res111 = []
for i in dict1:
    sp_res111.append([int(i), dict1[i]])
sp_ress111 = sp_res111.sort(key=lambda i: i[0])

for i in sp_res111:
    print(f'{i[0]}: {i[1]}')