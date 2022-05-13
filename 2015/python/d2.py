data = open('./2015/d2.txt', 'r').read()
boxes = data.split()

l = 0
w = 0
h = 0
wrapping = 0
smallest = 0
totalw = 0
ribbon = 0

for box in range(len(boxes)):
# print(boxes[box].split("x"))
    l = int(boxes[box].split("x")[0])
    w = int(boxes[box].split("x")[1])
    h = int(boxes[box].split("x")[2])
# Search for the smallest side 
    if ((l*w) <= (h*l)) and ((l*w) <= (h*w)):
        smallest = l*w
        ribbon = ribbon + 2*l + 2*w + l*w*h
    elif ((h*l) <= (l*w)) and ((h*l) <= (h*w)):
        smallest = h*l
        ribbon = ribbon + 2*h + 2*l + l*w*h
    elif ((h*w) <= (l*w)) and ((h*w) <= (h*l)):
        smallest = h*w
        ribbon = ribbon + 2*h + 2*w + l*w*h
    wrapping = 2*l*w + 2*w*h + 2*h*l + smallest
# print("Wrapping for current box: " + str(wrapping))
    totalw = totalw + wrapping
print("2015 - Day 2 part 1 answer: " + str(totalw))
print("2015 - Day 2 part 2 answer: " + str(ribbon))
