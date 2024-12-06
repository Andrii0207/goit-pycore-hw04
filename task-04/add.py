

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    print("Contact added.")