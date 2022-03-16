#Capitalize letter
#a. Write code that takes a string as input and capitalize the first letter of each word. Words
#will be separated by only one space. i.e. “hello world” should be outputted as “Hello
#World”

def capitalize_letter ():
    test = "hello world"
    test_list = []
    seperated_test = test.split()

    for words in seperated_test:
        capped_word = words.capitalize()
        test_list.append(capped_word)

        
    print(" ".join(test_list))

capitalize_letter()