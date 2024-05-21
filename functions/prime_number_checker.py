def prime_number_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print(f"{number} is a prime number.")

    else:
        print(f"{number} is not a prime number.")
checker_another_number = True
while checker_another_number:
    print("welcome to my prime number checker program.\n")
    number = int(input("Please enter a number to check if it is prime : \n"))
    prime_number_checker(number)

    check_again = input("Do you want to check another number? \n").lower()
    answer = True
    while answer:
        if check_again == "no":
            print("Thank you!")
            answer = False
            checker_another_number = False
        elif check_again == "yes":
            answer = False
        else:
            check_again= input("I am yet to receive the correct instruction from you. Please enter 'Yes' or 'No': \n").lower()
