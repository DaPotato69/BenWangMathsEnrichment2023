from fractions import Fraction # simplify fraction later
# negative numbers represent arriving before, and positive represent arriving after 4pm
# example: perceived: -4, actual: 1
# they arrive at 3:56 thinking it is 4pm
# but the actual time is 3:55; 5 minutes before 4pm so -5
# perceived - actual = -4 - 1 = -5
# another example: perceived: 3, actual: -2
# they arrive at 4:03 thinking it is 4pm
# but it is actually 4:05; 5 minutes after 4pm so 5
# perceived - actual = 3 - - 2 = 3 + 2 = 5

# to calculate wait time it is max(absolute(friend 1 - friend 2), absolute(friend 2 - friend 1))
perceived = [-4,-3,3,4]
actual = [-2,-1,1,2]
difference = []
for i in perceived:
    for j in actual:
        difference.append(i-j) # list of all possible watches
waittime = []
for f1index in range(0,len(difference)): #f1index = friend 1
    for f2index in range(0,len(difference)): #f2index = friend 2
        if f1index != f2index: # check that they don't have the same pair of perceived and actual
            waittime.append(abs(difference[f1index]-difference[f2index])) # add the difference of watches to the total list of wait times - abs is absolute because negative wait time is the same as positive wait time
print(*waittime)
print('min:', min(waittime))
print('max:', max(waittime))
print('probability of 5 min: ' + str(Fraction(waittime.count(5),len(waittime)))) # simplify fraction