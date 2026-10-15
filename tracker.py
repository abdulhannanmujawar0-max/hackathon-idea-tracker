import os

ideas = []
file_name = "ideas.txt"

# READ: Load ideas if the file exists
if os.path.exists(file_name):
    with open(file_name, "r") as file:
        for line in file:
            ideas.append(line.strip())

print("Welcome to the Hackathon Idea Tracker!")

while True:
    print("\n--- Main Menu ---")
    print("1. Add a new idea")
    print("2. View all ideas")
    print("3. Delete an idea")
    print("4. Exit")
    
    choice = input("Enter your choice (1, 2, 3, or 4): ")
    
    if choice == '1':
        new_idea = input("Type your hackathon idea: ")
        ideas.append(new_idea)
        
        # APPEND: Add to the bottom of the file
        with open(file_name, "a") as file:
            file.write(new_idea + "\n")
            
        print("Success! Idea saved permanently.")
        
    elif choice == '2':
        print("\n--- Your Ideas ---")
        if len(ideas) == 0:
            print("No ideas yet. Try adding one!")
        else:
            # enumerate() automatically numbers our list starting from 1
            for index, idea in enumerate(ideas, 1):
                print(f"{index}. {idea}")
                
    elif choice == '3':
        print("\n--- Delete an Idea ---")
        if len(ideas) == 0:
            print("No ideas to delete.")
        else:
            # Show the numbered list again
            for index, idea in enumerate(ideas, 1):
                print(f"{index}. {idea}")
            
            # Get the number to delete
            del_choice = input("Enter the number of the idea to delete: ")
            
            # .isdigit() checks if the user actually typed a number instead of letters
            if del_choice.isdigit():
                # Subtract 1 because Python lists start counting at 0, not 1
                del_index = int(del_choice) - 1 
                
                # Check if the number they typed is actually in our list
                if 0 <= del_index < len(ideas):
                    # .pop() removes the item and returns it so we know what was deleted
                    deleted_idea = ideas.pop(del_index) 
                    
                    # WRITE: "w" mode completely erases the file and writes our new list
                    with open(file_name, "w") as file:
                        for idea in ideas:
                            file.write(idea + "\n")
                            
                    print(f"Success! Deleted: '{deleted_idea}'")
                else:
                    print("Error: That number is not in the list.")
            else:
                print("Error: Please enter a valid number.")

    elif choice == '4':
        print("Goodbye!")
        break
        
    else:
        print("Invalid choice. Please type 1, 2, 3, or 4.")