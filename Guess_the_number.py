import random
import time


def guess_number():
    count = 0
    print("This is a Number Guessing Game. There are three levels. Pick a level and try to guess the correct number.")
    level = input("Please pick a level by typing 'Easy', 'Medium' or 'Hard':  \n >").lower()

    def play_again():
        time.sleep(2)
        again = input("Would you like to play again? Type 'yes' to start over:").lower()
        if again == "yes":
            guess_number()
        else:
            print("Thank you for playing. Goodbye")
            exit()

    while level == "easy":
        max_trial = 6
        number = random.randint(1, 10)
        print(f'Level: Easy - Number is whole and between 1-10. You have {max_trial} guesses')
        while count < max_trial:
            guess = int(input("Enter your guess here: \n >"))
            if guess == number:
                print("You got it right!")
                play_again()
            else:
                print("That is wrong.")
                count += 1
                print(f'You have {(max_trial - count)} guess(es) left. \n')
        else:
            print(f'You did not guess the right number. number is {number}. Game Over! \n')
            play_again()

    while level == "medium":
        max_trial = 4
        number = random.randint(1, 20)
        print(f'Level: Medium - Number is whole and between 1-20. You have {max_trial} guesses')
        while count < max_trial:
            guess = int(input("Enter your guess here: \n >"))
            if guess == number:
                print("You got it right!")
                play_again()
            else:
                print("That is wrong.")
                count += 1
                print(f'You have {(max_trial - count)} guess(es) left. \n')
        else:
            print(f'You did not guess the right number. number is {number}. Game Over! \n')
            play_again()

    while level == "hard":
        max_trial = 3
        number = random.randint(1, 50)
        print(f'Level: Hard - Number is whole and between 1-50. You have {max_trial} guesses')
        while count < max_trial:
            guess = int(input("Enter your guess here: \n >"))
            if guess == number:
                print("You got it right!")
                play_again()
            else:
                print("That is wrong.")
                count += 1
                print(f'You have {(max_trial - count)} guess(es) left. \n')
        else:
            print(f'You did not guess the right number. number is {number}. Game Over!\n')
            play_again()

    else:
        print("Please read the instruction and try again. \n")
        guess_number()


guess_number()