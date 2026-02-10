while True:
    # Asks if user would like to see instructions
    want_instructions = input("Would you like to see the instructions? (y/n) \n").lower()

    # Checks response
    if want_instructions == "y" or want_instructions == "yes":
        print("You said yes.")
        break
    elif want_instructions == "n" or want_instructions == "no":
        print("You said no.")
        break
    else:
        print("Please enter yes or no.")
        continue

print("We are done")