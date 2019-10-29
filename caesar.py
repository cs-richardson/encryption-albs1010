#Albert
'''
This code implements a program that takes in a number input and a plaintext
input. Then the program will output the original plaintext but shift a number
of times depending on the number output.
'''

import sys

alphabets = "abcdefghijklmnopqrstuvwxyz"
up_alphabets = alphabets.upper()
ciphertext = "ciphertext: "


rotate = input(sys.argv[0]+ " ")

#this function checks if the number input is valid

def check_one(rotate):
    for i in rotate:
        if i == " ":
            return False
        
    if rotate == "":
        return False

    elif not rotate.isdigit():
            return False
        
    elif int(rotate) < 0:
        return False

while check_one(rotate) == False:
    
    rotate = input(sys.argv[0]+ " ")

rotate = int(rotate)
    
get_string = input("plaintext: ")

'''
This loop iterates through the string and finds the letter and shifts it by
the number the user inputs with, then takes the letter and stores it in a
variable.
'''

for i in get_string:
    if i in alphabets:
        number = alphabets.index(i) + rotate
        number = number % 26
        ciphertext = ciphertext + alphabets[number]

    elif i in up_alphabets:
        number = up_alphabets.index(i) + rotate
        number = number % 26
        ciphertext = ciphertext + up_alphabets[number]

    else:
        ciphertext = ciphertext + i
    

print(ciphertext)

