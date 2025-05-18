from time import*  #Used to track how long the user takes to type.
import random as r #Used to randomly select a test sentence

if __name__ == '__main__':  #Asks the user if they're ready to start.
    while True:
        check = input("Ready to begin: yes or no :")

        test=["The quick brown fox jumps over the lazy dog",
              "She sells seashells by the seashore every sunny Saturday",
              "The humming of the refrigerator blended with the ticking of the old wall clock",
              "Practice typing every day to increase both speed and accuracy",
              "In 2025, technology continues to reshape how we live and communicate",
              "Success is not final, failure is not fatal"]
        
        test1=r.choice(test)  #Randomely Generate the test line from test

        #Records the time before and after user input

        time_1 = time()
        testinput = input("Enter : ")
        time_2 = time()


