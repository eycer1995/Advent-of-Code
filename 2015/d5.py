import time
data = open('./2015/d5.txt', 'r').read().split('\n')


def three_vowels(string):
    count = 0
    for letter in string:
        if letter == "a" or \
           letter == "e" or \
           letter == "i" or \
           letter == "o" or \
           letter == "u":
            count += 1
    if count >= 3:
        return True


def appears_twice(string):
    for letter in range(len(string)):
        if letter >= 1 and string[letter - 1] == string[letter]:
            return True


def forbidden_pairs(string):
    pair = ""
    for letter in range(len(string) - 1):
        pair = string[letter] + string[letter + 1]
        # print(pair)
        if pair == "ab" or \
           pair == "cd" or \
           pair == "pq" or \
           pair == "xy":
            return True


def main1():
    nice_counter = 0
    for string in range(len(data)):
        # print(data[string])
        if appears_twice(data[string]) and \
            three_vowels(data[string]) and not \
            forbidden_pairs(data[string]):
            nice_counter += 1
            # print(f"String #{string}: {data[string]} has 3 vowels")
            # print("has a least 1 repeated letter")
            # print("and does not have a forbidden pair")
            # print("--------------------------")
    print(f"There are {nice_counter} nice words part 1.")


# Day 5 part 2 ------------------------------
def double_pair(string):
    for letter in range(len(string)):
        if string[letter:letter+2] in string[letter+2:]:
            return True
    return False


def middle_letter(string):
    for letter in range(len(string) - 2):
        if string[letter] == string[letter + 2]:
            return True


def main2():
    nicest_counter = 0
    for string in range(len(data)):
        if double_pair(data[string]) and middle_letter(data[string]):
            nicest_counter += 1
            # print(f"String #{string}: {data[string]} has a double pair")
            # print("------------------------")
    print(f"There are {nicest_counter} words in part 2.")


if __name__ == "__main__":
    t1 = time.perf_counter()
    main1()
    main2()
    t2 = time.perf_counter()
    print("Finished")
    print(f"Elapsed time: {t2 - t1:0.2f}s")
