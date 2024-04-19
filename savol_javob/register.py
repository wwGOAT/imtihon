from db import Database


def register():
    print("Register Page")
    full_name = input("Full Name: ")
    phone_number = input("Phone Number: ")
    while len(phone_number) != 9:
        print("\nBunday yoza olmaysiz\n")
        phone_number = input("Phone Number: ")
    username = input("Username: ")
    password = input("Password: ")

    query = f"""INSERT INTO users(full_name, phone_number, username, password) 
    VALUES('{full_name}', '{phone_number}', '{username}', '{password}')"""

    print(Database.connect(query, "insert"))
    return None

if __name__ == "__main__":
    register()