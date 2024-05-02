import ticket.ticketChoice
import menu.ticketMenu

def chooseStatus():
    statusMap = {1: "ouvert", 2: "en cours", 3: "resolu"}
    ticket.ticketChoice.displayChoices('status', statusMap)
    menu.ticketMenu.statusTicket()

def displayTicketsByStatus(status):
    tickets = ticket.ticketChoice.getTickets()
    foundTickets = False
    ticketList = []
    index = 1
    for ticketItem in tickets:
        if ticketItem['status'].lower() == status.lower():
            foundTickets = True
            ticketList.append(ticketItem)
            print(f"\033[96m{index}. {ticketItem['title']}\033[0m")
            print(f"   Description : {ticketItem['description']}")
            index += 1

    return foundTickets, ticketList

def openTicket():
    found, tickets = displayTicketsByStatus("Ouvert")
    if not found:
        print("Il n'y a pas de tickets ouverts.")
        return
    selectedTicket = ticket.ticketChoice.selectTicket(tickets)
    if selectedTicket:
        print(f"Vous avez sélectionné le ticket: {selectedTicket['title']} - {selectedTicket['description']}")

def ongoingTicket():
    found, tickets = displayTicketsByStatus("En cours")
    if not found:
        print("Il n'y a pas de tickets en cours.")
        return
    selectedTicket = ticket.ticketChoice.selectTicket(tickets)
    if selectedTicket:
        print(f"Vous avez sélectionné le ticket: {selectedTicket['title']} - {selectedTicket['description']}")

def closedTicket():
    found, tickets = displayTicketsByStatus("Resolu")
    if not found:
        print("Il n'y a pas de tickets résolus.")
        return
    selectedTicket = ticket.ticketChoice.selectTicket(tickets)
    if selectedTicket:
        print(f"Vous avez sélectionné le ticket: {selectedTicket['title']} - {selectedTicket['description']}")
