contents = []
with open("input.txt") as f:
    contents = f.readlines()

total = []
for line in contents:
    colon_index = line.index(':')
    gameID = int(line[5:colon_index])
    line = line[colon_index+2:].rstrip("\n")
    sets = line.split(";")

    red = green = blue = 0
    for set in sets:
        colors = set.split(",")
        for c in colors:
            c = c.lstrip()
            num = int(c.split(" ")[0])
            match c[-1]:
                case "d": red = num if (red < num) else red
                case "n": green = num if (green < num) else green
                case "e": blue = num if (blue < num) else blue
    
    power = red * green * blue
    total.append(power)

print(sum(total))
