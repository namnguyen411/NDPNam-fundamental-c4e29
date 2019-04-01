
answer = input("Welcome to our shop, what do you want (C,R,U,D)")

menu = ['T-Shirt','Sweater']

if answer == 'r':
    print("Our items: {}".format(menu))
elif answer == 'c':
    x = input("Enter new item: ")
    menu.append(x)
    print(menu)
elif answer == 'u':
    y = int(input("Update position: "))
    z = input("New item: ")
    menu[y - 1] = z
    print(menu)
elif answer == 'd':
    t = int(input("Delete position: "))
    del menu[t - 1]
    print(menu)


