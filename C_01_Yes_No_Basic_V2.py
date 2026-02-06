# Functions

def yes_no(question):

    """ Checks user response is yes/no  (y/n) returns 'yes' or 'no' """

    while True:

        # Asks if user would like to see instructions
        response = input(question).lower()

        # Checks response
        if response == "y" or response == "yes":
            return "yes"
        elif response == "n" or response == "no":
            return "no"
        else:
            print("Please enter yes or no.")

# Main Routine

want_instructions = yes_no("Would you like to see the instructions? (y/n) \n").lower()
want_coffee = yes_no("Would you like some coffe? (y/n) \n")

print("We are done")