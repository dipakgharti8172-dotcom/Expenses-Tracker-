# Expenses tracker
import json

database = {}

# read file
def read_file_func():
    global database
    try:
        with open("Expenses.json", "r") as f:
            database = json.load(f)
    except FileNotFoundError:
      database = {}
            print("No data found.")
            
# update file
def update_file_func():
    with open("Expenses.json", "w") as fw:
        json.dump(database, fw)



# ask again function                
def ask_again_func():
            while True:
                ask_again = input("Want to continue (yes/no): ").lower().strip()
                if ask_again in ("yes", "no"):
                    return ask_again
                else:
                    print("Yes and no option allowed only.")



# add function

def add_func():
    while True:
        print()
        expenses_type = input("Expenses Type: ").title().strip()
        while True:
            try:
                expenses_amount = float(input("Amount: "))
                database[expenses_type] = {"Amount": expenses_amount}
                update_file_func()
            except ValueError:
                print("Amount should be number.")
                continue
            break
            
            
        # ask again function
        again = ask_again_func()
        if again == "yes":
            continue
        else:
            print("Expenses saved to file successfully.")
            break
            
# update function            
            
def update_func():
    while True:
        print()
        if len(database) == 0:
            print("No expenses added yet")
            break
        else:
            print("Available Expenses:")
            view = view_all_func()
            print()
            select_expenses = input("Select Expenses Type: ").title().strip()

            if select_expenses in database:
                update_expenses = input("Updated Expenses Type: ").title().strip()
            
                while True:
                    try:
                        update_expenses_amount = float(input("Updated amount: "))
                        break
                    except ValueError:
                        print("Amount should be number only.")
                        continue

            # delete old one
                if select_expenses != update_expenses:
                    del database[select_expenses]
            
                database[update_expenses] = {"Amount": update_expenses_amount}
                update_file_func()
                print(f"{select_expenses} successfully updated to {update_expenses}, amount to {update_expenses_amount}")

                answer = ask_again_func()
                if answer == "yes":
                    continue
                else:
                    print("Updated expenses save to file successfully.")
                    break
            else:
                print(f"No {select_expenses} expenses found in database.")

                        
# delete function
def delete_func():
            while True:
                print()
                if len(database) == 0:
                    print()
                    print("No expenses added yet.")
                    break
                else:
                    delete_expenses = input("Delete expenses type: ").title().strip()
                    if delete_expenses in database:
                        del database[delete_expenses]
                        print(f" {delete_expenses} successfully deleted")
                        update_file_func()
                    else:
                        print()
                        print(f"{delete_expenses} not found in database.")
                        
                    # ask again conditon   
                    again = ask_again_func()
                    if again == "yes":
                        continue
                    else:
                        break

                        
                                                                        
# view expenses function
def view_all_func():
    print()
    if len(database) != 0: # check database empty or not
        # view all value with counting numbers
        for index, value in enumerate(database, 1):
            print(f"{index}. Type: {value}, Amount:",database[value]["Amount"])
    else:
        print("No expenses added yet.")

            
read_file_func() # load data before running programs                                    
while True:   
    print()
    # our services option
    print("1. Add Expenses")
    print("2. Update Expenses")
    print("3. Delete Expenses")
    print("4. View All Expenses")
    print("5. Exit")
    print()
    #  Ask user to enter value
    user_choice = input("Select an option: ").lower().strip() 
     # i create a variable and store all checkable value.    
    add = ["1","add","add expenses"]
    update = ["2", "update", "update expenses"]
    delete = ["3", "delete", "delete expenses"]
    view = ["4", "view", "view all", "all", "all expenses", "view all expenses"]
    exit = ["5", "exit"]
    
    # add condition
    if user_choice in add:
        print(" 1. Add Expenses")
        add_func() # call add function
        
    # update condition
    elif user_choice in update:
        print("2. Update Expenses")
        update_func()  # call update function
       
    # delete condition
    elif user_choice in delete:
        print("3. Delete Expenses")
        delete_func()  # call delete function
        
    # view condition
    elif user_choice in view:
        print("4. View All Expenses")
        view_all_func() #call view all function
    
    # exit condition
    elif user_choice in exit:
        print("Successfully exit thanks for using our service.")
        break
     
     # condition if user enter space
    elif user_choice == "":
        print("Space isn't  allowed.")
        continue
        
    # if user makes mistake this condition run 
    else:
        print("Something went wrong! try again?")
        continue
        
        
        
    
