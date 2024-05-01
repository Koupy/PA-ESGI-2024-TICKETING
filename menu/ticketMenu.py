import menu.mainMenu
import priority.ticketPriority

def categoryTicket():
  while True:
    choice = menu.mainMenu.getChoice()
  
    if choice == 1:
      priority.ticketPriority.lowTicketPriority()
    elif choice == 2:
      priority.ticketPriority.midTicketPriority()
    elif choice == 3:
      priority.ticketPriority.highTicketPriority()
    elif choice == 4:
      priority.ticketPriority.criticalTicketPriority()
    else:
      print(f"\033[91mOption invalide !\033[0m")

