data = open('./2015/d1.txt', 'r').read()
result = 0
# print(data)
for floor in range(len(data)):
    if data[floor] == "(":
        result += 1
    elif data[floor] == ")":
        result -= 1

print(result)
