import random

hangman_words = ['beekeeper', 'spacecraft', 'hallucination']
word = random.choice(hangman_words)
word_list = [*word]
blanks_list = []
for w in word_list:
    blanks_list.append('_')


def check_letter(letter, h_word, r_lives):    
    c = 0
    for a in h_word:        
        if letter == a:
            c = h_word.index(a, c, len(h_word)) 
            blanks_list[c] = letter   
        c = h_word.index(a, c, len(h_word)) + 1

def display(b_list):
    blank = ""
    for l in b_list:
        blank = blank + l[0] + " "
    return blank


def user_letter():
    letter = input("Guess a letter: ").lower()
    return letter

def game_run():
    lives = 7     
    end_of_game = False  
    while lives !=0 and end_of_game != True: 
        input_word = user_letter()          
        check_letter(input_word, word_list, lives)

        if input_word not in word_list:
            print("You guessed {}, that's not in the word. You lose a life".format(input_word))
            lives = lives - 1   

        print(display(blanks_list))
        if word_list == blanks_list:
            print("You win!")
            end_of_game = True
        if lives == 0:
            print("You have ran out of lives, YOU LOSE!!!")

game_run()


    

