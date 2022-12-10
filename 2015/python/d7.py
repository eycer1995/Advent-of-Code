import time


class Wire():
    def __init__(self, name, value):
        self.name = name
        self.value = value


def get_data():
    lines = []
    with open("./2015/inputs/d7.txt", "r") as f:
        x = f.readline()
        while(x):
            lines.append(x)
            x = f.readline()
        return [(['',''] + l.replace('\n','').split(' '))[-5:] for l in lines]



def process_data(operation):
    count = 0
    for i in range(count):
        print(operation)





def main():
    data = get_data()
    for i in range(len(data)):
        # print(data[i])
        process_data(data[i]) 


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print("Finished")
    print(f"Elapsed time: {t2 - t1:0.2f}s")



