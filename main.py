from time import time
import random as r
from math import floor

TEST_SENTENCES = [
    "The quick brown fox jumps over the lazy dog",
    "She sells seashells by the seashore every sunny Saturday",
    "The humming of the refrigerator blended with the ticking of the old wall clock",
    "Practice typing every day to increase both speed and accuracy",
    "In 2025, technology continues to reshape how we live and communicate",
    "Success is not final, failure is not fatal"
]

def calculate_errors(original, user_input):
    """Calculate the number of errors in user's typing."""
    errors = 0
    min_length = min(len(original), len(user_input))
    
    # Count character mismatches
    for i in range(min_length):
        if original[i] != user_input[i]:
            errors += 1
    
    # Count extra characters if user input is longer
    errors += abs(len(original) - len(user_input))
    return errors

def calculate_typing_metrics(start_time, end_time, user_input):
    """Calculate and return typing speed metrics."""
    time_elapsed = end_time - start_time
    chars_per_sec = len(user_input) / time_elapsed
    words_per_min = (len(user_input.split()) / time_elapsed) * 60
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
    
    test_sentence = r.choice(TEST_SENTENCES)
    print(test_sentence)
    print("\n" * 2)
    
    input("Press Enter when ready to start typing...")
    print("Start typing now!\n")
    
    start_time = time()
    user_input = input("Type here: ")
    end_time = time()
    
    errors = calculate_errors(test_sentence, user_input)
    metrics = calculate_typing_metrics(start_time, end_time, user_input)
    
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