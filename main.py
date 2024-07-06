# 2024 Leobardo Montes

import random

print("""
Python Wordle
Guess the 5-letter word in 6 tries or less
R = red, character not in word
Y = yellow, character is in the wrong position
G = green, character is in the right position
""")

# get random word from file and assign it as a key
key = random.choice(open('key.txt').read().split()).strip()
# keep track of number of tries
num_of_guess = 1
# used to display accuracy of user input
tracker = ""
# keep track of letters
R = set()
Y = set()
G = set()

# check if user input is a valid word from file
def check(z):
    with open('validWords.txt') as f:
        lines = f.read().split()
    for row in lines:
        if z in row:
            return True
    print("Enter a valid word in the list")
    return False

# checks if the user answer is correct
def win():
    if user_input == key:
        print("you win!")
        return 1

while num_of_guess != 7:  # iterate until the max tries is 6
    user_input = input("enter guess: ")
    tracker = "abcde"
    while len(user_input) != 5 or not check(user_input): # check if word length is exactly 5
        print("Enter a 5-letter word")
        user_input = input("enter guess: ")

    # comparing the user input to the answer character by character, updating the tracker after comparing each character
    for x in range(len(user_input)):
        if user_input[x] == key[x]: # if input and key have the same char, update tracker to green
            G.add(user_input[x])
            tracker = tracker.replace(tracker[x], "G", 1)

        elif user_input[x] in key: # if input char is in key, update tracker to yellow
            Y.add(user_input[x])
            tracker = tracker.replace(tracker[x], "Y", 1)

        elif user_input[x] != key[x]: # if input and key do not have the same char, update tracker to red
            R.add(user_input[x])
            tracker = tracker.replace(tracker[x], "R", 1)

    print(tracker)
    print(user_input)
    print('_____')
    print("Green: ", G)
    print("Yellow: ", Y)
    print("Red: ", R)
    num_of_guess += 1 # increment after a guess

    if win():
        break

else: # losing condition with solution
    print("you lose, the word is " + key)
