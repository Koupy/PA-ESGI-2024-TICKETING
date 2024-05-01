import ticket
import menu.ticketMenu

def chooseStatus():
    status_map = {1: "ouvert", 2: "en cours", 3: "resolu"}
    ticket.displayChoices('status', status_map)
    menu.ticketMenu.statusTicket()

def displayTicketsByStatus(status):
    tickets = ticket.getTickets()
    foundTickets = False
    for ticket_item in tickets:
        if ticket_item['status'] == status:
            foundTickets = True
            print("\033[96m" + "."*10 + "\033[0m")
            print(ticket_item['title'])
            print(f"Description : {ticket_item['description']}")
            print("Quel ticket souhaitez vous voir ?")
    
    return foundTickets

def openTicket():
    if not displayTicketsByStatus("Ouvert"):
        print("Il n'y a pas de tickets ouverts.")
        return

def ongoingTicket():
    if not displayTicketsByStatus("En cours"):
        print("Il n'y a pas de tickets en cours.")
        return

def closedTicket():
    if not displayTicketsByStatus("Resolu"):
        print("Il n'y a pas de tickets résolus.")
        return
