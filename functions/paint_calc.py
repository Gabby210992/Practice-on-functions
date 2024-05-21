import math
def paint_calc(height, lenght23):
    area = print(f"You have {height * lenght}sqcm to paint \n")
    no_of_cans = math.ceil((height * lenght)/ 2) 
    print(f"You have to buy {no_of_cans}.")

height = int(input("Enter the height of your building: \n"))
lenght = int(input("Enter the length of your building: \n"))

paint_calc(height, lenght)