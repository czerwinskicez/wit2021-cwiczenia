srednia_predkosc_samochodu = int(input("Podaj średnią prędkość samochodu na tej trasie: "))

srednia_predkosc_pociagu = 250 / (2+(45/60))

if srednia_predkosc_samochodu > srednia_predkosc_pociagu:
    print("Dojedziesz szybciej niż pociąg")
else:
    print("Pociąg będzie szybciej niż Ty")