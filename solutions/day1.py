with open('inputs/day1.txt') as f:
    data = f.read().splitlines()
    total = 0
    for num in data:
        total += int(num)//3 -2
    print(total)

# Part 2
with open('inputs/day1.txt') as f:
    data = f.read().splitlines()
    total = 0
    for num in data:
        fuel = int(num)//3 -2
        while fuel > 0:
            total += fuel
            fuel = fuel//3 -2
    print(total)