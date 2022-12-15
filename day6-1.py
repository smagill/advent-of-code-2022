import re

# with open("input6-1.txt") as f:
#     buffer = f.readline()
#     last4 = buffer[0:4]
#     count = 4
#     for c in buffer[4:]:
#         if len(set(last4)) == 4:
#             print(count)
#             exit(0)
#         last4 = last4[1:]
#         last4.append(c)

# with open("input6-1.txt") as f:
#     buffer = f.readline()
#     for i in range(4,len(buffer)):
#         if len(set(buffer[i-4:i])) == 4:
#             print(i)

with open("input6-1.txt") as f:
    buffer = f.readline()
    print(list(filter(lambda x: x != '', list(map(lambda i: (len(set(buffer[i-4:i])) == 4) * str(i), range(4,len(buffer))))))[0])
