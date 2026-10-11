# secrette_word = "MD1"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False


# while guess != secrette_word and not out_of_guesses:
#     if guess_count < guess_limit:
#         guess = input("Enter guess Word : ")
#         guess_count += 1
#     else:
#         out_of_guesses = True

            
# if out_of_guesses:
#     print("you lose:(")
# else:
#     print("you win:)")    

#===============================================
secret_word = "MD1"
guess = ""
guess_limit = 3

while guess != secret_word and guess_limit > 0:
    guess = input("Enter guess word: ")
    guess_limit -= 1

if guess == secret_word:
    print(f"You win :) The secret word is {guess}")
else:
    print("Out of limit :(")