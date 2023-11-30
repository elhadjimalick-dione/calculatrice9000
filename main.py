def calculatrice():
    try:
        nombre1 = float(input("Entrez le premier nombre : "))
        operation = input("Entrez l'opération (+, -, *, /) : ")
        nombre2 = float(input("Entrez le deuxième nombre : "))

        if operation == "+":
            resultat = nombre1 + nombre2
        elif operation == "-":
            resultat = nombre1 - nombre2
        elif operation == "*":
            resultat = nombre1 * nombre2
        elif operation == "/":
            if nombre2 == 0:
                print("Erreur : Division par zéro est interdite.")
                return
            resultat = nombre1 / nombre2
        else:
            print("Erreur : Opération non valide.")
            return

        print(f"Le résultat de {nombre1} {operation} {nombre2} est : {resultat}")

    except ValueError as e:
        print(f"Erreur : {e}. Veuillez entrer des valeurs numériques et une opération valide.")
    except Exception as e:
        # Gérer les erreurs génériques
        print(f"Une erreur s'est produite : {e}. Veuillez réessayer.")

calculatrice()