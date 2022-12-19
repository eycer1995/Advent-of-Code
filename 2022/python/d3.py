import string

data = open('./inputs/d3.txt','r').read().split('\n')

print(data)

alphabet = list(string.ascii_letters)
score = 0

#print(len(alphabet))

# Count 
for runstack in range(len(data)):
    # Get each comparment by diving the runstack in hafl
    run_len = len(data[runstack])
    comp1 = data[runstack][0:run_len//2]
    comp2 = data[runstack][run_len//2:]

    print("for runstack: " + data[runstack])
    print("comparment 1 is : " + comp1)
    print("comparment 2 is : " + comp2)
        
    for letter in comp1:
        if letter in comp2:
            print(f"The letter {letter} is on both")
            for i in range(len(alphabet)):
                if alphabet[i] == letter:
                    score = score + i + 1
            break
    print("---")

print(f"The priorities for part 1 is: {score}")
