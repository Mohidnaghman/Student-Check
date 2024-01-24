import Register
username = input("Enter your Username: ")
Password = input("Enter your Password: ")

with open("Database.txt","r+") as f:
    for line in f:
       file_name,file_password,status = line.strip().split(',')
       if file_name == username or file_password == Password:
          print("Welcome Admin! ")
          print("Authenticate successfully! ")
          print(""" 
                   Press 1 to Add Student
                   Press 2 to update student
""")
          inp = int(input("Enter Number Between 1/2: "))
          if inp == 1: 
             
              Register.register11()
          else:
             pass
          break
       else:
          print("Welcome User! ")
          break
  


