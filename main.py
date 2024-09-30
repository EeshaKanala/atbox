print("Welcome to the Elite 101 Chatbox!")
userName = input("Please enter your name: ")
userAge = input("Nice to meet you " + userName + "! How old are you? ")
print("Welcome " + userName + "! Oh, to be " + userAge + " again! How can I help you today?")

def display_menu():
    print("Please choose from the following options:")
    print("1. Placeholder Option 1")
    print("2. Placeholder Option 2")
    print("3. Placeholder Option 3")
    print("4. Exit the conversation")

def user_selection():
    user_choice = int(input("Enter the number of your choice: "))
    if user_choice == 4:
        print("Goodbye," + userName + "! Have a great day!")

display_menu()
user_selection()