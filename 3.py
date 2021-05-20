poradok = input().split(' -> ')
n = int(input())
sp_z = []
for i in range(n):
    sp_z.append(input())
for i in sp_z:
    if i == poradok[0]:
        print(f'{poradok[0]} -> {poradok[1]}')
    elif i == poradok[-1]:
        print(f'{poradok[-2]} -> {poradok[-1]}')
    else:
        s = poradok.index(i)
        print(f'{poradok[s - 1]} -> {poradok[s]} -> {poradok[s + 1]}')
