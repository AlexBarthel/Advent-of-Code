contents = []
with open("input.txt") as f:
    contents = f.readlines()

total = 0
for line in contents:
    colon_index = line.index(':')
    gameID = int(line[5:colon_index])
    line = line[colon_index+2:].rstrip("\n")
    sets = line.split(";")
    invalid = True
    for set in sets:
        invalid = True
        colors = set.split(",")
        red = green = blue = 0
        for c in colors:
            c = c.lstrip()
            num = int(c.split(" ")[0])
            match c[-1]:
                case "d": red = num
                case "n": green = num
                case "e": blue = num
        if red > 12: break
        if green > 13: break
        if blue > 14: break
        invalid = False
    
    if not invalid:
        total += gameID

print(total)
