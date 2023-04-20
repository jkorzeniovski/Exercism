import operator

def is_armstrong(num_to_check, numbers_tab):
    endnumber = 0
    for i in range(len(numbers_tab)):
        endnumber = endnumber + pow(int(numbers_tab[i]), len(numbers_tab))
    if endnumber == int(num_to_check):
        print(num_to_check, "is an Armstrong number")
    else:
        print(num_to_check, "is not an Armstrong number")


num_to_check = input("Enter a number to check: ")
numbers_tab = list(num_to_check)

is_armstrong(num_to_check, numbers_tab)