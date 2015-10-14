import random

game_rules = """Guess the color sequence game.
Object of the game: Match a randomly chosen color sequence.
Rules:
1) The computer chooses a random sequence comprised of four colors from a list of six colors.
2) The user submits the color sequence guesses separated by a space.
3) The program scores the guesses by giving the number of correct matches and
   number of correct matches in correct positions.
4) The game continues until you guess the correct color sequence.
"""

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo']

def getSecretSequence(sequence_length):
    """ Returns a list of random sequence of a given length. """
    secret_sequence = []
    for i in range(sequence_length):
        color = random.choice(COLORS)
        secret_sequence.append(color)
    return secret_sequence

def getUserSequence(sequence_length):
    """ Allows user to enter a valid sequence comprised of a given length.
        Also checks for the specific length as well as user entry error. """
    user_sequence = []
    while True:
        userInput = input("Please enter a valid color sequence separated by a space:\n").lower()
        user_sequence = userInput.split()
        if len(user_sequence) != sequence_length:
            print("You have entered an invalid input.")
        else:
            mistake = 0
            for item in user_sequence:
                if item not in COLORS:
                    mistake += 1
            if mistake != 0:
                print("Please check your input for spelling mistakes.")
            else:
                break
    return user_sequence

def validate(secret_sequence, user_sequence):
    """ Returns correct matches and correct mathes in correct positions after
        comparing the user guess with the secret sequence. """
    correct_matches = 0
    correct_positions = 0
    secret_copy = secret_sequence[:]
    for i in range(len(secret_sequence)):
        if user_sequence[i] == secret_sequence[i]:
            correct_positions += 1
        if user_sequence[i] in secret_copy:
            correct_matches += 1
            secret_copy.remove(user_sequence[i])
    return (correct_matches, correct_positions)

if __name__ == "__main__":
    print (game_rules)
    print ("The color choices are {}\n".format(COLORS))
    sequence_length = 4
    secret_sequence = getSecretSequence(sequence_length)
    correct_matches = 0
    correct_positions = 0
    while correct_positions != sequence_length:
        user_sequence = getUserSequence(sequence_length)
        correct_matches, correct_positions = (validate(secret_sequence, user_sequence))
        print("Correct matches: {}    Correct positions: {}\n".format(correct_matches, correct_positions))
