import menu
import verif

print("Au Temps Donné - Ticketing")
while True:
  print("~"*50)
  menu.displayMainMenu()
  
  choice = menu.getChoice()
  
  if choice == 0:
    menu.exitMenu()
    break
  elif choice == 1:
    menu.mainMenuPriority()
  elif choice == 2:
    menu.mainMenuCategory()
  elif choice == 3:
    menu.mainMenuStatus()
  elif choice == 4:
    menu.mainMenuAllTickets()
  else:
    print(f"\033[91mOption invalide !\033[0m")