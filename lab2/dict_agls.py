lena = {'name': 'lena',
        'age': 34,
        'children': [{
            'name': 'vasja',
            'age': 12
        },  {
            'name': 'petja',
            'age': 9
             }
        ]
        }

ivan = {'name': 'ivan',
        'age': 45,
        'children': [{
            'name': 'sasha',
            'age': 21
        },  {
            'name': 'mark',
            'age': 19
             }
        ]
        }

employees = [lena, ivan]


#! Вывести имя сотрудника, ребёнок которого старше 18
def more18(arr):
    for emp in arr:
        for child in emp['children']:
            if child['age'] >= 18:
                print(emp['name'])
                break
    pass


more18(employees)