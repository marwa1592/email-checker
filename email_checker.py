import time 

def validate_email(email):
    if "@" in email and "." in email: 
       return True
    else: 
       return False

def add_user(name,email):
    if validate_email(email):
    #or if validate_email(email) == True  هي هي 
      print(f"User {name} with email {email} was successfully added!")
    else: 
      print(f"INvalid Email format for user {name}. Registration faild.")
user_name = input("Ente your user name: ")
user_email = input("Enter your email address..")


print("Cheking user name .... please wait")
time.sleep(2)
print("Validating email adress ... please wait ")
time.sleep(2)

add_user(user_name, user_email)
