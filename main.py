import time
import random
print("NUMBER GUESSING GAME BY AASTIK")

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

a = random.choice(numbers)
print("""THE RULES ARE AS FOLLOWS ->
1. you have 4 chances to guess the correct number
2. you have 3 hints
3.if u want to get your hint just type hint() in a input
THAT'S  IT ENJOY THE GAME""")

b = input("have u read the rules (y/n)? ")
if b == "y":
    print("alright starting the game")
    time.sleep(1)
    print("initialising the game.....")
    print(".") 
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
else:
    quit()

if a>50:
    print("hint 0 is that your number is greater than 50")
else:
    print("hint 0 is that your number is smaller than 50")

guess_one= int(input("what is ur  guess? ->"))
if guess_one == a:
    print("JACKPOT U GOT IT ON UR FIRST TRY")
    quit()
else:
    print("no your guess is wrong")
hint2 = (input("do you want your second hint? (y/n)"))
if hint2 == "y":
    if a%2 == 0:
        print("your number is even")
    else:
        print("your number is odd")    
        guess_2_2 = input("please enter your second guess ->")
        if guess_2_2 == a:
            print("you got it right!!")
            quit()
        else:
            print("no your guess is wrong u have 2 guess and 1 hint left ")
            hint3_2 = (input("do you want your last hint? (y/n)?"))
            if hint3_2 == "y":
                if a>20:
                    print("the number is greater than 20")
                else:
                    print("your number is smaller than 20")
                guess_3 = int(input("what is your guess?"))
                if guess_3 == a:
                    print("you won!!")
                    quit()
                else:
                    print("you have last 1 chance to guess and 0 hints left")
                final_guess = int(input("what is your final guess?"))
                if final_guess == a:
                    print("you won")
                    quit()
                else:
                    print(f"you lost the game as u dont have any more chances and the answer wasnt correct the correct answer was {a} :<")
                quit()
else:
    guess_2 = input("what is your guess?")
    if guess_2 == a:
        print("u won!!!")
        quit()
    else:
        hint_2_again = input("do you want your hint??")
        if hint_2_again == "y":
            if a%2 == 0:
                print("your number is even")
            else:
                print("your number is odd")
                guess_3 = int(input("what is your 3rd guess?"))
                if guess_3 == a:
                    print("you won!")
                    quit()
                else:
                    print("that isnt the number you have 1 try and 2 hints left")
                hint_3 = input("do you want a hint ?")
                if hint_3 == "y":
                    if a>70:
                        print("the number is greater than 20")
                    else:
                        print("the number is less than 20")
                    final_guess_2 = input("what is your final guess? ") 
                    if final_guess_2 == a:
                        print("you won!!")
                        quit()
                    else:
                        print(f"you lost as u did not guess the correct number and ran out of chances the number was {a}:<")  
                else:
                    final_guess_3 = input("what is your final guess? ")
                    if final_guess_3 == a:
                        print("you won!")
                        quit()
                    else:
                        print(f"you lost as u did not guess the correct number the number was {a} :<")
                        quit()
