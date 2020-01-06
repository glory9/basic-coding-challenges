
def gridGame(grid, k, rules):
    # Write your code here
    a = 0
    b = 0
    magic = list()
    for _ in rules:
        if _ == 'alive':
            magic.append(_)
    g = 0
    while g < grid_rows:
        h = 0
        count = 0
        while h < grid_columns:
            r = g - 1
            while r < g + 2:
                v = h - 1
                while v < h + 2:
                    gf = grid[r][v]
                    if gf is True:
                        if gf == 1:
                            count = count + 1
                    h = h + 1
                r = r + 1
            if count in magic:
                grid[g][h] = 1
            h = h + 1
        g = g + 1
    return grid



#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

grid_rows = int(input().strip())
grid_columns = int(input().strip())

grid = []

for _ in range(grid_rows):
    grid.append(list(map(int, input().rstrip().split())))

k = int(input().strip())

rules_count = int(input().strip())

rules = []

for _ in range(rules_count):
    rules_item = input()
    rules.append(rules_item)

result = gridGame(grid, k, rules)
print(result)
