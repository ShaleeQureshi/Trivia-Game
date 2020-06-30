from api_req import getQuestion, getAnswer
import os


def playAgain():
    print("--------------------------------------------------------------------------------")
    play = input("Would you like to play again? (y, N)\n")
    print("--------------------------------------------------------------------------------")
    if play == 'y' or play == 'Y':
        promptwithQ()
    else:
        end()

def end():
    print("--------------------------------------------------------------------------------")
    print("Thank you for playing")
    print("--------------------------------------------------------------------------------")
    print("View more of my software at squreshi.net/software or on github.com/ShaleeQureshi")
    print("--------------------------------------------------------------------------------")
    exit()

def intro():
    print("--------------------------------------------------------------------------------")
    print("View more of my software at squreshi.net/software or on github.com/ShaleeQureshi")
    print("--------------------------------------------------------------------------------")
    print("Welcome to Shahrukh Qureshi's Trivia Game")
    print("--------------------------------------------------------------------------------")

    print("Lets get started!")
    promptwithQ()

def promptwithQ():
    print("--------------------------------------------------------------------------------")
    print(getQuestion())
    print("--------------------------------------------------------------------------------")
    answer = input("You answer (True or False)\n")
    checkAns(answer)

def checkAns(userinput):
    correctAns = getAnswer()
    if userinput == correctAns:
        print("--------------------------------------------------------------------------------")
        print("CORRECT!")
        playAgain()
    else:
        print("--------------------------------------------------------------------------------")
        print("You lost the 50 / 50, the correct answer was " + correctAns)
        playAgain()

# Calling the intro function to run the program
intro() 