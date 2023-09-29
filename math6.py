def base9(x):
    digits = [] #make empty list
    base9_int = 0 #variable for num in base 9
    while x > 0:
        digits.append(x % 9)#working from right to left
        x = int(x / 9)#divide x by 9 for next digit, and round down
    for x in digits[::-1]:
        base9_int = base9_int * 10 + x#convert to human readable and not just an array
    return base9_int
ans = []
for i in range(0,4):#1st digit, not - 4 is not included
    for j in range(0,4):#2nd digit
        for k in range(0,4):#etc
            for l in range(0,4):
                num = l + k*4 + j*16 + i*64#convert to base 10
                if str(base9(num)) == str(i)+str(j)+str(k):#check if base 9 equals base 4 minus last digit
                    ans.append(str(i)+str(j)+str(k)+str(l))#add to answer array
                print(str(i)+str(j)+str(k)+str(l))#print number just checked - see where computer is up to
print(ans)#print answer
