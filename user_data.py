while True:

    def show_imiona(imiona):
        imiona.sort()  # Sortuje listę imion alfabetycznie
        print(f"Imiona, które podałeś, jest ich {len(imiona)}, oto one: {', '.join(imiona)}")

    lista_imion = []

    for i in range(100):
        imie = input(f"Podaj imię nr {i+1}(jeśli chcesz zakończyć wpisywanie, napisz stop): ")
        if imie != "stop":
            lista_imion.append(imie)
        else:
            print("Zakończono wpisywanie imion.")
            break

    show_imiona(lista_imion)

    kontynuacja = input("Czy chcesz kontynuować? (tak/nie): ").strip().lower()
    if kontynuacja != "tak":
        print("Dziękujemy za skorzystanie z programu!")
        break