x = input("Enter: ")
x = x.lower()  
alphabet = 'abcdefghijklmnopqrstuvwxyz'
letter_count = {}
for character in x:
    if character in alphabet: 
        if character in letter_count:
            letter_count[character] += 1
        else:
            letter_count[character] = 1
keys = letter_count.keys()
for character in sorted(keys):
    print(character, letter_count[character])