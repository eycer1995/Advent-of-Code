import hashlib
import time


def main():
    data = "yzbqklnj"
    find = 0
    leading = False
    md5_hash = md5_input = five_zeroes = ""
    while leading is False:
        md5_input = data + str(find)
        md5_hash = hashlib.md5(md5_input.encode('utf-8')).hexdigest()
        print(md5_hash)
        # print(find)
        if md5_hash[0] == "0" and md5_hash[1] == "0" and md5_hash[2] == "0" and md5_hash[3] == "0" and md5_hash[4] == "0" and five_zeroes == "":
            five_zeroes = find
            print("Day 4 part 1 is: " + str(five_zeroes))
        if md5_hash[0] == "0" and md5_hash[1] == "0" and md5_hash[2] == "0" and md5_hash[3] == "0" and md5_hash[4] == "0" and md5_hash[5] == "0":
            leading = True
            print("Day 4 part 2 is: " + str(find))
        find += 1


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print("Finished")
    print(f"Elapsed time: {t2 - t1:0.2f}s")
