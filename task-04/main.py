from parser import parse_input
from add import add_contact
from change import change_contact
from show import show_phone
from all import show_all


def main():
    print("Welcome to the assistant bot!")

    contacts = {"John": "0987654321"}
    # contacts = {}

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
 
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        else:
            print("Invalid command.")



if __name__ == "__main__":
    main()
