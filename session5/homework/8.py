def get_even_list(list):
    even_number =[]
    for i in list:
        if(i%2 == 0):
            even_number.append(i)
    return even_number
        

even_list = get_even_list([1, 2, 5, 9, -10, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")