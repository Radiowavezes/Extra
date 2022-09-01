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
if input_action == 1:
    full_name = input('Enter the full name: ')
    phone = input('Enter the phone: ')
    town = input('Enter the city: ')
    state = input('Enter the state: ')
    update_phonebook.setdefault(
                            full_name,
                                { 
                                'first_name': full_name.split()[0],
                                'last_name': full_name.split()[1],
                                'Phonenumber': phone,
                                'City': town,
                                'State': state,
                            }
                        )
elif input_action == 2:
    to_find = input('Input parameters to search a record: ')
    for person, params in update_phonebook.items():
        if to_find.lower() in person.lower():
            pprint(update_phonebook[person])
        else:
            for value in params.values():
                if to_find.lower() in value.lower():
                    pprint(update_phonebook[person])
elif input_action == 3:
    to_del = input('Input the phonenumber to delete a record: ')
    for person, params in update_phonebook.copy().items():
        for key, value in params.items():
            if to_del in value:
                update_phonebook.pop(person)
elif input_action == 4:
    to_upd = input('Input the phonenumber to update a record: ')
    for person, params in update_phonebook.copy().items():
        for key, value in params.items():
            if to_upd in value:
                for data_to_update in params:
                    params[data_to_update] = input(f'Enter the {data_to_update}: ')
else:
    print('Good bye!')
with open('phonebook', 'w') as output_file:
    json.dump(update_phonebook, output_file)
