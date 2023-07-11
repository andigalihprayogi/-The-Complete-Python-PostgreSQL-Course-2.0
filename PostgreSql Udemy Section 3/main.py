from database import add_entry, get_entries, create_table, delete_data


menu = """Please select one of the following options:
1) Add new sentry for today
2) View entries
3) Reset Data (Delete All data)
4) Exit

Your selection: """
welcome = "Welcome to the programming diary"

print(welcome)
create_table()


def promp_new_entry():
    entry_content = input("What have you learned today?")
    entry_date = input("Enter the date: ")
    add_entry(entry_content, entry_date)


def view_entries(entries):
    for entri in entries:
        print(f"{entri[1]}\n{entri[0]}\n\n")


while (user_input := input(menu)) != "4":
    if user_input == "1":
        promp_new_entry()
    elif user_input == "2":
        view_entries(get_entries())
    elif user_input == "3":
        delete_data()
        create_table()
    else:
        print("Invalid opyion, please try again!")
