import datetime

# ANSI escape codes for colors
colors = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "reset": "\033[0m"
}

# Define users with their chosen colors
users = {
    "Nadeem": "green",
    "Ali": "blue",
    "Sara": "magenta"
    # Add more users here as needed
}

# File to store conversation log
log_file = "multi_user_conversation_log.txt"

def log_conversation():
    while True:
        # Display available users
        print("\nAvailable users:")
        for user in users:
            print(f"{user} ({users[user]})")
        
        # Prompt for username and check if it exists
        username = input("\nEnter username (or type 'exit' to quit): ")
        if username.lower() == "exit":
            print("Conversation logging stopped.")
            break
        
        if username not in users:
            print("User not found. Please try again.")
            continue

        # Get user's color
        user_color = colors[users[username]]

        # Prompt for conversation text
        user_input = input(f"{user_color}{username}: {colors['reset']}")
        
        # Stop logging if user enters "exit"
        if user_input.lower() == "exit":
            print("Conversation logging stopped.")
            break

        # Get current timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Format log entry
        log_entry = f"[{timestamp}] {username}: {user_input}\n"

        # Save to file
        with open(log_file, "a") as file:
            file.write(log_entry)

        # Print to terminal with color
        print(f"{user_color}{log_entry}{colors['reset']}")

if __name__ == "__main__":
    log_conversation()
