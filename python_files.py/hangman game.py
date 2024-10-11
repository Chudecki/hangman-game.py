import random
import time
possible_letters = [

"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"
,"n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"

]

#words that will be generated
words = ["clock"]

#generated the word
generator = random.choice(words)

#for letter in user_guess:
#    if letter in letters:
#        letters.remove(letter)
def letter_in_word():
    pass
    
    
def main(): 
    
    print(f"this is your word:", end="")
    for letters in generator:
        print("_", "", end="")
        
    print(f"  please enter a letter")
    user_guess = input()
    
    if user_guess in generator:
        letter_in_word()
main()