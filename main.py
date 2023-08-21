import datetime


# I sent manuella the email of submitting and hour or two ago, and now I remembered that we have to put the big(O)


# O(1) because it is fixed number of prints
def a_menu():
    print("1. Display Statistics")
    print("2. Add an Employee")
    print("3. Display All Employees")
    print("4. Change Employee Salary")
    print("5. Remove Employee")
    print("6. Raise Employee's Salary")
    print("7. Exit")


# O(1) because it is fixed number of prints
def u_menu():
    print("1. Check My Salary")
    print("2. Exit")


# O(n) because it is the worst case depending on n; n being the number of data in file
def file():  # I've learned dealing with file from here
    # https://www.youtube.com/watch?v=ZCmdm-RuRFA&list=PLuXY3ddo_8nzrO74UeZQVZOb5-wIS6krJ&index=30&ab_channel=Codezilla
    d = {}
    with open(
            "Employees.txt") as f:  # Converting to dictionary from here
        # https://stackoverflow.com/questions/4803999/how-to-convert-a-file-into-a-dictionary
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


# O(1) because it is fixed number of 5 times trying
def login(d):
    count = 0  # The max it can get is 4
    print("Welcome to the system !")

    while count < 5:
        username = input('Enter username: ')
        password = input('Enter password: ')

        if password == 'admin123123' and username == 'admin':
            admin_menu(d)
            break

        elif username in d and password == "":
            user_menu(username, d)
            break

        else:
            count += 1
            print('Access denied. Try again. You still got ', (5 - count), 'times to try and the system will close')


# O(1) because we are adding only one employee at a time
def add_employee(d):
    emp_id = "emp" + str(len(d) + 1)  # I didn't know how to make emp00, so I used this
    username = input("Enter username: ")
    gender = input("Enter gender (male/female): ")
    salary = int(input("Enter salary: "))
    timestamp = datetime.datetime.now().strftime(
        '%Y%m%d')  # I know this from a Female Automated Voice Assistant that I've made before

    d[username] = {  # I found an example on how to fill nested dictionaries and changed the keys and values
        'emp_id': emp_id,
        'Time': timestamp,  # since we don't need to input it manually I removed the previous comment about that we
        # can add it manually
        'Gender': gender,
        'Salary': salary
    }

    with open("Employees.txt", "a") as f:
        f.write('{}, {}, {}, {}, {}\n'.format(emp_id, username, timestamp, gender,
                                              salary))  # https://stackoverflow.com/questions/6931183/how-to-write
        # -multiple-values-into-one-line-in-a-text-file

    print("Employee added successfully!")


# O(n) because we don't know how many employees we have and n is number of employees (worst case n)
def display_all():
    a = open("Employees.txt",
             "r")  # same ref https://www.youtube.com/watch?v=ZCmdm-RuRFA&list=PLuXY3ddo_8nzrO74UeZQVZOb5-wIS6krJ
    # &index=30&ab_channel=Codezilla
    sorted_lines = sorted(a, key=lambda line: line.split(", ")[2],
                          reverse=True)  # https://stackoverflow.com/questions/56561266/sort-text-file-lines-using
    # -python-by-timestamp
    for line in sorted_lines:
        print(line)


# O(1) because we are changing only one value for one employee
def change_salary():
    emp_id_update = input("Enter Employee's ID: ")
    new_salary = input("Enter the new salary: ")

    with open("Employees.txt",
              "r") as f:  # here I opened the file to then loop in it to check when the users input is = to the
        # emp_id to rewrite the employee with the new salary
        lines = f.readlines()

    with open("Employees.txt", "w") as f:
        for line in lines:
            emp_id, name, time, gender, salary = line.strip().split(", ")
            if emp_id == emp_id_update:
                f.write("{}, {}, {}, {}, {}\n".format(emp_id, name, time, gender,
                                                      new_salary))  # I couldn't see anything about update so I rewrote
            else:
                f.write(line)

    print("Salary updated successfully!")


# O(1) because we are removing only one employee
def remove():  # here I just copied the one with edit and removed the writing
    emp_id_r = input("Enter Employee's ID You Wish To Remove: ")

    with open("Employees.txt", "r") as f:
        lines = f.readlines()

    with open("Employees.txt", "w") as f:
        for line in lines:
            emp_id, name, time, gender, salary = line.strip().split(", ")  # when I used this alone it deleted all
            if emp_id != emp_id_r:  # that is why I used this to see if it is not the employee I want to remove it keeps
                f.write(line)
                print("Employee not found")
            else:
                del [emp_id_r]  # I've got the delete from here
                # https://www.w3schools.com/python/python_dictionaries_remove.asp
                print("Employee Removed Successfully!")


# O(1) because we are raising one value for one employee
def raise_salary():
    d = {}
    with open(
            "Employees.txt") as f:  # Converting to dictionary from here
        # https://stackoverflow.com/questions/4803999/how-to-convert-a-file-into-a-dictionary
        for line in f:
            (emp_id, name, time, gender, salary) = line.strip().split(
                ", ")  # I had to make a new one with emp_id as key in order to access the rest
            d[emp_id] = {
                'Name': name,
                'Time': time,
                'Gender': gender,
                'Salary': int(salary)
            }
    emp_id = input("Enter Employee's ID: ")

    if emp_id in d:
        percentage = (input("Enter the raise percentage (e.g., 10 for 10%): "))  # It made an error when the
        # user inputs something else than float, so I changed it to normal then check it down
        if percentage.isdigit():  # is digit I learned it from previous assignment
            current_salary = d[emp_id]['Salary']
            new_salary = int(current_salary * (1 + int(percentage) / 100))
            d[emp_id]['Salary'] = new_salary
            print("Salary raised successfully!")
            with open("Employees.txt", "w") as f:
                for emp_id, emp_data in d.items():
                    # f.write("{}, {}, {}, {}, {}\n".format(emp_id, name, time, gender, new_salary))# I used this
                    # didn't work
                    line = "{}, {}, {}, {}, {}\n".format(emp_id, emp_data['Name'], emp_data['Time'],emp_data['Gender'],emp_data['Salary'])
                    # that is why I used this using this
                    # link (I had to manipulate it due to many data) https://stackoverflow.com/questions/48345630/writing-a-nested-dictionary-to-a-txt-file
                    f.write(line)
        else:
            print("wrong input")

    else:
        print("Employee not found.")


# O(n) although it is a fixed number of 7 choices but after each choice it will repeat until user press exit,
# so I believe it must be O(n) referring to how many times admin uses the system at the time (while true)
def admin_menu(d):
    print("welcome admin")

    while True:
        a_menu()
        x = input("Choose a number: ")
        if x == '1':
            male = sum(1 for employee in d.values() if employee[
                'Gender'] == 'male')  # I took this snippet from here
            # https://www.geeksforgeeks.org/python-sum-values-for-each-key-in-nested-dictionary/
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
            remove()

        elif x == '6':
            raise_salary()
        elif x == '7':
            break  # the saving is already done in other function each time
        else:
            print("Wrong input")


# same as admin_menu O(n)
def user_menu(username, d):
    gender = d[username]['Gender']  # here the dictionary have the username as the key in order to get as male or female
    if gender == "male":
        print("Welcome Mr. " + username)
    else:
        print("Welcome Ms. " + username)
    while True:
        u_menu()
        x = input("Choose a number: ")
        if x == '1':
            a = d[username]['Salary']
            print("My Salary is: ", a)
        elif x == '2':
            new_time = datetime.datetime.now().strftime('%Y%m%d')
            with open("Employees.txt", "r") as f:
                lines = f.readlines()
            with open("Employees.txt", "w") as f:
                for line in lines:
                    emp_id, name, time, gender, salary = line.strip().split(", ")
                    if name == username:
                        f.write("{}, {}, {}, {}, {}\n".format(emp_id, name, new_time, gender,
                                                              salary))  # I used the one like change salary
                    else:
                        f.write(line)
            break
        else:
            print("Wrong input")


file()
