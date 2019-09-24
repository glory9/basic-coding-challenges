cars = [2,10,8,17]
k = 3

lengths = []
c1 = 0
c2 = k
newCars = sorted(cars)

for i in range(len(cars) - k + 1):
    roof = newCars[c1:c2]
    length = max(roof) - min(roof) + 1
    lengths.append(length)
    c1 = c1 + 1
    c2 = c2 + 1

print(min(lengths))
