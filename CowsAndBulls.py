import random


def cows_and_bulls(digits):
    num = [random.randint(0, 9) for n in range(digits)]
    for i in range(0,digits):
        for j in range(0,i):
            if num
    print("Cheat = ", num)
    count = 0
    while count <= 10:
        count += 1
        print("*****Guess number", count, "*****")
        print("Guess the", digits, "digit number: ")
        guess = [int(i) for i in str(input())]
        if guess == num:
            print("You Win!\nIt took you ", count, "guesses")
            break
        else:
            bulls = 0
            cows = 0
            for a in range(0, digits):
                if guess[a] == num[a]:
                    bulls += 1
                elif guess[a] in num:
                    cows += 1
        print("Cows: ", cows, " Bulls: ", bulls)
        print("******************")


digits = int(input("Enter the number of digits: "))
cows_and_bulls(digits)
