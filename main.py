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
    menu.mainMenuOption1()
  elif choice == 2:
    menu.mainMenuOption2()
  elif choice == 3:
    menu.mainMenuOption3()
  else:
    print(f"\033[91mOption invalide !\033[0m")