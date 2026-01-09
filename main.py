print("Welcome to this quiz") #start of the quiz
print("You are going to be given a set of questions, for each one answer with the value you think is correct")
print("good luck")

#question 1
def my_function(user_answer): #if functions to determine if answer is correct
    if user_answer == 4:
        print("that is correct!")
    else:
        print("that is incorrect")

terminal_answer = int(input("what is 2 plus 2"))

my_function(terminal_answer)

#creating fucntion to calculate total marks at end of quiz

if my_function == "that is correct!":
    terminal_answer = 1

#question 2
def my_function2(user_answers):
    if user_answers == 10:
        print("correct")
    else:
        print("incorrect")

terminal_answer = int(input("what is 5 multiplied by 2?"))
my_function2(terminal_answer)

#question 3
def my_function3(user_answers):
    if user_answers == 81:
        print("correct")
    else:
        print("incorrect")

terminal_answer = int(input("what is 9 squared?"))
my_function3(terminal_answer)

#end of quiz
print ("well done thank you for taking this quiz")