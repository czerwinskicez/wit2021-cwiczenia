wiek = int(input("Podaj swój wiek:"))
if wiek>=21:
    print("Możesz prowadzić samochód oraz głosować w wyborach")
elif wiek>17:
    print("Możesz prowadzić samochód")
else:
    print("Nie możesz głosować ani prowadzić samochodu")