#Write a script that takes input of a users password and determine if it is secure by checking multiple requirements

#First requirement: must be atleast 12 characters
def length (password):
    length = False
    x = len(password)
    if x < 12:
        print ("Password is not long enough.  Please Try again!")
    else:
        length = True

#Second Requirement; must contain atleast one number
def number (password):
    number = False
    for a in range(len(password)):
        index = password[a]
        if index.isdigit():
            number = True
    if number == False:
        print("Password does not contain a number.  Please try again!")
        
#Third requirement; must contain atleast one special character
def spec_char (password):
    spec_char = False
    special_chars ="!@$%^&*()-+?_=,<>/"
    for a in range(len(password)):
        index = password[a]
        for b in range(len(special_chars)):
            special_index = special_chars[b]
            if index == special_index:
                spec_char = True
    if spec_char == False:
        print("Password does not contain a special character.  Please Try again!")


success = False

while(success == False):
    password = input(str("Please enter a password: "))

    length(password)
    number(password)
    spec_char(password)
   
    print ("You have successfully created a secure password!")
    