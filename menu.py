import ticket

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
  print("1. Voir les tickets par catégorie")
  print("2. Voir les tickets par statut")
  print("3. Voir tous les tickets")
  print("0. Quitter")

def mainMenuCategory():
    ticket.choosePriority()

def mainMenuStatus():
    ticket.chooseStatus()

def mainMenuAllTickets():
    ticket.seeTickets()

def exitMenu():
    print("Exit")

