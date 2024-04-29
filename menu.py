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
  print("1. Voir tous les tickets")
  print("2. Voir mes tickets")
  print("0. Quitter")

def mainMenuOption1():
    print("1")

def mainMenuOption2():
    print("2")

def mainMenuOption3():
    print("3")

def exitMenu():
    print("Exit")

