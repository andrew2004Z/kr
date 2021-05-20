import copy

n = int(input())
sp1 = []
for i in range(n):
    sp1.append(input().replace('@untitled.py', ''))
m = int(input())
sp2 = []
for i in range(m):
    sp2.append(input())
sp_res = []
for i in sp2:
    s = 0
    t = False
    z = copy.deepcopy(i)
    if z not in sp1:
        sp_res.append(z + '@untitled.py')
        t = True
    while True:
        if z not in sp1:
            sp_res.append(z + '@untitled.py')
            sp1.append(z)
            break
        else:
            if s !=  0:
                z = z[:len(z) - len(str(s))]
            s += 1
            z += str(s)
sp = []
[sp.append(item) for item in sp_res if item not in sp]
for i in sp:
    print(i)
