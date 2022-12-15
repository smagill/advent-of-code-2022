with open("input1-1.txt") as f:
    elf_calories = list()
    total = 0
    for line in f:
        if line == "\n":
            elf_calories.append(total)
            print("done with that elf (🧝).  they have " + str(total) + " calories")
            total = 0
        else:
            num = int(line)
            total = total + num
            print(num)
    elf_calories.sort(reverse=True)
    print("sum of max 3 is: "+str(elf_calories[0]+elf_calories[1]+elf_calories[2]))