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

def mainMenuOption1():
    print("1")

def mainMenuOption2():
    print("2")

def mainMenuOption3():
    print("3")

def exitMenu():
    print("Exit")

