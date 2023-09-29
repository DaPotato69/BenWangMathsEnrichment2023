for hundred in range(1,101): #its actually 1 to 100; stop is not included
    for fifty in range(1,101-hundred): #iterating through every single possible combination but total is still less than 100
        for twenty in range(1,101-fifty):
            for ten in range(1,101-twenty):
                five = 50 - twenty - fifty # 50 (100/2, half of the notes) - twenties - fifties is how many fives you need to satisfy the condition
                if five + ten + twenty + fifty + hundred == 100 and (5 * five) + (10 * ten) + (20 * twenty) + (50 * fifty) + (100 * hundred) == 1000:
                    #part 1: check if 100 notes in total
                    #part 2: check if sum is 100
                    print(five, ten, twenty, fifty, hundred)
                    #if it is print the answer
else:
    print('no 💀') #if nothing found