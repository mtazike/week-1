#Assignment1
def palindrome(word):                       # define a function
    new_word = word.lower()                 # make everything lowercase
    new_word = new_word.replace(" ", "")    # remove spaces
    reversed_word = new_word[::-1]          # reverse the string
    return new_word == reversed_word        # compare forward and backward


user_input = input ("type a word or phrase: ")    # ask user to type something
result = palindrome(user_input)                   # chack if it's a palindrome

if result:                                        # if result == True
    print("Yes! that's apalindrome!")
else:
    print("Nope, not a palindrome.")




#Assignment2
def parentheses(sequence):                       # define a function
    counter = 0                                  # start counter at 0

    for character in sequence:                   # look at each character in the string one by one
        if character == "(":                     # if the character is opening parenthesis
            counter += 1                         # add 1 to the counter
        elif character == ")":                   # if the character is closing parenthesis
            counter -= 1                         # subtract 1 from the counter

            if counter < 0:                      # if counter goes below 0
                return False                     # too many closing ")" so not balanced
            


    return counter == 0                          # True is balanced, False if not


    
print(parentheses("((blah)())"))                 # True
print(parentheses("(((())blee))"))               # True
print(parentheses("((hello(())))"))              # True
print(parentheses("((((((())"))                  # False
print(parentheses("())"))                        # False