#!/usr/bin/env python3
# ============================================================================
# GitHub Profile Analyzer - A Learning Project for Beginner AI Engineers
# ============================================================================
# This script demonstrates how to interact with the GitHub API, handle user
# input, make HTTP requests, and work with JSON data - all essential skills
# for a global AI engineer!
# ============================================================================

# Import the 'requests' library - this lets us make HTTP calls to APIs
# Think of it like opening a web browser and requesting a webpage, but
# programmatically (through code instead of clicking).
import requests

# Import 'sys' which provides access to system-specific functions.
# We'll use this to exit the program gracefully if something goes wrong.
import sys


def get_github_repos(username):
    """
    This is a function (a reusable block of code) that takes a GitHub username
    as input and returns the number of public repositories.
    
    Parameters:
        username (str): The GitHub username to look up
    
    Returns:
        int or None: Number of public repos, or None if user not found
    """
    
    # Construct the GitHub API URL. GitHub's API is located at:
    # https://api.github.com/users/{username}
    # This URL follows a standard pattern called REST (Representational State Transfer)
    # The {username} placeholder will be replaced with the actual username we get
    api_url = f"https://api.github.com/users/{username}"
    
    # Try to make the HTTP GET request (like visiting the URL in a browser)
    try:
        # The 'requests.get()' function sends an HTTP GET request to the URL
        # This returns a 'Response' object containing the data from GitHub
        response = requests.get(api_url)
        
        # Check if the HTTP request was successful
        # Status code 200 means "OK" - the request worked!
        # Other codes like 404 mean "Not Found"
        if response.status_code == 200:
            # response.json() converts the JSON data GitHub sent us into a Python dictionary
            # A dictionary is like a real-world dictionary: you look up a key and get a value
            user_data = response.json()
            
            # Access the 'public_repos' key from the dictionary
            # This gives us the number of public repositories the user has
            public_repos = user_data['public_repos']
            
            # Return this number so the caller can use it
            return public_repos
        
        # If status code is 404, the user doesn't exist on GitHub
        elif response.status_code == 404:
            # Print a friendly error message
            print(f"❌ User '{username}' not found on GitHub.")
            # Return None (Python's way of saying "no value")
            return None
        
        # For any other status code (500, 403, etc.), something else went wrong
        else:
            print(f"❌ Error: GitHub returned status code {response.status_code}")
            return None
    
    # If the request fails entirely (no internet, GitHub is down, etc.)
    except requests.exceptions.RequestException as error:
        # 'except' catches errors. 'RequestException' is the error type for network issues
        # 'as error' captures the error so we can print it
        print(f"❌ Network error: {error}")
        return None


def main():
    """
    This is the main function - the entry point of our program.
    It orchestrates (directs) the overall flow of the application.
    """
    
    # Print a welcome message to the user
    print("\n" + "="*60)
    print("🚀 Welcome to the GitHub Profile Analyzer!")
    print("="*60)
    print("This tool analyzes public GitHub profiles and shows you")
    print("how many public repositories a developer has.\n")
    
    # Loop forever (until we break out with 'exit' or error)
    # This lets users check multiple GitHub profiles without restarting
    while True:
        # Get the GitHub username from the user using input()
        # input() displays a prompt and waits for the user to type something
        # The .strip() method removes extra spaces from the beginning and end
        username = input("Enter a GitHub username (or 'quit' to exit): ").strip()
        
        # Check if the user typed 'quit' to exit the program
        if username.lower() == 'quit':
            # Print a goodbye message
            print("\n👋 Thanks for using GitHub Profile Analyzer!")
            # sys.exit(0) terminates the program. 0 means "exited successfully"
            sys.exit(0)
        
        # Check if the username is empty (user just pressed Enter)
        if not username:
            # 'not username' checks if the string is empty
            # If it is, print an error and continue to next loop iteration
            print("⚠️  Please enter a valid username.\n")
            # continue skips the rest of this loop and goes to the next iteration
            continue
        
        # Call our function to get the number of public repos
        # This sends the request to GitHub and gets the count
        public_repos = get_github_repos(username)
        
        # Check if we got a valid result
        # If public_repos is None, it means an error occurred
        if public_repos is not None:
            # public_repos is a number, so we successfully found the user!
            # Format and print the result with an emoji for visual appeal
            print(f"\n🔥 BOOM! {username} is a builder with {public_repos} repos!")
            print("-" * 60 + "\n")


# This is the entry point of the script
# It means "if this file is run directly (not imported), run the main() function"
# Without this, the script would run immediately if imported by another file
if __name__ == "__main__":
    # Call the main function to start the program
    main()
