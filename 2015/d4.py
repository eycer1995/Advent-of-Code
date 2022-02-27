import hashlib

data = "yzbqklnj"
# answer is 609043
find = 0
leading = False
md5_input = ""
md5_hash = ""
five_zeroes = ""
six_zeroes = ""
while leading is False:
    md5_input = data + str(find)
    md5_hash = hashlib.md5(md5_input.encode('utf-8')).hexdigest()
    print(md5_hash)
    # print(find)
    if md5_hash[0] == "0" and md5_hash[1] == "0" and md5_hash[2] == "0" and md5_hash[3] == "0" and md5_hash[4] == "0" and five_zeroes == "":
        five_zeroes = find
    if md5_hash[0] == "0" and md5_hash[1] == "0" and md5_hash[2] == "0" and md5_hash[3] == "0" and md5_hash[4] == "0" and md5_hash[5] == "0":
        leading = True
        six_zeroes = find
    find += 1
print("Day 4 part 1 is: " + str(five_zeroes))
print("Day 4 part 2 is: " + str(six_zeroes))
print("Finished")
