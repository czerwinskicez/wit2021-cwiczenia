dane_logowania={"Admin":"1234"}

authenticated=False
while not authenticated:
    login=input("Login: ")
    haslo=input("Haslo: ")

    if dane_logowania.get(login) and dane_logowania.get(login)==haslo:
        authenticated=True

print("Logowanie poprawne")