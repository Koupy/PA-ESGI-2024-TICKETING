import requests

def ticketAction(selected_ticket):
    while True:
        print("\nActions disponibles pour le ticket:")
        print("1. Voir toutes les informations du ticket")
        print("2. Ajouter un commentaire")
        print("3. Changer le statut du ticket")
        print("4. Voir l'historique du ticket")
        print("0. Menu principal")

        choice = input("Entrez votre choix (1-4): ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                displayTicketDetails(selected_ticket)
            elif choice == 2:
                addCommentToTicket(selected_ticket)
            elif choice == 3:
                changeTicketStatus(selected_ticket)
            elif choice == 4:
                displayTicketHistory(selected_ticket)
            elif choice == 0:
                break
            else:
                print("Choix invalide. Veuillez entrer un nombre entre 1 et 4.")
        else:
            print("Veuillez entrer un nombre.")

def displayTicketDetails(selected_ticket):
    return 1

def addCommentToTicket(selected_ticket):
    return 1

def changeTicketStatus(selected_ticket):
    return 1

def displayTicketHistory(selected_ticket):
    return 1