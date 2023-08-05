import os
import pyautogui
import time

def clear_terminal():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux and macOS
        os.system('clear')

def create_payload_folder():
    if not os.path.exists('payload_folder'):
        os.makedirs('payload_folder')

def create_or_type_or_delete_payloads():
    print(" \nGhost Typer:")
    print(" 1. Create payload")
    print(" 2. Execute payload")
    print(" 3. Delete payload")
    choice = input("\nEnter your choice: ")
    if choice == '1':
        create_payload_file()
    elif choice == '2':
        type_payloads_from_file()
    elif choice == '3':
        delete_payload_file()
    else:
        print(" Invalid choice. Please try again.")
        time.sleep(2)

def create_payload_file():
    count = 0
    while True:
        count += 1
        file_name = f'payload_folder/payload.txt' if count == 1 else f'payload_folder/payload{count}.txt'
        if not os.path.exists(file_name):
            break

    with open(file_name, 'w') as file:
        print(" \nType the payloads. To save the payload, type 'save' in a new line:")
        while True:
            user_input = input()
            if user_input.strip().lower() == 'save':
                break
            file.write(user_input + '\n')

def type_payloads_from_file():
    files = [f for f in os.listdir('payload_folder') if f.startswith('payload')]
    if not files:
        print(" \nNo payload.txt file exists. Creating a new one...")
        create_payload_file()
    else:
        print(" \nSelect a payload.txt file to type from:")
        for i, file in enumerate(files, start=1):
            print(f"{i}. {file}")

        choice = int(input())
        if 1 <= choice <= len(files):
            selected_file = files[choice - 1]

            with open(f'payload_folder/{selected_file}', 'r') as file:
                lines = file.readlines()

            countdown()
            for line in lines:
                pyautogui.typewrite(line.strip())
                pyautogui.press('enter')
        else:
            print(" Invalid choice.")
        time.sleep(2)

def delete_payload_file():
    files = [f for f in os.listdir('payload_folder') if f.startswith('payload')]
    if not files:
        print(" \nNo payload.txt file exists to delete.")
    else:
        print(" \nSelect a payload.txt file to delete:")
        for i, file in enumerate(files, start=1):
            print(f"{i}. {file}")

        choice = int(input())
        if 1 <= choice <= len(files):
            selected_file = files[choice - 1]

            confirm = input(f"Are you sure you want to delete {selected_file}? (yes/no): ").lower()
            if confirm == 'yes':
                os.remove(f'payload_folder/{selected_file}')
                print(f"{selected_file} has been deleted.")
        else:
            print(" Invalid choice.")
        time.sleep(2)

def countdown():
    print(" \nStarting typing in:")
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)

def view_payload_files():
    files = [f for f in os.listdir('payload_folder') if f.startswith('payload')]
    if not files:
        print(" \nNo payload.txt file exists.")
    else:
        print(" \nAvailable payload files:")
        for i, file in enumerate(files, 1):
            print(f"{i}. {file}")

        try:
            choice = int(input("\nEnter the number of the payload you want to view (e.g., 1): "))
            if choice < 1 or choice > len(files):
                print(" Invalid choice. Please select a valid file number.")
            else:
                chosen_file = files[choice - 1]
                print(f"\nContents of {chosen_file}:")
                with open(f'payload_folder/{chosen_file}', 'r') as file:
                    for line in file:
                        print(line.strip())
        except ValueError:
            print(" Invalid input. Please enter a valid file number.")
        time.sleep(2)

if __name__ == "__main__":
    create_payload_folder()

    while True:
        clear_terminal()
        print("""
     ▄▄█▀▀▀▄█  ▀██                       ▄   █▀▀██▀▀█                                    
    ▄█▀     ▀   ██ ▄▄     ▄▄▄    ▄▄▄▄  ▄██▄     ██     ▄▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄    ▄▄▄▄  ▄▄▄ ▄▄  
    ██    ▄▄▄▄  ██▀ ██  ▄█  ▀█▄ ██▄ ▀   ██      ██      ▀█▄  █   ██▀  ██ ▄█▄▄▄██  ██▀ ▀▀ 
    ▀█▄    ██   ██  ██  ██   ██ ▄ ▀█▄▄  ██      ██       ▀█▄█    ██    █ ██       ██     
     ▀▀█▄▄▄▀█  ▄██▄ ██▄  ▀█▄▄█▀ █▀▄▄█▀  ▀█▄▀   ▄██▄       ▀█     ██▄▄▄▀   ▀█▄▄▄▀ ▄██▄    
                                                       ▄▄ █      ██                      
                                                        ▀▀      ▀▀▀▀                     

              """)
        print(" 1. Create or execute or delete payloads")
        print(" 2. View payload.txt files")
        print(" 3. Exit")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            create_or_type_or_delete_payloads()
        elif choice == '2':
            view_payload_files()
        elif choice == '3':
            print(" Exiting the program...")
            break
        else:
            print(" Invalid choice. Please try again.")
            time.sleep(2)

