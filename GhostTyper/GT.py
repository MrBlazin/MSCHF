import os
import pyautogui
import time

Version = "1.1.0"

# Function to clear the terminal screen based on the operating system
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to create a folder to store payload files
def create_keystoke_payload_folder():
    if not os.path.exists('payload_folder'):
        os.makedirs('payload_folder')

# Main menu function to provide user options and handle their choice
def create_or_type_or_delete_or_view_payloads():
    clear_terminal()
    # Display the program title and menu
    print(f"""
     ▄▄█▀▀▀▄█  ▀██                       ▄   █▀▀██▀▀█
    ▄█▀     ▀   ██ ▄▄     ▄▄▄    ▄▄▄▄  ▄██▄     ██     ▄▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄    ▄▄▄▄  ▄▄▄ ▄▄
    ██    ▄▄▄▄  ██▀ ██  ▄█  ▀█▄ ██▄ ▀   ██      ██      ▀█▄  █   ██▀  ██ ▄█▄▄▄██  ██▀ ▀▀
    ▀█▄    ██   ██  ██  ██   ██ ▄ ▀█▄▄  ██      ██       ▀█▄█    ██    █ ██       ██
     ▀▀█▄▄▄▀█  ▄██▄ ██▄  ▀█▄▄█▀ █▀▄▄█▀  ▀█▄▀   ▄██▄       ▀█     ██▄▄▄▀   ▀█▄▄▄▀ ▄██▄
                                                       ▄▄ █      ██
        By: MrBlazin                                    ▀▀      ▀▀▀▀  {Version}
    """)
    print("==" * 50)
    print("\n ")
    print(" 1. Create  >> payloads to type.")
    print(" 2. Execute >> payloads and unleash the Ghost.")
    print(" 3. Delete  >> payloads and clean up unwanted payloads.")
    print(" 4. View    >> payloads and see what lies in them.")
    print(" 5. Exit    >> Definitely not a rick roll.")
    choice = input("\n  Enter your choice:\n >")
    if choice == '1':
        create_payload_file()
    elif choice == '2':
        execute_payload()
    elif choice == '3':
        delete_payload_file()
    elif choice == '4':
        view_payload_files()
    elif choice == '5':
        print(" Exiting the program...")
        exit()
    else:
        print(" Invalid choice. Please try again.")
        time.sleep(2)

# Function to create a payload file based on user choice
def create_payload_file():
    count = get_payload_count()

    options = [" 1. Keystroke Payload", "2. SPAMMING Payload"]  # To-do: Make More payloads

    print("\n Choose an option:")
    print("\n ".join(options))
    choice = input(" Enter your choice:\n >")

    if choice == '1':
        file_name = f'payload_folder/payload{count}.txt'
        create_keystoke_payload(file_name)
    elif choice == '2':
        create_spam_payload_file()
    # Add more payloads here - elif choice == '#':
    # Add more - functions() here
    else:
        print(" Invalid choice. Please choose '1' for Keystroke Payload or '2' for SPAM Payload.")

# Function to create a spam payload file
def create_spam_payload_file():
    user_input = input("\n Type the SPAM payload here and press ENTER to save:\n >")

    while True:
        try:
            SPAMnum = int(input("\n How many times do you want to SPAM the message?\n >"))
            break
        except ValueError:
            print(" Invalid input. Please enter a valid integer.")
    
    file_name = f'payload_folder/payload-SPAM-x{SPAMnum}.txt'
    with open(file_name, 'w') as file:
        file.write(f"{user_input}\n " * SPAMnum)

# Function to create a keystroke payload file
def create_keystoke_payload(file_name):
    with open(file_name, 'w') as file:
        print("\n Type the payloads. To save the payload, type '-save' in a new line:\n ")
        while True:
            user_input = input(' >')
            if user_input.strip().lower() == '-save':
                break
            file.write(user_input + '\n ')

        print("\n Payload saved in:", file_name)

# Function to get the count of existing payload files
def get_payload_count():
    SPAMnum = int
    count = 0
    while True:
        count += 1
        file_name = f'payload_folder/payload{count}.txt'
        file_name_s = f'payload_folder/payload-SPAM-x{SPAMnum}'
        if not os.path.exists(file_name) and not os.path.exists(file_name_s):
            break
    return count


# Function to delete a payload file
def delete_payload_file():
    files = [f for f in os.listdir('payload_folder') if f.startswith('payload')]

    if not files:
        print("\n  No payload file exists to delete.")
    else:
        print("\n  Select a payload file to delete:\n >")
        for i, file in enumerate(files, start=1):
            print(f" {i}. {file}")

        choice = int(input(" >"))
        if 1 <= choice <= len(files):
            selected_file = files[choice - 1]

            confirm = input(f" Are you sure you want to delete {selected_file}? (yes/no): ").lower()
            if confirm == 'yes':
                os.remove(f'payload_folder/{selected_file}')
                print(f" {selected_file} has been deleted.")
        else:
            print(" Invalid choice.")
        time.sleep(2)

# Function to display a countdown before starting ghosttyping
def countdown():
    print("\n  Starting ghost in:")
    for i in range(5, 0, -1):
        print(f" {i}")
        time.sleep(1)

def execute_payload():
    files = [f for f in os.listdir('payload_folder') if f.startswith('payload')]

    if not files:
        print("\n  No payload file exists.")
    else:
        print("\n  Available payload files:")
        for i, file in enumerate(files, 1):
            print(f" {i}. {file}")

        try:
            choice = int(input("\n  Enter the number of the payload you want to execute (e.g., 1):\n >"))
            if 1 <= choice <= len(files):
                chosen_file = files[choice - 1]
                with open(f'payload_folder/{chosen_file}', 'r') as file:
                    lines = file.readlines()

                    input("\n Press Enter to start ghosttyping...\n >")

                    countdown()

                    for i, line in enumerate(lines, start=1):
                        pyautogui.typewrite(line.strip())
                        pyautogui.press('enter')
                        print(
                            "Progress: [{}{}] {}%".format("=" * int(i / len(lines) * 20), " " * (20 - int(i / len(lines) * 20)),
                                                        int(i / len(lines) * 100)), end="\r")
                    else:
                        print("\n Press 'ENTER' to EXIT")
                    input()  # Wait for user to press enter
        except ValueError:
            print(" Invalid input. Please enter a valid file number.")

# Function to view the contents of payload files
def view_payload_files():
    files = [f for f in os.listdir('payload_folder') if f.startswith('payload')]

    if not files:
        print("\n  No payload file exists.")
    else:
        print("\n  Available payload files:")
        for i, file in enumerate(files, 1):
            print(f" {i}. {file}")

        try:
            choice = int(input("\n  Enter the number of the payload you want to view (e.g., 1):\n >"))
            if 1 <= choice <= len(files):
                chosen_file = files[choice - 1]
                print(f"\n  Contents of {chosen_file}:")
                with open(f'payload_folder/{chosen_file}', 'r') as file:
                    for line in file:
                        print("  " + line.strip())
            else:
                print("  Invalid choice. Please select a valid file number.")
        except ValueError:
            print(" Invalid input. Please enter a valid file number.")

            
        print("\n Press 'ENTER' to EXIT viewing mode")
        input()  # Wait for user to press enter
        
        # Loading bar
        print(" Exiting:")
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(1)

# Main entry point of the script
if __name__ == "__main__":
    create_keystoke_payload_folder()
    # Check if the script is running on Windows and start in a new Command Prompt if needed
    if os.name == 'nt' and os.environ.get('PROMPT') is None:
        print(" Starting in a new Command Prompt...")
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(1)
        os.system('start cmd /k python "' + os.path.abspath(__file__) + '"')
        exit()
    # Main loop for user interaction
    while True:
        create_or_type_or_delete_or_view_payloads()
