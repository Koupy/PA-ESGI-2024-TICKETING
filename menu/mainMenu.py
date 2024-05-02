import category.ticketCategory
import priority.ticketPriority
import status.ticketStatus
import ticket.ticketChoice
import priority
import status
import category

def getChoice():
    while True:
        try:
            choix = int(input("Entrez votre choix: "))
            return choix
        except ValueError:
            print(f"\033[91mVeuillez entrer un nombre !\033[0m")
            print("~"*50)
            displayMainMenu()

def displayMainMenu():
  print("1. Voir les tickets par priorité")
  print("2. Voir les tickets par catégorie")
  print("3. Voir les tickets par statut")
  print("4. Voir tous les tickets")
  print("0. Quitter")

def mainMenuPriority():
    priority.ticketPriority.choosePriority()

def mainMenuCategory():
    category.ticketCategory.chooseCategory()

def mainMenuStatus():
    status.ticketStatus.chooseStatus()

def mainMenuAllTickets():
    ticket.ticketChoice.seeTickets()

def exitMenu():
    print("Exit")

