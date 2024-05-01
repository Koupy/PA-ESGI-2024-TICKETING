import ticket
import menu.ticketMenu

def chooseStatus():
    status_map = {1: "ouvert", 2: "en cours", 3: "resolu"}
    ticket.displayChoices('status', status_map)
    menu.ticketMenu.statusTicket()

def displayTicketsByStatus(status):
    tickets = ticket.getTickets()
    foundTickets = False
    ticket_list = []
    for index, ticket_item in enumerate(tickets, start=1):
        if ticket_item['status'].lower() == status.lower():
            foundTickets = True
            ticket_list.append(ticket_item)
            print(f"\033[96m{index}. {ticket_item['title']}\033[0m")
            print(f"   Description : {ticket_item['description']}")

    return foundTickets, ticket_list

def openTicket():
    found, tickets = displayTicketsByStatus("Ouvert")
    if not found:
        print("Il n'y a pas de tickets ouverts.")
        return
    selected_ticket = ticket.selectTicket(tickets)
    if selected_ticket:
        print(f"Vous avez sélectionné le ticket: {selected_ticket['title']} - {selected_ticket['description']}")

def ongoingTicket():
    found, tickets = displayTicketsByStatus("En cours")
    if not found:
        print("Il n'y a pas de tickets en cours.")
        return
    selected_ticket = ticket.selectTicket(tickets)
    if selected_ticket:
        print(f"Vous avez sélectionné le ticket: {selected_ticket['title']} - {selected_ticket['description']}")

def closedTicket():
    found, tickets = displayTicketsByStatus("Resolu")
    if not found:
        print("Il n'y a pas de tickets résolus.")
        return
    selected_ticket = ticket.selectTicket(tickets)
    if selected_ticket:
        print(f"Vous avez sélectionné le ticket: {selected_ticket['title']} - {selected_ticket['description']}")
