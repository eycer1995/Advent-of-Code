import hashlib
import time


def main():
    data = "yzbqklnj"
    find = 0
    part1 = part2 = False
    md5_hash = md5_input = ""
    while (part1 and part2) is False:
        md5_input = data + str(find)
        md5_hash = hashlib.md5(md5_input.encode('utf-8')).hexdigest()
        # print(md5_hash)
        # print(find)
        if md5_hash.startswith("00000") and part1 is False:
            part1 = True
            print("Day 4 part 1 is: " + str(find))
        if md5_hash.startswith("000000") and part2 is False:
            part2 = True
            print("Day 4 part 2 is: " + str(find))
        find += 1


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print("Finished")
    print(f"Elapsed time: {t2 - t1:0.2f}s")
