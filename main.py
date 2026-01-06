print("Hello World")
def my_function(user_answer):
    if user_answer == 4:
        print("that is correct!")
    else:
        print("that is incorrect")

terminal_answer = int(input("what is 2 plus 2"))

my_function(terminal_answer)