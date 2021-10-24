kapital_poczatkowy = int(input("Podaj kapitał początkowy: "))
miesieczne_wplywy = int(input("Podaj miesięczne wpływy: "))
okres_inwestowania = int(input("Podaj okres inwestowania (w miesiącach): "))
docelowa_wartosc = int(input("Podaj docelową wartość inwestycji: "))

kapital = kapital_poczatkowy + miesieczne_wplywy * okres_inwestowania

kapital = kapital * 1.02

print("Ilość pieniędzy po docelowym okresie inwestowania: ", kapital)
if kapital >= docelowa_wartosc:
    print("Finalna wartość inwestycji jest większa lub równa niż zakładana docelowa wartość.")
else:
    print("Wartość inwestycji mniejsza niż zakładano.")