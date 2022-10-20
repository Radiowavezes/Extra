import json

from pprint import pprint

input_file = input("Enter the name of the phonebook: ")
try:
    phonebook = open(input_file)
except:
    print("No such file exists")
else:
    update_phonebook = json.load(phonebook)
while True:
    input_action = input(
        """
                        What do you want to get?
                        - to add data, press 1
                        - to find data, press 2
                        - to delete a record, press 3
                        - to update a record, press 4
                        - to exit, press 0
                    """
    )
    try:
        input_action = int(input_action)
    except ValueError:
        print("Please, input your NUMBER of choice: ")
    else:
        if input_action in range(5):
            break
        else:
            print("Please, input your number of choice, from 0 to 4: ")
if input_action == 1: # to add data
    full_name = input("Enter the full name: ")
    if update_phonebook.get(full_name) == None:
        phone = input("Enter the phone: ")
        town = input("Enter the city: ")
        state = input("Enter the state: ")
        update_phonebook.setdefault(
            full_name,
            {
                "first_name": full_name.split()[0],
                "last_name": full_name.split()[1],
                "Phonenumber": phone,
                "City": town,
                "State": state,
            },
        )
        pprint(update_phonebook[full_name])
    else:
        print("Such record already exists!")
elif input_action == 2: # to find data
    to_find = input("Input parameters to search a record: ")
    is_found = 0
    for person, params in update_phonebook.items():
        if to_find.lower() in person.lower():
            pprint(update_phonebook[person])
            is_found = 1
        else:
            for value in params.values():
                if to_find.lower() in value.lower():
                    pprint(update_phonebook[person])
                    is_found = 1
    if not is_found:
        print("Sorry, there's no record with such parameters")
elif input_action == 3: # to delete a record
    to_del = input("Input the phonenumber to delete a record: ")
    is_del = 0
    for person, params in update_phonebook.copy().items():
        for key, value in params.items():
            if to_del == value:
                update_phonebook.pop(person)
                is_del = 1
    if is_del:
        print("Done")
    else:
        print("Sorry, there's no record with such phonenumber")

elif input_action == 4: # to update a record
    to_upd = input("Input the phonenumber to update a record: ")
    is_upd = 0
    for person, params in update_phonebook.copy().items():
        for key, value in params.items():
            if to_upd in value:
                is_upd = 1
                for data_to_upd in params:
                    params[data_to_upd] = input(f"Enter the {data_to_upd}: ")
    if not is_upd:
        print("Sorry, there's no record with such phonenumber")
else: # to exit
    print("Good bye!")
with open("phonebook", "w") as output_file:
    json.dump(update_phonebook, output_file)
