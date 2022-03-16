#BONUS CHALLENGE: Palindrome
#a. A word, phrase, or sequence that reads the same backward as forward i.e. madam
#b. Write code that takes a user input and checks to see if it is a Palindrome and reports the
#result

def pal_in_drome():
    user_phase = input("Please enter a phase or string: ")
    if user_phase == user_phase[::-1]:
        print("This is a Palindrome congrats.")
        
    else:
        print("Sorry, not a palindrome.")
        
        
pal_in_drome()