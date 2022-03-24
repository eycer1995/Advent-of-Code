data = open('./2015/d5.txt', 'r').read().split('\n')


def three_vowels(string):
    count = 0
    for letter in string:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            count += 1
    if count >= 3:
        return True


def appears_twice(string):
    count = 0
    for letter in range(len(string)):
        if letter >= 1 and string[letter - 1] == string[letter]:
            count += 1
    if count >= 1:
        return True


def forbidden_pairs(string):
    pair = ""
    for letter in range(len(string) - 1):
        pair = string[letter] + string[letter + 1]
        # print(pair)
        if pair == "ab" or pair == "cd" or pair == "pq" or pair == "xy":
            return True


nice_counter = 0
for string in range(len(data)):
    # print(data[string])
    if appears_twice(data[string]) and three_vowels(data[string]) and not forbidden_pairs(data[string]):
        nice_counter += 1
        print(f"String #{string}: {data[string]} has 3 vowels")
        print("and has a least 1 repeated letter")
        print(f"String #{string}:{data[string]} does not a permitted pair")
        print("--------------------------")

print(f"There are {nice_counter} nice words.")
