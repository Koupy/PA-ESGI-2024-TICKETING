import ticket.ticketChoice
import ticket.ticketAction
import menu.ticketMenu

def choosePriority():
    priorityMap = {1: "faible", 2: "moyen", 3: "élevé", 4: "critique"}
    ticket.ticketChoice.displayChoices('priority', priorityMap)
    menu.ticketMenu.priorityTicket()

def displayTicketsByPriority(priority):
    tickets = ticket.ticketChoice.getTickets()
    foundTickets = False
    ticketList = []
    index = 1
    for ticketItem in tickets:
        if ticketItem['priority'] == priority:
            foundTickets = True
            ticketList.append(ticketItem)
            print(f"\033[96m{index}. {ticketItem['title']}\033[0m")
            print(f"   Description : {ticketItem['description']}")
            index += 1

    return foundTickets, ticketList

def lowTicketPriority():
    found, tickets = displayTicketsByPriority(1)
    if not found:
        print("Il n'y a pas de tickets de priorité faible.")
        return
    selectedTicket = ticket.ticketChoice.selectTicket(tickets)
    if selectedTicket:
        print(f"Vous avez sélectionné le ticket: {selectedTicket['title']}")
        ticket.ticketAction.ticketActionMenu(selectedTicket)


def midTicketPriority():
    found, tickets = displayTicketsByPriority(2)
    if not found:
        print("Il n'y a pas de tickets de priorité moyenne.")
        return
    selectedTicket = ticket.ticketChoice.selectTicket(tickets)
    if selectedTicket:
        print(f"Vous avez sélectionné le ticket: {selectedTicket['title']}")
        ticket.ticketAction.ticketActionMenu(selectedTicket)


def highTicketPriority():
    found, tickets = displayTicketsByPriority(3)
    if not found:
        print("Il n'y a pas de tickets de priorité élevée.")
        return
    selectedTicket = ticket.ticketChoice.selectTicket(tickets)
    if selectedTicket:
        print(f"Vous avez sélectionné le ticket: {selectedTicket['title']}")
        ticket.ticketAction.ticketActionMenu(selectedTicket)

def criticalTicketPriority():
    found, tickets = displayTicketsByPriority(4)
    if not found:
        print("Il n'y a pas de tickets de priorité critique.")
        return
    selectedTicket = ticket.ticketChoice.selectTicket(tickets)
    if selectedTicket:
        print(f"Vous avez sélectionné le ticket: {selectedTicket['title']}")
        ticket.ticketAction.ticketActionMenu(selectedTicket)