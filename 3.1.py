import sys
import copy

nums = []
for line in sys.stdin:
    nums.append(line.rstrip())
c = nums[0]
n = 0
sp = []
for i in nums[1:]:
    t1 = list(copy.deepcopy(c))
    for j in i:
        temp = False
        if j not in t1:
            temp = True
            break
        else:
            t1.pop(t1.index(j))
    if temp != True:
        n += 1
        sp.append(i)
print(n)
for i in sp:
    print(i)
