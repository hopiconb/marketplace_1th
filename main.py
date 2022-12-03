

while True:
    # meniu principal
    print("1 - Utilizatori")
    print("2 - Produse")
    print("3 - Comenzi")
    print("4 - Inchide")

    # variabila meniu principal
    g = input("cmd: ")
    g = g.strip()

    if g == "1":  # Utilizatori
        print("Utilizatori \n")
        print("1 - Adauga")
        print("2 - Afiseaza")
        print("3 - Sterge")
        u1 = input("cmd: ")  # variabila pentru meniu utilizator

        if u1 == "1":  # adauga utilizatori
            print()

        elif u1 == "2":  # afiseaza lista de utilizatori
            print()

        elif u1 == "3":  # sterge utilizatori
            print()

    elif g == "2":  # Produse
        print("Produse\n")
        # adauga produse

        # afiseaza lista de produse

        # sterge produse

    elif g == "3":  # Comenzi
        print("Comenzi\n")
        # adauga comenzi

        # afiseaza lista de comenzi

        # modifica o comanda

        # sterge comenzi

    elif g == "4":
        print("Se inchide programul")
        break
    else:
        print("Optiune invalida, te rog foloseste un numar valid")
