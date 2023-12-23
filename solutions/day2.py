with open("inputs/day2.txt", "r") as f:
    data = f.read().split(",")
    data = [int(x) for x in data]
    i = 0
    data[1] = 12
    data[2] = 2
    while data[i] != 99:
        if (data[i] == 1):
            data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
        elif (data[i] == 2):
            data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
        else:
            print("Error")
            break
        i += 4
    print(data[0])

# Part 2
with open("inputs/day2.txt", "r") as f:
    data = f.read().split(",")
    data = [int(x) for x in data]
    dataCopy = data.copy()
    for noun in range(0, 100):
        for verb in range(0, 100):
            i = 0
            data[1] = noun
            data[2] = verb
            while data[i] != 99:
                if (data[i] == 1):
                    data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
                elif (data[i] == 2):
                    data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
                else:
                    break
                i += 4
            if (data[0] == 19690720):
                print(100 * noun + verb)
                data = dataCopy.copy()
                break
            data = dataCopy.copy()
