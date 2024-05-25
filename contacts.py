import argparse

# Input phone numbers for Masha, Pasha, and Natasha
masha_number = int(input("Введите номер Маши: "))
pasha_number = int(input("Введите номер Паши: "))
natasha_number = int(input("Введите номер Наташи: "))

# Input contact name to delete or 'all' to clear all contacts
contact_to_delete = input(
    "Вы бы хотели удалить какой-нибудь контакт(напишите название контакта) \n (Так же если хотите обнулить контакты пишите all)\nПишите имена на английском языке: "
)

# Create a dictionary to store contacts
phone_book = {"Masha": masha_number, "Pasha": pasha_number, "Natasha": natasha_number}

# Handle contact deletion based on user input
if contact_to_delete == "Masha":
    phone_book.pop("Masha", None)
elif contact_to_delete == "Pasha":
    phone_book.pop("Pasha", None)
elif contact_to_delete == "all":
    phone_book.clear()

# Initialize ArgumentParser for command-line arguments
parser = argparse.ArgumentParser(description="Телефонная книга")

# Define command-line arguments for adding, deleting, and showing contacts
parser.add_argument("--add", dest="add_param", nargs=2, default=[], action="append")
parser.add_argument("--delete", dest="delete_param", nargs=1, default=[], action="append")
parser.add_argument("--show", dest="show_param", nargs=1, default=["all"])

args = parser.parse_args()

# Process the command-line arguments to add, delete, or show contacts
if args.add_param:
    name, tele = args.add_param[0]
    phone_book[name] = tele
    print(f"Контакт {name} с номером {tele} добавлен")
elif args.delete_param:
    name = args.delete_param[0][0]
    if name in phone_book:
        del phone_book[name]
        print(f"Контакт {name} удален")
    else:
        print(f"Контакт {name} не найден")
elif args.show_param:
    if args.show_param[0] == "all":
        for name, tele in phone_book.items():
            print(f"{name}: {tele}")
    else:
        name = args.show_param[0][0]
        if name in phone_book:
            print(f"{name}: {phone_book[name]}")
        else:
            print(f"Контакт {name} не найден")
