import menu


while True:
  print("Au Temps Donné - Ticketing")
  menu.displayMainMenu()
  
  choix = menu.getChoice()
  
  if choix == 0:
      menu.exitMenu()
      break
  elif choix == 1:
      menu.mainMenuOption1()
  elif choix == 2:
      menu.mainMenuOption2()
  elif choix == 3:
      menu.mainMenuOption3()
  else:
      print("Option invalide")

