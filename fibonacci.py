
from re import L



def fibonacci_separator(number):
    #split into separate parts
    digit_holder = []
    last_number =number
    #append digit to list to seperate
    for digit in str(number):
        digit_holder.append(int(digit))
    #the list with each digit 
    return(digit_holder)
    


def last_digit_adder(number_list):
    last_int = number_list[-1]
    sum_of_numbers= last_int

    
    while True:
        last_digit_adder(fibonacci_separator(sum_of_numbers))




last_digit_adder(fibonacci_separator(1))       