from time import*  #Used to track how long the user takes to type.
import random as r #Used to randomly select a test sentence

'''
Defining a method called mistake() which literally

Compares each character of the original sentence (par_test) with the user's input (user_test).

If characters don't match, or an index error occurs (user typed fewer characters), it counts an error.

Count will be incremented

Returns the total number of errors.

'''

def mistake(par_test,user_test):
    error=0
    for i in range(len(par_test)):
        try:
            if par_test[i]!=user_test[i]:
                error+=1
        except:
            error+=1
    return error


'''
Defining a method called speed_time() which literally

Calculates the time difference between start (time_start) and end (time_end) of typing.

Computes the typing speed in characters per second (w/sec).

Rounds the result.

'''


def speed_time(time_start, time_end, userinput):
    time_delay = time_end - time_start
    time_Roundoff = round(time_delay, 2)
    speed = len(userinput) / time_Roundoff
    return round(speed)



if __name__ == '__main__':  
    
    #Asks the user if they're ready to start.
    while True:
        check = input("Ready to begin: yes or no :")


        #Some Random lines to Test
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

        #Calculates Speed and Mistake

        


