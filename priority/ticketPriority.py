import ticket
import menu.ticketMenu

def choosePriority():
    priority_map = {1: "faible", 2: "moyen", 3: "élevé", 4: "critique"}
    ticket.displayChoices('priority', priority_map)

    menu.ticketMenu.categoryTicket()

def lowTicketPriority():
    tickets = ticket.getTickets()
    for lowTickets in tickets:
        if lowTickets['priority'] == 1:
            print("."*10)
            print(lowTickets['title'])  
            print(f"Description : {lowTickets['title']}")  

def midTicketPriority():
    tickets = ticket.getTickets()
    for midTickets in tickets:
        if midTickets['priority'] == 2:
            print("."*10)
            print(midTickets['title'])  
            print(f"Description : {midTickets['title']}")

def highTicketPriority():
    tickets = ticket.getTickets()
    for highTickets in tickets:
        if highTickets['priority'] == 3:
            print("."*10)
            print(highTickets['title'])  
            print(f"Description : {highTickets['title']}")

def criticalTicketPriority():
    tickets = ticket.getTickets()
    for criticalTickets in tickets:
        if criticalTickets['priority'] == 4:
            print("."*10)
            print(criticalTickets['title'])  
            print(f"Description : {criticalTickets['title']}")

