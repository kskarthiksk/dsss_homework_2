import random


def random_number(min: int, max: int):
    """Returns a random integer in range [min, max] including both end points

    Args:
        min (int): lower bound for output
        max (int): upper bound for output

    Returns:
        int: an integer between min and max, both included
    """
    return random.randint(min, max)


def choose_operation():
    """Chooses randomly between 3 mathematical operations +, - or *

    Returns:
        str: Returns either +, - or * as a single character string
    """
    return random.choice(['+', '-', '*'])


def format_problem(num1: int, num2: int, operation: str):
    """Formats the problem as a string

    Args:
        num1 (int): first number
        num2 (int): second number
        operation (str): desired operation ( +, - or * )

    Returns:
        str: a string describing the operation
        
    """
    problem = f"{num1} {operation} {num2}"

    return problem

def calculation(num1: int, num2: int, operation: str) -> int:
    """calculates the answer to the operation (sum, difference or product of two numbers)

    Args:
        num1 (int): first number
        num2 (int): second number
        operation (str): desired operation ( +, - or * )

    Returns:
        int: the solution of the operation
    """
    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    
    return answer

def math_quiz():
    """Function that performs the math quiz. Asks the user some questions, checks the answer and calculates the score
    """
    score = 0           # initializing score
    num_questions = 3   # number of questions to ask the user

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(num_questions):
        num1 = random_number(1, 10)     # select a random number from 1 to 10
        num2 = random_number(1, 5)      # select a random number from 1 to 5
        operation = choose_operation()  # choose the operation to perform

        problem = format_problem(num1, num2, operation)     # formats the problem as a string
        answer = calculation(num1, num2, operation)         # calculates the solution to the problem

        print(f"\nQuestion: {problem}")                 # prints the problem for the user

        try:
            user_answer = int(input("Your answer: "))  # takes the answer from the user

            if user_answer == answer:                   # checks if the answer is correct and rewards a point if it is
                print("Correct! You earned a point.")
                score += 1
            else:                                       # prints the correct answer if the user inputs a wrong answer
                print(f"Wrong answer. The correct answer is {answer}.")

        except ValueError:                              # executed if user input is not an integer
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{num_questions}")   # printing the final score

if __name__ == "__main__":
    math_quiz()
