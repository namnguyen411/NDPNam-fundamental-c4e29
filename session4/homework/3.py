print("Answer the following algebra question: ")
print("If x = 8, then what is the value of 4(x + 3) ?")
answer = {
    "1." : 35,
    "2." : 36,
    "3." : 40,
    "4." : 44,
}
for key, value in answer.items():
    print(key, value)
x = int(input("Your choice: "))
loop = True
while loop:
    if x == 4:
        print('Bingo')
        loop = False
    else:
        print(':(')
        loop = False