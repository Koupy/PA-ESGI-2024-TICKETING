import ticket
import menu.ticketMenu

def choosePriority():
    priority_map = {1: "faible", 2: "moyen", 3: "élevé", 4: "critique"}
    ticket.displayChoices('priority', priority_map)
    menu.ticketMenu.priorityTicket()

def displayTicketsByPriority(priority):
    tickets = ticket.getTickets()
    foundTickets = False
    ticket_list = []
    for index, ticket_item in enumerate(tickets, start=1):
        if ticket_item['priority'] == priority:
            foundTickets = True
            ticket_list.append(ticket_item)
            print(f"\033[96m{index}. {ticket_item['title']}\033[0m")
            print(f"   Description : {ticket_item['description']}")

    return foundTickets, ticket_list


def lowTicketPriority():
    found, tickets = displayTicketsByPriority(1)
    if not found:
        print("Il n'y a pas de tickets de priorité faible.")
        return
    selected_ticket = ticket.selectTicket(tickets)
    if selected_ticket:
        print(f"Vous avez sélectionné le ticket: {selected_ticket['title']} - {selected_ticket['description']}")

def midTicketPriority():
    found, tickets = displayTicketsByPriority(2)
    if not found:
        print("Il n'y a pas de tickets de priorité moyenne.")
        return
    selected_ticket = ticket.selectTicket(tickets)
    if selected_ticket:
        print(f"Vous avez sélectionné le ticket: {selected_ticket['title']} - {selected_ticket['description']}")

def highTicketPriority():
    found, tickets = displayTicketsByPriority(3)
    if not found:
        print("Il n'y a pas de tickets de priorité élevée.")
        return
    selected_ticket = ticket.selectTicket(tickets)
    if selected_ticket:
        print(f"Vous avez sélectionné le ticket: {selected_ticket['title']} - {selected_ticket['description']}")

def criticalTicketPriority():
    found, tickets = displayTicketsByPriority(4)
    if not found:
        print("Il n'y a pas de tickets de priorité critique.")
        return
    selected_ticket = ticket.selectTicket(tickets)
    if selected_ticket:
        print(f"Vous avez sélectionné le ticket: {selected_ticket['title']} - {selected_ticket['description']}")