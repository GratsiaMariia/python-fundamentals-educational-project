def continue_or_exit(message_y_n):
    while True:
        choice = input(message_y_n + " Enter YES - if you want to continue, NO - if you want to go back to the beginning: ")
        if choice.lower() == 'yes':
            return True
        elif choice.lower() == 'no':
            return False
        else:
            print("Invalid input. Please type 'YES' or 'NO'.")