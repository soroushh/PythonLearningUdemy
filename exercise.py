def who_do_you_know():
    #Ask the user for the list of people they know.
    #Split the string the the list.
    #Return that list
    return(input("Please enter the names of people you know with spaces between them").split(" "))

def ask_user():
    # Ask user for a name
    #print if they know it or not
    second_name = input("Please enter the second name")
    return( second_name in who_do_you_know())

print(ask_user())
