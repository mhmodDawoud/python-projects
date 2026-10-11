#vowel ===>> a  i o e u

def translate(str):
    translation=""

    for letter in str:
        if letter.lower() in "aieoue":
            if letter.isupper():

               translation += " * "
            else:
                    
                translation += " * "

        else:
            translation += letter


    return translation   

print(translate(input("Enter a phrase: ")))
