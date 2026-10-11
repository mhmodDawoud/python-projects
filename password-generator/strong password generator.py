import termcolor
import pyfiglet

print(pyfiglet.figlet_format("GOAT MD1"))
print(termcolor.colored(pyfiglet.figlet_format("Mhmod"), color="red"))

#-------------------------------------------------------------------------------------

import string
import random

s1=list(string.ascii_lowercase)
s2=list(string.ascii_uppercase)
s3=list(string.digits)
s4=list(string.punctuation)

character_number=input("\nEnter number of character for the password: ")

#-------------------------------------------------------------------------------------

while True:
    try:
        character_number=int(character_number)

        if character_number < 6:

            print("you need at least 6 character..")

            character_number=input("\nEnter number of character for the password: ")

        else:
            break
    except:

        print("please enter number only\n")
        
        character_number=input("\nEnter number of character for the password: ")


#-------------------------------------------------------------------------------------

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

#-------------------------------------------------------------------------------------

part_1=round(character_number * (30/100))
part_2=round(character_number * (30/100))

#-------------------------------------------------------------------------------------

password = []

for i in range(part_1):
    password.append(s1[i])
    password.append(s2[i])

for i in range(part_2):
    password.append(s3[i])
    password.append(s4[i])

#-------------------------------------------------------------------------------------

print("".join(password))

#-------------------------------------------------------------------------------------

print(termcolor.colored(pyfiglet.figlet_format("Thank You (●ˇ∀ˇ●)"), color="red"))

#-------------------------------------------------------------------------------------