import requests
from datetime import datetime

def formatDate(date_str):
    date = datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %Z')
    formattedDate = date.strftime('%d/%m/%Y à %H:%M:%S')
    return formattedDate


def ticketActionMenu(selected_ticket):
    while True:
        print("\nActions disponibles pour le ticket:")
        print("1. Voir toutes les informations du ticket")
        print("2. Ajouter un commentaire")
        print("3. Changer le statut du ticket")
        print("4. Voir l'historique du ticket")
        print("0. Menu principal")

        choice = input("Entrez votre choix : ")
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

def displayTicketDetails(ticket):
    print("\nDétails du Ticket:")
    print(f"Titre: {ticket['title']}")
    print("\033[96m" + "."*10 + "\033[0m")
    print(f"Description: {ticket['description']}")
    print(f"Catégorie: {ticket['category']}")
    formattedDate = formatDate(ticket['created_at'])
    print(f"Créé le: {formattedDate}")
    print("\033[96m" + "."*10 + "\033[0m")

def addCommentToTicket(ticket):
    return 1

def changeTicketStatus(ticket):
    return 1

def displayTicketHistory(ticket):
    return 1