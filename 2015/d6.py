import time
data = open("./2015/d6.txt", "r").read().split("\n")


def arrange_light():
    global lights
    lights = []
    for x in range(1000):
        lights.append([])
        for y in range(1000):
            lights[x].append("off")


def count_on():
    count = 0
    for x in range(1000):
        for y in range(1000):
            if lights[x][y] == "on":
                count += 1
    return count


def change_lights(nstate, coor1, coor2):
    for x in range(coor1[0], coor2[0]):
        for y in range(coor1[1], coor2[1]):
            if nstate == "toggle":
                if lights[x][y] == "off":
                    lights[x][y] = "on"
                else:
                    lights[x][y] = "off"
            elif nstate == "off":
                if lights[x][y] == "on":
                    lights[x][y] = "off"
            elif nstate == "on":
                if lights[x][y] == "off":
                    lights[x][y] = "on"


def get_instruction(instruction):
    # print(instruction)
    parts = instruction.split(" ")
    coor1 = []
    coor2 = []
    if parts[0] == "toggle":
        coor1 = parts[1].split(",")
        coor2 = parts[3].split(",")
        coor1 = list(map(int, coor1))
        coor2 = list(map(int, coor2))
        change_lights("toggle", coor1, coor2)
    elif parts[1] == "off":
        coor1 = parts[2].split(",")
        coor2 = parts[4].split(",")
        coor1 = list(map(int, coor1))
        coor2 = list(map(int, coor2))
        change_lights("off", coor1, coor2)
    elif parts[1] == "on":
        coor1 = parts[2].split(",")
        coor2 = parts[4].split(",")
        coor1 = list(map(int, coor1))
        coor2 = list(map(int, coor2))
        change_lights("on", coor1, coor2)


def main():
    arrange_light()
    for instruction in range(len(data) - 1):
        get_instruction(data[instruction])
        # print(f"There are {count_on()} lights on.")


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print("Finished")
    print(f"Elapsed time: {t2 - t1:0.2f}s")
