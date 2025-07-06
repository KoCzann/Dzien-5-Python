def polecenie(lista):
    for filmy in lista:
        print(f"Dzięki za polecenie: {filmy}")

lista_filmów = []

for i in range(4):
    film = input(f"Podaj ulubiony film nr {i+1}, który warto obejrzeć:")
    if film != "":
        lista_filmów.append(film)
    else:
        print(f"Nie podałeś {i+1} filmu.")
        continue
    
polecenie(lista_filmów)