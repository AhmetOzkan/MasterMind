from random import randint


print('Welcome to my Mastermind game, I will generate 4 numbers. Can you guess the order.')
print('This is how the game works, if you get an C it means you are correct')
print('If you get an I it means you are correct but in the wrong place')
print('If you get an N it means you are incorrect')


Number1 = randint(1, 9)
Number2 = randint(1, 9)
Number3 = randint(1, 9)
Number4 = randint(1, 9)

c = 1

while True:

    print(Number1, Number2, Number3, Number4)

    guessA = input("Guess the first number: ")
    guessB = input("Guess the second number: ")
    guessC = input("Guess the third number: ")
    guessD = input("Guess the fourth number: ")

    guessA = int(guessA)
    guessB = int(guessB)
    guessC = int(guessC)
    guessD = int(guessD)

    NumbersWrong = 0

    if guessA == Number1:
        print("C")
    elif guessA == Number2 or guessA == Number3 or guessA == Number4:
        print("I")
        NumbersWrong += 1
    else:
        print("N")
        NumbersWrong += 1

    if guessB == Number2:
        print("C")
    elif guessB == Number1 or guessB == Number3 or guessB == Number4:
        print("I")
        NumbersWrong += 1
    else:
        print("N")
        NumbersWrong += 1

    if guessC == Number3:
        print("C")
    elif guessC == Number1 or guessC == Number4 or guessC == Number2:
        print("I")
        NumbersWrong += 1
    else:
        print("N")
        NumbersWrong += 1

    if guessD == Number4:
        print("C")
    elif guessD == Number1 or guessD == Number2 or guessD == Number3:
        print("I")
        NumbersWrong += 1
    else:
        print("N")
        NumbersWrong += 1

    if NumbersWrong == 0:
        print("Well done! you had 0 numbers wrong")
        break
    else:
        print("You had " + str(NumbersWrong) + " wrong, try again")
