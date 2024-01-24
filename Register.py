def register11():
    username = input("Enter username: ")
    password = input("Enter password: ")
    status1 = input("Enter status: ")
    with open("Database.txt", "r+") as f:
            for line in f:

                file_name,file_password,status = line.strip().split(',')
                if file_name == username or file_password == password:
                     print("This username and password are already exit! ")
                else:
                     new_username = username
                     new_password = password
                     status = status1


                     f.write(f" {new_username},{new_password}, {status} ")
