import re
stacks = dict()

def do_move(src,dst):
    crate = stacks[src].pop()
    stacks[dst].append(crate)

def do_moves(count,src,dst):
    stacks[dst] += stacks[src][-count:]
    stacks[src] = stacks[src][0:-count]

def print_stacks(stacks):
    for k,v in stacks.items():
        print(str(k)+': '+" ".join(v))

with open("input5-1.txt") as f:
    stack_text = list()
    lines = f.readlines()
    input_line = 0
    # Read the initial state
    while True:
        stack_text.append(lines[input_line])
        input_line += 1
        if lines[input_line] == "\n":
            input_line += 1
            break
    
    # Parse the initial state
    for x_pos in range(0,len(stack_text[-1])):
        m = re.match('(\d+)',stack_text[-1][x_pos:])
        if m:
            index = int(m.group(1))
            stacks[index] = list()
            y_pos = len(stack_text) - 2
            while y_pos >= 0 and stack_text[y_pos][x_pos] != ' ':
                stacks[index].append(stack_text[y_pos][x_pos])
                y_pos -= 1
    
    # Print the initial state
    print_stacks(stacks)

    # Do the moves
    while input_line < len(lines):
        print(lines[input_line])
        m = re.match('move (\d+) from (\d) to (\d)',lines[input_line])
        if not m:
            print("Parse error on line: "+lines[input_line])
            break
        num = int(m.group(1))
        src = int(m.group(2))
        dst = int(m.group(3))
        do_moves(num,src,dst)
        print_stacks(stacks)
        input_line += 1
    
    output = list()
    for stack in stacks.values():
        output.append(stack.pop())
    print("".join(output))