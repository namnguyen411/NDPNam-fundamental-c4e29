x = int(input("Insert number: "))

factorial = 1
if x < 0:
    print("fail")
elif x==0:
    print("1")
else:
    for i in range(1,x+1):
        factorial = factorial*i
    print("The fractorial is: ", factorial)