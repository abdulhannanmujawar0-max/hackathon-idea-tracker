import requests

# 1. Get a username from the user
username = input("Enter a GitHub username (e.g., octocat, torvalds): ")

# 2. Build the exact API URL for that user using an f-string
url = f"https://api.github.com/users/{username}"

print(f"\nContacting GitHub at: {url} ...\n")

# 3. Make the GET request
response = requests.get(url)

# 4. Check the status code
if response.status_code == 200:
    # 200 means success. Convert the JSON into a Python dictionary
    user_data = response.json()
    
    print("--- Profile Found ---")
    # We use .get() here to prevent errors if a user doesn't have a name or bio set
    print("Name: " + str(user_data.get('name')))
    print("Bio: " + str(user_data.get('bio')))
    print("Public Repos: " + str(user_data.get('public_repos')))
    print("Followers: " + str(user_data.get('followers')))
    
elif response.status_code == 404:
    # 404 specifically means "Not Found"
    print(f"Error: The username '{username}' does not exist on GitHub.")
    
else:
    # Catch any other errors (like 500 Server Error)
    print(f"Failed! The server responded with status code: {response.status_code}")