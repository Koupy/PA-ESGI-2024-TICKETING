import menu.mainMenu
import priority.ticketPriority
import status.ticketStatus
import category.ticketCategory

def priorityTicket():
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
    
    break

def statusTicket():
  while True:
    choice = menu.mainMenu.getChoice()
  
    if choice == 1:
      status.ticketStatus.openTicket()
    elif choice == 2:
      status.ticketStatus.ongoingTicket()
    elif choice == 3:
      status.ticketStatus.closedTicket()
    else:
      print(f"\033[91mOption invalide !\033[0m")

    break

def categoryTicket():
  while True:
    choice = menu.mainMenu.getChoice()
  
    if choice == 1:
      category.ticketCategory.stockTicket()
    elif choice == 2:
      category.ticketCategory.truckTicket()
    elif choice == 3:
      category.ticketCategory.warehouseTicket()
    elif choice == 4:
      category.ticketCategory.serviceTicket()
    elif choice == 5:
      category.ticketCategory.planningTicket()
    elif choice == 6:
      category.ticketCategory.activityTicket()
    else:
      print(f"\033[91mOption invalide !\033[0m")

    break