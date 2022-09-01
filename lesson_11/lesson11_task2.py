import json

input_file = input("Enter the name of the phonebook: ")
try:
    phonebook = open(input_file, 'a+')
except:
    print("No such file exists")
else:
    while True:
        try:
            input_action = int(
                input(
                    """
                                    What do you want to get?
                                    - to add data, press 1
                                    - to find data, press 2
                                    - to delete a record, press 3
                                    - to update a record, press 4
                                    - to exit, press 0
                                """
                )
            )

        except ValueError:
            print("Please, type the number of action ")
        else:
            break
update_phonebook = {}
if input_action == 1:
    full_name = input("Please, enter the full name: ")
    update_phonebook[full_name] = {
        "first_name": full_name.split()[0],
        "last_name": full_name.split()[1],
        "Phonenumber": input("Enter the phone number: "),
        "City": input("Enter the city: "),
        "State": input("Enter the state: "),
    }
    json.dump(update_phonebook, phonebook)

