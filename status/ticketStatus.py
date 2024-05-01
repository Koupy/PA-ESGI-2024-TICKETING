import ticket
import menu.ticketMenu

def chooseStatus():
    status_map = {1: "ouvert", 2: "en cours", 3: "résolu"}
    ticket.displayChoices('status', status_map)
    menu.ticketMenu.statusTicket()

def displayTicketsByStatus(status):
    tickets = ticket.getTickets()
    for ticket_item in tickets:
        if ticket_item['status'] == status:
            print("."*10)
            print(ticket_item['title'])
            print(f"Description : {ticket_item['description']}")
            print("Quel ticket souhaitez vous voir ?")

def openTicket():
    displayTicketsByStatus("Ouvert")

def ongoingticket():
    displayTicketsByStatus("En cours")

def closedTicket():
    displayTicketsByStatus("Fermé")