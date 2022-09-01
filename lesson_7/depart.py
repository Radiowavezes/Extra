from departments import DEPARTMENTS

import pprint


for position, people in DEPARTMENTS.items():
    result_employees = []
    for person in people:
        temp_employee = {
            'first_name': person['name'].split()[0],
            'second_name': person['name'].split()[1],
            'birthdate': person['birthdate'],
            'department': position,
        }
        result_employees.append(temp_employee)

pprint.pprint(result_employees)
