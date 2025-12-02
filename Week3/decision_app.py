# decision_app.py
# A very simple decision making program using if/else and a loop.
#Author: Brylan Williamson
print("Welcome to the Simple Decision Assistant!")
print("Are you ready to answer some questions?")
if input("Type 'yes' to continue or 'no' to exit: ").lower() != "yes": 
    print("Goodbye! Have a nice day!" if input("Are you feeling smelly? ").lower() != "yes" else "goodbye smelly, have a smelly day!")
    exit()
# The loop will keep running until the user decides to exit
while True:
    print("\nPlease answer the following questions with 'yes' or 'no'.")

    # Ask a few Yes/No questions
    tired = input("Are you feeling tired? ").lower()
    if tired == "yes":
        print("You should take a short nap or get some rest.")
    elif tired == "no":
        print("That's good to hear!")
    hungry = input("Are you feeling hungry? ").lower()
    if hungry == "yes":
        print("You should eat something healthy!")
    elif hungry == "no":
        print("Well good for you!")
    bored = input("Are you feeling bored? ").lower()
    if bored == "yes":
        print("Maybe try doing something fun or creative.")
    elif bored == "no":
        print("I guess you are busy with my program then!")
    silly = input("Are you feeling silly? ").lower()
    if silly == "yes":
        print("How about playing a fun game or telling jokes?")
    elif silly == "no":
        print("oh fine then be boring I dont care anyway boring ahh")
    smelly = input("Are you feeling smelly? ").lower()
    if smelly == "yes":
        print("then go take a shower instead of making everyone smell you!")
    elif smelly == "no":
        print("good, thats how it should be!")
    # Use if/elif/else statements to make decisions
    else:
        # If none of the conditions are met, provide a general message
        print("You seem to be doing great! Keep it up!")
    # Ask if the user wants to try again
    again = input("\nWould you like to answer again? (yes/no): ").lower()
    if again != "yes":
        #do it again
     if again == "no":
        # Exit the loop and end the program

        print("Goodbye! Have a nice day!")
    if smelly == "yes":
        print(input("goodbye smelly have a smelly day!"))
        break  # exits the loop
    if again == "no":
        break  # exits the loop
