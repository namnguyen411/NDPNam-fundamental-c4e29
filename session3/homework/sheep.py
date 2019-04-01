sheep = [5, 7, 300, 90, 24, 50, 75]
 
print('''Hello, my name is Nam and these are my ship sizes 
{}'''.format(sheep))

max_num = sheep[0]
for i in range (1,len(sheep)):
    if sheep[i] > max_num:
        max_num = sheep[i]
print("Now my biggest sheep has size {} let's sheer it".format(max_num))
sheep.append(8)
sheep.remove(max_num)
print('''After sheering, here is my flock {}'''.format(sheep))

loop = True

while loop:
    answer1 = input("Continue? ")
    total = sum(sheep)
    if answer1 == 'y':
        sheep = [i + 50 for i in sheep]
        print('''One month passed, now here is my flock {}'''.format(sheep))
        answer2 = input("Continue sheering? ")
        total = sum(sheep)
        max_num1 = sheep[0]
        for i in range (1,len(sheep)):
            if sheep[i] > max_num1:
                max_num1 = sheep[i]
        if answer2 == 'y':
            print("Now my biggest sheep has size {} let's sheer it".format(max_num1))
            sheep.remove(max_num1)
            sheep.append(8)
        
            print('''After sheering, here is my flock {}'''.format(sheep))
    
        elif answer2 == 'n':
            loop = False
            print ("My flock has size in {}".format(total))
            print("I would get", total, "*2$", "=", total*2, "$")
        
    elif answer1 == 'n':
            loop = False
            print ("My flock has size in {}".format(total))
            print("I would get", total, "*2$", "=", total*2, "$")

