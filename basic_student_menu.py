students = [
    {
        "id": 1,
        "name": "Student One",
        "age": 19,
        "school_name": "Humber College",
        "completed": {
            "Math": 97,
            "Science": 87
        },
        "ongoing": {
            "Computer Science": 94,
            "Geography": 85
        }
    },
    {
        "id": 2,
        "name": "Student Two",
        "age": 20,
        "school_name": "Humber College",
        "completed": {
            "Math": 63,
            "Science": 75
        },
        "ongoing": {
            "Computer Science": 80,
            "Geography": 72
        }
    },
    {
        "id": 3,
        "name": "Student Three",
        "age": 18,
        "school_name": "Humber College",
        "completed": {
            "Math": 80,
            "Science": 91
        },
        "ongoing": {
            "Computer Science": 96,
            "Geography": 63
        }
    }
]


def all(i):
    print(f'Student ID: {i["id"]}')
    print(f'Name: {i["name"]}')
    print(f'Age: {i["age"]}')
    print(f'School Name: {i["school_name"]}')
    print("Completed:")
    for c in i["completed"].items():
        print(f"{c[0]} : {c[1]}")
    for c in i["ongoing"].items():
        print(f"{c[0]} : {c[1]}")


menu = "1. View all students’ information\n2. View all information on specific student\n3. View all ongoing grades of specific student\n4. View all completed grades of specific student\n5. View average completed grades of student\n6. View specific grade of specific student"

loop = True

while loop:
    print(menu)
    operation = int(input("Choose an operation (1/2/3/4/5/6): "))
    found = False
    if operation == 1:
        found = True
        for i in students:
            all(i)

    else:
        s_id = int(input("Enter needed student id: "))
        for i in students:
            if s_id == i["id"]:
                found = True
                if operation == 2:
                    all(i)
                elif operation == 3:
                    for c in i["ongoing"].items():
                        print(f"{c[0]} : {c[1]}")
                elif operation == 4:
                    for c in i["completed"].items():
                        print(f"{c[0]} : {c[1]}")
                elif operation == 5:
                    grades = list(i["completed"].values())
                    print(f"Completed Course Average: {sum(grades)/len(grades):.2f}")
                elif operation == 6:
                    found = False
                    c_name = input("Enter needed course name: ")
                    full = list(i["ongoing"].items())
                    completed = list(i["completed"].items())
                    full.extend(completed)
                    for c in full:
                        if c[0].lower() == c_name.lower():
                            found = True
                            print(f"{c[0]} : {c[1]}")
    if not found:
        print("No information found!")


    ct = input("Would you like to perform another query?(y/n): ")
    if ct.lower() == 'n':
        loop = False
