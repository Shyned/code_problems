



from this import d


def happy_number(number):
    #digit holder
    digit_holder = []
    print(digit_holder)
  
    #append digit to list to seperate
    for digit in str(number):
        
        digit_holder.append(int(digit))
    return(digit_holder)



def square_rooter(number_list):
    squared_root_list = []
    print(squared_root_list)
    for number in number_list:
        squared_root_list.append((number)**2) 
    return squared_root_list



def happy_or_sad (sr_list):
    new_number = sum(sr_list)
    print(new_number)
    while True: 
        if new_number !=1:
            happy_or_sad(square_rooter(happy_number(new_number)))
        else:
            print(new_number)
            print("This is a happy number")
            quit()
       


happy_or_sad(square_rooter(happy_number(19)))