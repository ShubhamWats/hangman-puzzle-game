import random
from words import words
from words import alphabets



def get_valid_word(words):
    word = random.choice(words)
    
    while "-" in word or " " in word or len(word)>3:
        word = random.choice(words)

    return word

def hangman(words, alphabet):
    alphabets = set(alphabet)
    word = get_valid_word(words).upper()
    letters = set(word)
    used_letters = set()
    i=0
    lives = 100
    while (len(letters)>0):
        word_mask = [letter if letter in used_letters else '-' for letter in word]
        print("Current Word: ", ' '.join(word_mask))
        if '-' not in word_mask:
            print("You Won! Word was: ", ''.join(word_mask))
            break

                

        user_input = input("Enter a letter: ").upper()

        if user_input not in letters:
            lives-=1
            if lives == 0:
                print("0 Lives! You Lost!")
                break

        
        if user_input in (alphabets - used_letters):
            used_letters.add(user_input)
            print (" ".join(used_letters))
            print("Lives Remaining: ", lives)
            
            


        elif user_input in used_letters:
            print("No repetetions please. Enter a new letter")
        else:
            print("Only alphabet are allowed!")


        
            
        
    




hangman(words, alphabets)
    
