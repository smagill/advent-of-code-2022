import re

with open("input7-1.txt") as f:
    lines = f.readlines()
    lines.reverse()

# An Entry stores the name and size of either a directory or file.
# If subdir == None then this is a file.
# Otherwise the Entry is a directory and subdir stores a dictionary that contains the contents of the directory.
class Entry:
    def __init__(self,name,size,subdir):
        self.name = name
        self.size = size
        self.subdir = subdir

full_path = list()
dir_tree = Entry('/',None,dict())

def print_entry(e):
    print(e.name, e.size, e.subdir)

def print_entry_rec(e,spaces=0):
    print(f'{" "*spaces}- {e.name} ({"dir" if e.subdir else "file"}, size={e.size})')
    if e.subdir:
        for k,v in e.subdir.items():
            print_entry_rec(v,spaces+2)

def get_node(path):
    ret = dir_tree
    for dir in full_path:
        ret = ret.subdir[dir]
    return ret

def process_cd(path):
    global full_path
    if path == "..":
        full_path.pop()
    elif path == '/':
        full_path = list()
    else:
        full_path.append(path)

def process_ls():
    while len(lines) > 0:
        curr_entry = get_node(full_path)
        print_entry_rec(curr_entry)
        line = lines.pop()
        if line[0] == '$':
            lines.append(line)
            break
        print(line)
        curr_dir = curr_entry.subdir
        m = re.match('dir (\w+)',line)
        if m:
            curr_dir[m.group(1)] = Entry(m.group(1),None,dict())
            continue
        m = re.match('(\d+) ([\w\.]+)',line)
        if m:
            curr_dir[m.group(2)] = Entry(m.group(2),int(m.group(1)),None)
            continue

def sum_dir(dir):
    sum = 0
    for k,v in dir.items():
        print_entry(v)
        if v.subdir:
            v_size = sum_dir(v.subdir)
            dir[k].size = v_size
            sum += v_size
        else:
            sum += v.size
    return sum

def dir_sizes(dir):
    sizes = list()
    for k, v in dir.items():
        if v.subdir:
            sizes.append(v.size)
            sizes += dir_sizes(v.subdir)
    return sizes

while len(lines) > 0:
    print('cwd: /'+'.'.join(full_path))
    print_entry_rec(dir_tree)
    line = lines.pop()
    print(line)
    m = re.match('\$ cd ([/\w\.]+)',line)
    if m:
        process_cd(m.group(1))
        continue
    m = re.match('\$ ls',line)
    if m:
        process_ls()
        continue
    print("Parse error: "+line)

total = sum_dir(dir_tree.subdir)
print('Total size: '+str(total))

sizes = dir_sizes(dir_tree.subdir)
print(sizes)

free_space = 70000000 - total
needed_space = 30000000 - free_space
candidates = filter(lambda x: x > needed_space, sizes)
print(min(candidates))