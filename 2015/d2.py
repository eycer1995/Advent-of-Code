data = open('./2015/d2.txt', 'r').read()

l = 0
w = 0
h = 0
wrapping = 0
smallest = 0
total = 0
# print(data.split())
boxes = data.split()
for box in range(len(boxes)):
    print(boxes[box].split("x"))
    l = int(boxes[box].split("x")[0])
    w = int(boxes[box].split("x")[1])
    h = int(boxes[box].split("x")[2])
    print("This is l: " + str(l) + " This is w: " + str(w) +
          " This is h: " + str(h))
    if ((l*w) <= (h*l)) and ((l*w) <= (h*w)):
        smallest = l*w
    elif ((h*l) <= (l*w)) and ((h*l) <= (h*w)):
        smallest = h*l
    elif ((h*w) <= (l*w)) and ((h*w) <= (h*l)):
        smallest = h*w
    print(smallest)
    wrapping = 2*l*w + 2*w*h + 2*h*l + smallest
    print("Wrapping for current box: " + str(wrapping))
    total = total + wrapping
print(total)
