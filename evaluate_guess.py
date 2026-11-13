# Catherine Kati Casella
# Evaluating guesses and getting a game score


# This will end up being pulled from random 
# in dictionary of languages (covered in Daija's file)
correct_language = "French"
points = {1 : 600,
          2 : 400,
          3 : 200}
max_attempts = 3

def play_game(correct_language):
    """
    Play game and get three tries to win.
    Args:
        correct_language: the language randomly generated. 
        guess: user input guess
    Returns:
        points_scored: points you have scored.
        0: if you lose the game you get 0 points.
    """
    for attempt in range (1, max_attempts + 1):
        guess = input("This language is: ")
        guess.strip().lower()
        if guess == correct_language.lower():
            points_scored = points[attempt]
            # idealistically this data would 
            # be stored in your user stats 
            # that we will connect later on. 
            print(f"Congrats! It was {correct_language}! You earned {points_scored} points.")
            return points_scored
        attempts_left = max_attempts - attempt
        if attempts_left:
            print(f"Not it! Try again. Attempts left: {attempts_left}") 
    print(f"All out of tries! The language was {correct_language}.")
    return 0

def main():
    score = play_game(correct_language)
    
if __name__ == "__main__":
    main()