import os
import ExampleClass

#basic menu
def main_menu():
    print("Press 1 for list of files in folder")
    print("Press 2 for copying the files into a new folder")
    print("Press 3 to delete coppied files from new folder")
    print("Press 4 to quit")
    
#introduction
print("Refresher/Example Python demonstration.")
print()

#state the current working directory is
print("Current working directory is: " + os.getcwd())
print()

#main loop
while True:

    #get user input
    while True:
        try:
            main_menu()
            answer = int(input())
        except ValueError:
            print()
            print("Invalid input. Try again.")
            continue

        if answer < 0 or answer > 4:
            print()
            print("Invalid input. Try again.")
            continue
        else:
            break

    #create class
    ec = ExampleClass.MyClass(os.getcwd())

    if answer == 1:
        print(ec.get_files())
    elif answer == 2:
        ec.copy_and_move_files("\\Copy Folder")
    elif answer == 3:
        ec.delete_copied_files("\\Copy Folder")
    elif answer == 4:
        quit()

    #spacing
    print()

    #ask user if want to run again
    print("Run another operation? y for yes or n for no")
    run = input()

    #test response
    if run == "y":
        continue
    else:
        quit()