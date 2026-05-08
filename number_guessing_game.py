import random

best_score = None

print("-"*40)
print("HELLO USER")
print("WELCOME TO GAME")
print("-"*40)

while True:

    choice = int(input("\nENTER THE DIFFICULTY LEVEL\nEASY : 1\nMODERATE : 2\nHARD : 3\n\nENTER : "))

    levels = {1:50, 2:100, 3:200}
    max_range = levels.get(choice, 50)

    number = random.randint(1, max_range)
    attempt = 0

    while True:
        guess = int(input("GUESS THE NUMBER : "))
        attempt += 1
        difference = abs(guess - number)

        if guess > number:
            if difference >= 20:
                print("HINT : TOO HIGH")
            elif difference >= 10:
                print("HINT : HIGH")
            else:
                print("HINT : CLOSE")

        elif guess < number:
            if difference >= 20:
                print("HINT : TOO LOW")
            elif difference >= 10:
                print("HINT : LOW")
            else:
                print("HINT : CLOSE")

        else:
            print("\n" + "*"*40)
            print("CORRECT")
            print("*"*40 + "\n")

            if best_score is None or attempt < best_score:
                best_score = attempt

            print("ATTEMPTS :", attempt)
            print("BEST SCORE :", best_score)

            break   # ✅ only here

    play_again = input("Want to play again? (yes/no): ")

    if play_again.lower() not in ["yes", "y"]:
        break