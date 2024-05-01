import ticket
import menu.ticketMenu

def choosePriority():
    priority_map = {1: "faible", 2: "moyen", 3: "élevé", 4: "critique"}
    ticket.displayChoices('priority', priority_map)
    menu.ticketMenu.priorityTicket()

def displayTicketsByPriority(priority):
    tickets = ticket.getTickets()
    foundTickets = False
    for ticket_item in tickets:
        if ticket_item['priority'] == priority:
            foundTickets = True
            print("\033[96m" + "."*10 + "\033[0m")
            print(ticket_item['title'])
            print(f"Description : {ticket_item['description']}")
    
    return foundTickets 

def lowTicketPriority():
    if not displayTicketsByPriority(1):
        print("Il n'y a pas de tickets de priorité faible.")
        return

def midTicketPriority():
    if not displayTicketsByPriority(2):
        print("Il n'y a pas de tickets de priorité moyenne.")
        return

def highTicketPriority():
    if not displayTicketsByPriority(3):
        print("Il n'y a pas de tickets de priorité élevée.")
        return

def criticalTicketPriority():
    if not displayTicketsByPriority(4):
        print("Il n'y a pas de tickets de priorité critique.")
        return
