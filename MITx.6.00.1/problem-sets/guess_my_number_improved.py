def guess_my_number_game(low=0, high=100):
    """
    Ask the user to think of an integer in [low, high).
    The computer guesses using bisection search until it’s correct
    or the user quits by typing 'q'.
    """
    print(f"Please think of a number between {low} and {high} (exclusive)")
    guess_counter = 0 # counts number of guesses we made

    while True:
        guess = (low+high)//2
        guess_counter += 1

        print(f"\nIs your number {guess} ?") # leaves spacing between the this and the previous output
        print(" Enter 'h' if the guess is too high")
        print(" Enter 'l' if the guess is too low")
        print(" Enter 'c' if I guessed it correctly")
        print(" Enter 'q' to quit the game")
        answer = input("Type you choice: ").strip().lower() # trims spaces and returns lower case

        # validating input
        if answer not in ('h', 'l', 'c', 'q'):
            print("⚠️  Invalid input. Please type h, l, c, or q.")
            continue

        # quitting option 
        if answer == "q":
            print("Game aborted, see you next time")
            break

        # bisection updates for lower and upper bound
        if answer == "h":
            high = guess
        elif answer == "l":
            low = guess
        elif answer == "c":
            print(f"\nGame over, it took {guess_counter} guesses")
            print(f"Your secret number was {guess}")
            break

        # sanity check: when (high-low) <= and anser != 'c'
        if high-low <= 1 and answer != 'c':
            print("It seems there's a contradiction. "
                  "You may have mistyped h or l earlier ")
            break

if __name__ == "__main__":
    guess_my_number_game()