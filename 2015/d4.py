import hashlib

data = "abcdef"
# answer is 609043
find = ""
leading = False
i = 0
# print(hashlib.md5(data.encode('utf-8')).hexdigest())

while leading is False:
    print(i)
    i += 1
    if i == 20:
        leading = True
print("Leading is true")
