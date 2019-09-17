word = input("que dice el don: ")
print("\n"*69)
letters = list(word)
guess_arr = []
wrong_counter = 1
side = 0
import sys
from random import randint
#array for hangman
brojon = [" ---|\n",
           "    o\n",
           "    |\n",
           "   /","|","\\","\n",
           "    |\n",
           "   /"," ","\\","\n"]
for i in letters:
    guess_arr.append("_")

#lets start
while True:
    trubro = ""
    for i in range(0,wrong_counter):
        trubro += brojon[i]
    print(trubro)
#print the guesses
    current_letters = ""
    for i in guess_arr:
        current_letters += i + " "
    print(current_letters)
    #guesses
    guess = input("whatcha got stud? ")
    #checking guess
    if guess not in letters:
        wrong_counter += 1
        side = randint(1,6)
        if side == 1:
            print("nah chief, that aint it")
        if side == 2:
            print("do better")
        if side == 3:
            print("ok buddy")
        if side == 4:
            print("dummy dummy stupid little boy")
        if side == 5:
            print("ignorant bastard")
        if side == 6:
            print("jesus christ")
        if brojon[wrong_counter] == "\n" or brojon[wrong_counter] == " ":
            wrong_counter +=1
    else:
        for i in letters:
            if guess in letters:
                letters_pos = letters.index(guess)
                guess_arr[letters_pos] = guess
                letters[letters_pos] = " "
                print("yee")
        
            else:
                break
    #win
    if guess_arr == list(word):
        print("you have paid the troll toll, you may now have the boys soul")
        break
    if wrong_counter == len(brojon):
        trubro = ""
        for i in range(0, wrong_counter):
            trubro += brojon[i]
        print(trubro)
        print("you have failed to pay the troll toll, now the wungi are coming for your soul")
        break
