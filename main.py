import datetime



def file(): # I've learned dealing with file from here    https://www.youtube.com/watch?v=ZCmdm-RuRFA&list=PLuXY3ddo_8nzrO74UeZQVZOb5-wIS6krJ&index=30&ab_channel=Codezilla
    d = {}
    with open("Employees.txt") as f: # Converting to dictionary from here   https://stackoverflow.com/questions/4803999/how-to-convert-a-file-into-a-dictionary
        for line in f:
            (emp_id, name, time, gender, salary) = line.strip().split(", ")
            d[name] = {
                'emp_id': emp_id,
                'Time': time,
                'Gender': gender,
                'Salary': int(salary)
            }
    # print(d)  it was just for reference
    return login(d)

def login(d):

    count = 0
    print("Welcome to the system !")

    while count < 5:
        username = input('Enter username: ')
        password = input('Enter password: ')

        if password == 'admin123123' and username == 'admin':
            admin_menu(d)
            break

        elif username in d and password == "" :
            user_menu (username,d)
            break

        else:
            count += 1
            print('Access denied. Try again. You still got ',(5-count),'times to try and the system will close')


def a_menu():
    print("1. Display Statistics")
    print("2. Add an Employee")
    print("3. Display All Employees")
    print("4. Change Employee Salary")
    print("5. Remove Employee")
    print("6. Raise Employee's Salary")
    print("7. Exit")
    pass


def add_employee(d):
    emp_id = "emp" + str(len(d) + 1)
    username = input("Enter username: ")
    gender = input("Enter gender (male/female): ")
    salary = int(input("Enter salary: "))
    timestamp = datetime.datetime.now().strftime('%Y%m%d')  # I know this from a Female Automated Voice Assistant that I've made before

    d[username] = {
        'emp_id': emp_id,
        'Time': timestamp,  # You can update this with actual DOB input if needed
        'Gender': gender,
        'Salary': salary
    }

    with open("Employees.txt", "a") as f:
        f.write('{}, {}, {}, {}, {}\n'.format(emp_id, username, timestamp, gender,salary))   #https://stackoverflow.com/questions/6931183/how-to-write-multiple-values-into-one-line-in-a-text-file

    print("Employee added successfully!")

def display_all():
    d = {}
    a=open("Employees.txt","r") #same ref https://www.youtube.com/watch?v=ZCmdm-RuRFA&list=PLuXY3ddo_8nzrO74UeZQVZOb5-wIS6krJ&index=30&ab_channel=Codezilla
    sorted_lines = sorted(a, key=lambda line: line.split(", ")[2], reverse=True) # https://stackoverflow.com/questions/56561266/sort-text-file-lines-using-python-by-timestamp
    for line in sorted_lines:
        print(line)

def change_salary():
    emp_id_to_update = input("Enter Employee's ID: ")
    new_salary = input("Enter the new salary: ")

    with open("Employees.txt", "r") as f:
        lines = f.readlines()

    with open("Employees.txt", "w") as f:
        for line in lines:
            emp_id, name, time, gender, salary = line.strip().split(", ")
            if emp_id == emp_id_to_update:
                f.write("{}, {}, {}, {}, {}\n".format(emp_id, name, time, gender, new_salary))
            else:
                f.write(line)

    print("Salary updated successfully!")


def admin_menu(d):
    print("welcome admin")

    while True:
        a_menu()
        x = input("Choose a number: ")
        if x == '1':
            male = sum(1 for employee in d.values() if employee['Gender'] == 'male') # I took this snippet from here https://www.geeksforgeeks.org/python-sum-values-for-each-key-in-nested-dictionary/
            female = sum(1 for employee in d.values() if employee['Gender'] == 'female')
            print("Male Employees:", male)
            print("Female Employees:", female)

        elif x == '2':
            add_employee(d)

        elif x == '3':
            display_all()

        elif x == '4':
            change_salary()

        elif x == '5':
            pass
        elif x == '6':
            pass
        elif x == '7':
            pass
        else:
            print("Wrong input")




def user_menu(username,d):

    gender = d[username]['Gender']
    if gender == "male":
        print("Welcome Mr. "+username)
    else:
        print("Welcome Ms. "+username)
    pass



file()