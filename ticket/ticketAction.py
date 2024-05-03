import ticket.ticketResponse
import ticket.ticketChoice
import json
from datetime import datetime

def formatDate(dateStr):
    try:
        date = datetime.strptime(dateStr, '%a, %d %b %Y %H:%M:%S')
        return date.strftime('%d/%m/%Y à %H:%M:%S')
    except ValueError:
        return dateStr

def parseMessage(message):
    try:
        if message.startswith("{"):
            messageDict = json.loads(message.replace("'", '"'))
            return messageDict.get('comment', message)
        return message
    except json.JSONDecodeError:
        return message
    
def ticketActionMenu(selectedTicket):
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
                displayTicketDetails(selectedTicket)
            elif choice == 2:
                addCommentToTicket(selectedTicket)
            elif choice == 3:
                changeTicketStatus(selectedTicket)
            elif choice == 4:
                displayTicketHistory(selectedTicket)
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

def addCommentToTicket(selectedTicket):
    ticketId = selectedTicket['id']
    userId = selectedTicket['user_id']
    comment = input("Entrez votre commentaire: ")
    currentTime = datetime.now()
    
    try:
        ticket.ticketResponse.ticketAnswer(ticketId, userId, comment)
        print("\033[92mCommentaire ajouté.\033[0m")
    except Exception as e:
        print(currentTime)
        print(f"\033[91mErreur lors de l'ajout du commentaire: {str(e)}\033[0m")


def changeTicketStatus(selectedTicket):
    while True:
        print("\nChanger le statut du ticket:")
        print("2. Mettre le ticket en cours")
        print("3. Résoudre le ticket")
        print("0. Quitter")

        choice = input("Votre choix: ")

        if choice.isdigit():
            choice = int(choice)
            if choice == 2:
                selectedTicket['status'] = "En cours"
                ticket.ticketChoice.updateTicketStatus(selectedTicket)
                print("\033[92mLe statut du ticket a été mis à jour vers 'En cours'.\033[0m")
                break
            elif choice == 3:
                selectedTicket['status'] = "Resolu"
                ticket.ticketChoice.updateTicketStatus(selectedTicket)
                print("\033[92mLe statut du ticket a été mis à jour vers 'Résolu'.\033[0m")
                break
            elif choice == 0:
                print("Opération annulée.")
                break
            else:
                print("\033[91mChoix invalide !\033[0m")
        else:
            print("\033[91mVeuillez entrer un nombre !\033[0m")
    
def displayTicketHistory(selectedTicket):
    test = ticket.ticketResponse.getTicketAnswers()
    print(test)
    ticketID = selectedTicket['id']
    print(ticketID)
    allResponses = ticket.ticketResponse.getTicketAnswers()  
    filteredResponses = [response for response in allResponses if response['ticket_id'] == ticketID]

    print(f"\nHistory for Ticket ID {ticketID}:")
    if filteredResponses:
        for entry in filteredResponses:
            createdAt = formatDate(entry['created_at'])
            message = parseMessage(entry['message'])
            updatedAt = formatDate(entry['updated_at']) if entry['updated_at'] else 'N/A'

            print(f"Posté le: {createdAt}")
            print(f"Message: {message}")
            print("\033[96m" + "."*10 + "\033[0m")

    else:
        print("No history available for this ticket.")