import requests
import sqlite3
import random

print("Welcome to the Hackathon Idea Tracker (Database Edition)!")

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
        
        # 1. Connect to DB
        conn = sqlite3.connect("ideas.db")
        cursor = conn.cursor()
        
        # 2. Execute SQL INSERT
        cursor.execute("INSERT INTO hackathon_ideas (title) VALUES (?)", (new_idea,))
        
        # 3. Save and close
        conn.commit()
        conn.close()
        print("Success! Idea saved to the database.")
        
    elif choice == '2':
        print("\n--- Your Database Ideas ---")
        conn = sqlite3.connect("ideas.db")
        cursor = conn.cursor()
        
        # SQL SELECT to grab all rows
        cursor.execute("SELECT id, title, status FROM hackathon_ideas")
        rows = cursor.fetchall() 
        conn.close()
        
        if len(rows) == 0:
            print("No ideas yet. Try adding one!")
        else:
            for row in rows:
                # row[0] is ID, row[1] is title, row[2] is status
                print(f"ID {row[0]}: {row[1]} (Status: {row[2]})")
                
    elif choice == '3':
        del_id = input("Enter the EXACT ID number of the idea to delete: ")
        
        if del_id.isdigit():
            conn = sqlite3.connect("ideas.db")
            cursor = conn.cursor()
            
            # SQL DELETE
            cursor.execute("DELETE FROM hackathon_ideas WHERE id = ?", (int(del_id),))
            conn.commit()
            
            if cursor.rowcount > 0:
                print(f"Success! Idea ID {del_id} deleted.")
            else:
                print("Error: That ID does not exist.")
            conn.close()
        else:
            print("Error: Please enter a valid number.")

    elif choice == '4':
        print("\nFetching an idea from the cloud...")
        product_id = random.randint(1, 100)
        response = requests.get(f"https://dummyjson.com/products/{product_id}")
        
        if response.status_code == 200:
            data = response.json()
            random_idea = f"Build an AI-powered {data['title']}"
            print(f"💡 Suggestion: {random_idea}")
            
            save_choice = input("Do you want to save this idea? (y/n): ")
            if save_choice.lower() == 'y':
                conn = sqlite3.connect("ideas.db")
                cursor = conn.cursor()
                cursor.execute("INSERT INTO hackathon_ideas (title) VALUES (?)", (random_idea,))
                conn.commit()
                conn.close()
                print("Success! Internet idea saved to the database.")
        else:
            print(f"Error connecting to the API. Status code: {response.status_code}")

    elif choice == '5':
        print("Goodbye!")
        break
        
    else:
        print("Invalid choice. Please type 1, 2, 3, 4, or 5.")