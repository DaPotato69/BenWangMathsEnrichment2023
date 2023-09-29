for hundred in range(1,101): #its actually 1 to 100; stop is not included
    for fifty in range(1,101): #iterating through every single possible combination even if it doesnt add to 100 notes
        for twenty in range(1,101):
            for ten in range(1,101):
                for five in range(1,101):
                    if five + ten + twenty + fifty + hundred == 100 and (5 * five) + (10 * ten) + (20 * twenty) + (50 * fifty) + (100 * hundred) == 1000:
                        #part 1: check if 100 notes in total
                        #part 2: check if sum is 100
                        print(five, ten, twenty, fifty, hundred)
                        #if it is print the answer
else: #if nothing found
    print("nah")

# this code isn't really efficient, but i optimised it a bit for 8b and c