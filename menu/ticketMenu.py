import menu.mainMenu

def categoryTicket():
  while True:
    choice = menu.mainMenu.getChoice()
    
    if choice == 0:
      menu.mainMenu.exitMenu()
      break
    elif choice == 1:
      menu.mainMenu.mainMenuPriority()
    elif choice == 2:
      menu.mainMenu.mainMenuCategory()
    elif choice == 3:
      menu.mainMenu.mainMenuStatus()
    elif choice == 4:
      menu.mainMenu.mainMenuAllTickets()
    elif choice == 5:
      menu.mainMenu.mainMenuAllTickets()
    elif choice == 6:
      menu.mainMenu.mainMenuAllTickets()
    else:
      print(f"\033[91mOption invalide !\033[0m")