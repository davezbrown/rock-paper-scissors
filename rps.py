import random

while True:
    print("Enter choice \n 1 = Rock \n 2 = Paper \n 3 = Scissors \n")

    choice = int(input("User turn: "))

    while choice > 3 or choice < 1:
        choice = int(input("enter valid input: "))
        
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'
    print(f"The user's choice is: {choice_name}")

    comp_choice = random.randint(1, 3)


    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'
    print(f"The computer's choice is: {comp_choice_name}")
 
    if choice == comp_choice:
        result = "draw"
    elif((choice == 1 and comp_choice == 2) or
        (choice == 2 and comp_choice ==1 )):
        result = "Paper"
    elif((choice == 1 and comp_choice == 3) or
        (choice == 3 and comp_choice == 1)):
        result = "Rock"
    else:
        result = "Scissors"

    if result == "draw":
        print("Game Tied.")
    elif result == choice_name:
        print("You win!")
    else:
        print("You lose.")

    question = input("Do you want to play again? (Y/N) ")

    if question.lower() == "n":
        break

print("\nThanks for playing!")