import ticket
import menu.ticketMenu

def choosePriority():
    priority_map = {1: "faible", 2: "moyen", 3: "élevé", 4: "critique"}
    ticket.displayChoices('priority', priority_map)
    menu.ticketMenu.categoryTicket()

def displayTicketsByPriority(priority):
    tickets = ticket.getTickets()
    for ticket_item in tickets:
        if ticket_item['priority'] == priority:
            print("."*10)
            print(ticket_item['title'])
            print(f"Description : {ticket_item['description']}")
            print("Quel ticket souhaitez vous voir ?")

def lowTicketPriority():
    displayTicketsByPriority(1)

def midTicketPriority():
    displayTicketsByPriority(2)

def highTicketPriority():
    displayTicketsByPriority(3)

def criticalTicketPriority():
    displayTicketsByPriority(4)
