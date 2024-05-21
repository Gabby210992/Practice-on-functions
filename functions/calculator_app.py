from calculator_logo import calc_logo
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return  n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations ={"+": add, 
             "-": subtract, 
             "*": multiply, 
             "/": divide
            }
def calculator():
    print(calc_logo)
    num1 = float(input("What's the first number: "))
    perform = False
    while not perform:
        for operation in operations:
            print(operation)
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        should_continue = input(f"type 'y' to continue with {answer} and 'n' to exit: ")
        correct_input = False
        while not correct_input:
            if should_continue == "n":
                correct_input = True
                perform = True
            elif should_continue == "y":
                correct_input = True
                num1 = answer
            else:
                answer = input("you have not entered the correct input. Please enter 'y' or 'n': ")
                should_continue = answer

        begin_again = input("Press 't' to start all over: ")
        if begin_again == 't':
            calculator()

calculator()
            

    