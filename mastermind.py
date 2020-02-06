import random
# ugh
print(" --- MASTERMIND --- \n")
print("Guess the secret number code in as few tries as possible.")
print("I have randomized 4 numbers so you can guess them.")
print("Please, enter your number.")

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
attempts = 0
game = True

while game:
    number_code = random.sample(numbers, 4)
    print(number_code)

    correct_number = ""
    guessed_number = ""
    wrong_number = ""
    player_guess = input().upper()
    attempts += 1

    if len(player_guess) != len(number_code):
        print("\nThe secret code has exactly four numbers. I know, you can count to four. Try again!")
        continue

    if correct_number != "CCCC":
        for i in range(4):
            print(number_code[i])
            if player_guess[i] == number_code[i]:
                correct_number += "C"
            if player_guess[i] != number_code[i] and player_guess[i] in number_code:
                guessed_number += "I"
            if player_guess[i] != number_code[i]:
                print(wrong_number)
                wrong_number += "N"
        print(correct_number + guessed_number + wrong_number + "\n")

    if correct_number == "CCCC":
        if attempts == 1:
            print("Wow! You guessed at the first attempt!")
        else:
            print("Well done... You needed " + str(attempts) + " attempts to guess.")
        game = False

    if attempts >= 1 and attempts < 6 and correct_number != "NNNN":
        print("Next attempt: ")
    elif attempts >= 6:
        print("You didn't guess! The secret code was: " + str(number_code))
        break

    while not game:
        finish_game = input("\nDo you want to play again (Y/N)?").upper()
        attempts = 0
        if finish_game == "N":
            print("Thanks for the game! Bye, bye!")
            break
        elif finish_game == "Y":
            game = True
            print("So, let's play again... Guess the secret code: ")
