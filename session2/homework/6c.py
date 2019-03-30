numb = int(input("Enter a number: "))

for i in range(numb):
    if( i%2==0 ):
        print("x", end=" ")
    else:
        print("*", end=" ")
print()