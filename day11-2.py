import re
import numpy as np

monkeys = list()

class LineQueue:
    def __init__(self,lines):
        self.lines = lines

    def __len__(self):
        return len(self.lines)

    def pop(self):
        l = self.lines.pop()
        print(l)
        return l

def throwTo(num,item):
    monkeys[num].catch(item)

def print_monkeys(lst):
    for m in lst:
        print(m)

def to_arg(s):
    if s == 'old':
        return lambda x: x
    else:
        n = int(s)
        return lambda x: n

class Monkey:
    def __init__(self,lines):
        self.inspections = 0
        self.lcm = 1
        m = re.match('Monkey (\d+):',lines.pop())
        self.number = int(m.group(1))
        m = re.match('Starting items: (.+)',lines.pop())
        self.items = list(map(int,m.group(1).split(', ')))
        m = re.match('Operation: new = ([^ ]+) (.) ([^ ]+)',lines.pop())
        arg1 = to_arg(m.group(1))
        arg2 = to_arg(m.group(3))
        if m.group(2) == '*':
            self.operation = lambda x: arg1(x) * arg2(x)
        if m.group(2) == '/':
            self.operation = lambda x: arg1(x) / arg2(x)
        if m.group(2) == '+':
            self.operation = lambda x: arg1(x) + arg2(x)
        if m.group(2) == '-':
            self.operation = lambda x: arg1(x) - arg2(x)
        m = re.match('Test: divisible by (\d+)',lines.pop())
        self.divisor = int(m.group(1))
        self.test = lambda x: x % self.divisor == 0
        m = re.match('If true: throw to monkey (\d+)',lines.pop())
        self.true_monkey = int(m.group(1))
        m = re.match('If false: throw to monkey (\d+)',lines.pop())
        self.false_monkey = int(m.group(1))
        if lines:
            lines.pop()
    
    def take_turn(self):
        #print('Monkey',self.number)
        for item in self.items:
            self.inspections += 1
            #print('  Inspecting',item)
            item = self.operation(item)
            #print('    Worry now',item)
            item %= self.lcm
            #print('    Worry now',item)
            if self.test(item):
                #print('  Throwing to',self.true_monkey)
                throwTo(self.true_monkey,item)
            else:
                #print('  Throwing to',self.false_monkey)
                throwTo(self.false_monkey,item)
        self.items = list()

    def catch(self,item):
        self.items.append(item)
    
    def __str__(self):
        return 'Monkey '+str(self.number)+': '+', '.join(map(str,self.items))

with open("input11-1.txt") as f:
    lines = f.readlines()
    lines = list(map(lambda x: x.strip(), lines))
    lines.reverse()
    lines = LineQueue(lines)
    while lines:
        monkeys.append(Monkey(lines))
    lcm = 1
    for m in monkeys:
        print('lcm =',lcm)
        lcm *= m.divisor
    print('lcm =',lcm)
    for m in monkeys:
        m.lcm = lcm
    
    print_monkeys(monkeys)

    for round in range(0,10000):
        for m in monkeys:
            m.take_turn()
        if (round + 1) in ([1,20]+list(range(1000,10001,1000))):
            print('== Round',round+1,'==')
            for m in monkeys:
                print('Monkey',m.number,'inspected items',m.inspections,'times.')
    
    print_monkeys(monkeys)

    for m in monkeys:
        print('Monkey',m.number,'inspected items',m.inspections,'times.')
    
    inspections = list(map(lambda x: x.inspections, monkeys))
    inspections.sort(reverse=True)
    print('monkey business:',inspections[0]*inspections[1])