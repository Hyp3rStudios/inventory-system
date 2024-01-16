# -----------------------
# INVENTORY SYSTEM
# a simple system with an inventory. feel free to use in games.
# -----------------------

import os # import os for clearing screen

os.system('cls') # For windows
# For mac: os.system('clear')

inventory = [] # declare a blank list

def add(item): # make an "add" function, "item" is a variable
    inventory.append(item) # add the item to the inventory

def remove(item): # make a "remove" function, "item" is a variable
    inventory.remove(item) # remove the item from the inventory

def list(): # make a "list" function
    print(inventory) # print the list

running = True # make a "running" variable so that the user can exit

while running == True: # make a loop, can also be written as "while running", because it's already true
    action = input("Enter action (add, remove, list, or exit): ").lower() # ask the user, then make it lowercase
    
    if action == "add": # check if the action is "add"
        add_item = input("Enter item to add: ") # get user input
        add(add_item) # use our add function
        print(f"Added: {add_item}") # show that the item was added

    elif action == "remove": # check if the action is "remove"
        remove_item = input("Enter item to remove: ")
        remove(remove_item)
        print(f"Removed: {remove_item}") # show that the item was removed

    elif action == "list": # check if the action is "list"
        list() # list the inventory

    elif action == "exit": # check if the action is "exit"
        print("Exiting... ")
        running = False # set running to false
        break # exit the loop (and the program)

    else: # check if it's anything else
        print("That's not a valid action.") # tell the user
    