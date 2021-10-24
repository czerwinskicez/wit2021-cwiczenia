username = "Admin"
password = "1234"

is_auth = False

while is_auth == False:
    i_username = str(input("Login:"))
    i_password = str(input("Hasło:"))

    if i_username == username and i_password == password:
        is_auth = True

print("Zalogowano")