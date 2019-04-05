print("Answer the following algebra question: ")
print("If x = 8, then what is the value of 4(x + 3) ?")
answer1 = {
    "1." : 35,
    "2." : 36,
    "3." : 40,
    "4." : 44,
}
for key, value in answer1.items():
    print(key, value)
right = 0  
x = int(input("Your choice: "))
if x == 4:
    print('Bingo')
    right += 1
else:
    print(':(') 

print('Estimate this answer (exact calculation not needed):')
print("Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean?")
answer2 = {
    '1.' : 'About 55',
    '2.' : 'About 65',
    '3.' : 'About 75',
    '4.' : 'About 85',
}
for key, value in answer2.items():
        print(key, value)

y = int(input("Your choice: "))
if y == 2:
    print('Bingo')
    right += 1
else:
    print(':(') 
    
print('You correctly answer', right,'out of 2 questions')