



def file(): # I've learned dealing with file from here    https://www.youtube.com/watch?v=ZCmdm-RuRFA&list=PLuXY3ddo_8nzrO74UeZQVZOb5-wIS6krJ&index=30&ab_channel=Codezilla
    d = {}
    with open("Employees.txt") as f: # Converting to dictionary from here   https://stackoverflow.com/questions/4803999/how-to-convert-a-file-into-a-dictionary
        for line in f:
            (emp_id, name, dob, gender, salary) = line.strip().split(", ")
            d[emp_id] = {
                'Name': name,
                'Date of Birth': dob,
                'Gender': gender,
                'Salary': int(salary)
            }
    print(d)
    return login(d)
def login(d):

    ua = "admin"
    up = "admin123123"
    count = 0
    print("Welcome to the system !")
    username = ""
    password = ""

    while password != 'admin123123' and username != 'admin' and count < 5:
        username = input('Enter username: ')
        password = input('Enter password: ')

        if password == 'admin123123' and username == 'admin':
            admin_menu()
            break

        elif username in d.values() and password == "" :
            user_menu (username,d)
            break

        else:
            count += 1
            print('Access denied. Try again. You still got ',(5-count),'times to try and the system will close')



def admin_menu():
    print("welcome admin")



def user_menu(username,d):

    # gender = d[][2]
    # if gender == "male":
    #     print("Welcome Mr. "+username)
    # else:
    #     print("Welcome Ms. "+username)
    pass



file()