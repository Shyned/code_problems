#2. Prime Numbers
#a. A prime number is a number that is only divisible by one and itself.
#b. Write a method that prints out all prime numbers between 1 and 100


def prime_numbers_checker(number):
    # split into range in have to divide by
    first_half_range=range(1,number)
    second_half_range=range(number,101)
    joined_ranges=[]
    divisble=[]
    
    for first_half_digit in first_half_range:
        joined_ranges.append(first_half_digit)
    
    for second_half_digit in second_half_range:
        joined_ranges.append(second_half_digit)
        
    for joined_number in joined_ranges:
        if number%joined_number==0:
            divisble.append(joined_number)
            
        
        else:
            pass
    
    
    if len(divisble)>2:
        print("Not a prime number!")
        
    else:
        print("Prime number")