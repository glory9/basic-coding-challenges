a = [1234,4321]
m = [2345,3214]
#find the fewest number of moves required to make make a equal to m by adding
#or subtracting 1 from each digit in a per move

master = list()
master.append(a)
master.append(m)

dir = list()
for _ in master:
    boss = list()
    for num in _:
        g = list()
        for char in str(num):
            g.append(char)
        boss.append(g)
    dir.append(boss)

moves = 0
a= 0
for item in dir[0]:
    b = 0
    for n in item:
        m = abs(int(n) - int(dir[1][a][b]))
        b = b + 1
        moves = moves + m
    a = a + 1
print("moves needed:", moves)
