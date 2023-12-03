contents = []
with open("input.txt") as f:
    contents = f.readlines()

cvs = []

nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for line in contents:
    line = line.rstrip("\n")
    first = last = ""

    for i in range(len(line)):
        char = line[i]
        try:
            char = int(char)
            if first == "": first = char
            else: break
        except:
            for n in nums:
                if line[i:i+len(n)] == n:
                    if first == "":
                        first = nums.index(n) + 1
                    else:
                        break

    for i in range(len(line)-1, 0, -1):
        char = line[i]
        try:
            char = int(char)
            if last == "": last = char
            else: break
        except:
            for n in nums:
                if line[i:i+len(n)] == n:
                    if last == "":
                        last = nums.index(n) + 1
                    else:
                        break
    if last == "": last = first
    cvs.append(f'{first}{last}')

total = 0
for i in cvs:
    total += int(i)

print(total)
