import os
import requests

ideas = []
file_name = "ideas.txt"

# READ: Load existing ideas
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
    print("4. Get a random internet idea")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        new_idea = input("Type your hackathon idea: ")
        ideas.append(new_idea)
        with open(file_name, "a") as file:
            file.write(new_idea + "\n")
        print("Success! Idea saved permanently.")
        
    elif choice == '2':
        print("\n--- Your Ideas ---")
        if len(ideas) == 0:
            print("No ideas yet. Try adding one!")
        else:
            for index, idea in enumerate(ideas, 1):
                print(f"{index}. {idea}")
                
    elif choice == '3':
        print("\n--- Delete an Idea ---")
        if len(ideas) == 0:
            print("No ideas to delete.")
        else:
            for index, idea in enumerate(ideas, 1):
                print(f"{index}. {idea}")
            
            del_choice = input("Enter the number of the idea to delete: ")
            
            if del_choice.isdigit():
                del_index = int(del_choice) - 1 
                if 0 <= del_index < len(ideas):
                    deleted_idea = ideas.pop(del_index) 
                    
                    with open(file_name, "w") as file:
                        for idea in ideas:
                            file.write(idea + "\n")
                    print(f"Success! Deleted: '{deleted_idea}'")
                else:
                    print("Error: That number is not in the list.")
            else:
                print("Error: Please enter a valid number.")

    elif choice == '4':
        import random  # Python's built-in tool for random numbers
        
        print("\nFetching an idea from the cloud...")
        
        # Pick a random number between 1 and 100
        product_id = random.randint(1, 100)
        
        # Inject our random number into the API URL
        url = f"https://dummyjson.com/products/{product_id}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            random_idea = f"Build an AI-powered {data['title']}"
            print(f"💡 Suggestion: {random_idea}")
            
            save_choice = input("Do you want to save this idea? (y/n): ")
            
            if save_choice.lower() == 'y':
                ideas.append(random_idea)
                with open(file_name, "a") as file:
                    file.write(random_idea + "\n")
                print("Success! Internet idea saved to your list.")
        else:
            print(f"Error connecting to the API. Status code: {response.status_code}")
            print(f"Server response: {response.text}")
    elif choice == '5':
        print("Goodbye!")
        break
        
    else:
        print("Invalid choice. Please type 1, 2, 3, 4, or 5.")