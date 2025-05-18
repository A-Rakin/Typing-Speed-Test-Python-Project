from time import time  #Imports the time() function from the time module.
import random as r  #Imports the random module and gives it an alias r.
from math import floor #Imports the floor() function from math, though in this version it’s not used (can be removed).

#A list of sample test sentences for the user to type.

TEST_SENTENCES = [
    "The quick brown fox jumps over the lazy dog",
    "She sells seashells by the seashore every sunny Saturday",
    "The humming of the refrigerator blended with the ticking of the old wall clock",
    "Practice typing every day to increase both speed and accuracy",
    "In 2025, technology continues to reshape how we live and communicate",
    "Success is not final, failure is not fatal"
]

#Defines a function to calculate typing errors by comparing the target sentence with the user's input.

def calculate_errors(original, user_input):

    """
    Initializes errors counter to 0.

    min_length is the length of the shorter string between original and 

    user_input to avoid index errors during character comparison.

    """
    errors = 0
    min_length = min(len(original), len(user_input))
    
    # Count character mismatches
    for i in range(min_length):

        """
        Compares each character in both strings.

        Increments error count for every mismatch.

        """
        if original[i] != user_input[i]:
            errors += 1
    
    # Count extra characters if user input is longer
    errors += abs(len(original) - len(user_input))
    return errors

    #Defines a function to calculate typing speed and time metrics.

def calculate_typing_metrics(start_time, end_time, user_input):
    """Calculate and return typing speed metrics."""
    time_elapsed = end_time - start_time  #Calculates how long the user took to type the input.

    chars_per_sec = len(user_input) / time_elapsed  #Calculates how many characters the user typed per second.

    words_per_min = (len(user_input.split()) / time_elapsed) * 60 #Calculates words per minute (WPM). split() breaks input into words.

    #Returns the metrics in a dictionary with rounded values for neat display.

    return {
        'time_elapsed': round(time_elapsed, 2),
        'chars_per_sec': round(chars_per_sec, 2),
        'words_per_min': round(words_per_min, 2)
    }

def run_typing_test():
    """Main function to run the typing test."""
    print("\n" * 2)
    print("   ***** Typing Speed Test *****")
    print("\n" * 2)
    

    #Randomly picks a sentence and displays it to the user.

    test_sentence = r.choice(TEST_SENTENCES)
    print(test_sentence)
    print("\n" * 2)
    
    input("Press Enter when ready to start typing...")
    print("Start typing now!\n")


    """
    Records the start time.

    Accepts the user’s typed input.

    Records the end time right after.

    """
    
    start_time = time()
    user_input = input("Type here: ")
    end_time = time()
    
    errors = calculate_errors(test_sentence, user_input)
    metrics = calculate_typing_metrics(start_time, end_time, user_input)

    """
    Computes accuracy as a percentage.
    Formula: accuracy = 100 - (errors / total characters) * 100
    max(0, …) ensures the result is not negative if user made too many errors.
    
    """
    
    accuracy = max(0, (1 - errors/len(test_sentence)) * 100)
    
    print("\nResults:")
    print(f"Time: {metrics['time_elapsed']} seconds")
    print(f"Speed: {metrics['words_per_min']} WPM")
    print(f"Accuracy: {round(accuracy, 1)}%")
    print(f"Errors: {errors}")

if __name__ == '__main__':
    while True:
        choice = input("Ready to begin? (yes/no): ").lower()
        if choice == 'yes':
            run_typing_test()
        elif choice == 'no':
            print("Thank you for using the typing test!")
            break
        else:
            print("Please enter 'yes' or 'no'")