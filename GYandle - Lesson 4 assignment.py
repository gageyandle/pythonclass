import random

def main():  
    continue_playing = True

    while continue_playing:  
        user_weapon = get_user_weapon()
        opponent_weapon = get_opponent_weapon()
        determine_winner(user_weapon,  opponent_weapon)

        play_again = input("Play again? (y/n):  ")
        if play_again.lower() != 'y':  
            continue_playing = False

def get_user_weapon():  
    print("Choose your weapon:  ")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    while True:  
        try:  
            user_choice = int(input("Enter your choice (1-3):  "))
            if 1 <= user_choice <= 3:  
                return user_choice
            else:  
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:  
            print("Invalid input. Please enter a number.")

def get_opponent_weapon():  
    return random.randint(1,  3)

def determine_winner(user_weapon,  opponent_weapon):  
    print(f"You chose:  {user_weapon}")
    print(f"Opponent chose:  {opponent_weapon}")

    if user_weapon == opponent_weapon:  
        print("The game is a tie!")
    elif (user_weapon == 1 and opponent_weapon == 3) or \
         (user_weapon == 2 and opponent_weapon == 1) or \
         (user_weapon == 3 and opponent_weapon == 2):  
        print("You win!")
    else:  
        print("You lose!")

if __name__ == "__main__":  
    main()

print("Completed by,  Gage Yandle")


