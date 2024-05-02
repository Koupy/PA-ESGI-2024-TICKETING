import ticket
import menu.ticketMenu

def chooseCategory():
    api_category_names = ["stock", "truck", "warehouse", "service", "planning", "activity"]
    display_category_names = ["stocks", "camions", "entrepots", "services", "plannings", "activités"]
    category_map = dict(zip(api_category_names, display_category_names))
    ticket.displayChoices('category', category_map)
    
    menu.ticketMenu.categoryTicket()

def displayTicketsByCategory(category):
    tickets = ticket.getTickets()
    foundTickets = False
    ticket_list = []
    index = 1
    for ticket_item in tickets:
        if ticket_item['category'].lower() == category.lower():
            foundTickets = True
            ticket_list.append(ticket_item)
            print(f"\033[96m{index}. {ticket_item['title']}\033[0m")
            print(f"   Description : {ticket_item['description']}")
            index += 1

    return foundTickets, ticket_list

def stockTicket():
    found, tickets = displayTicketsByCategory("stock")
    if not found:
        print("Il n'y a pas de tickets dans la catégorie des stocks.")
        return
    selected_ticket = ticket.selectTicket(tickets)
    if selected_ticket:
        print(f"Vous avez sélectionné le ticket: {selected_ticket['title']}")

def truckTicket():
    found, tickets = displayTicketsByCategory("truck")
    if not found:
        print("Il n'y a pas de tickets dans la catégorie des camions.")
        return
    selected_ticket = ticket.selectTicket(tickets)
    if selected_ticket:
        print(f"Vous avez sélectionné le ticket: {selected_ticket['title']}")

def warehouseTicket():
    found, tickets = displayTicketsByCategory("warehouse")
    if not found:
        print("Il n'y a pas de tickets dans la catégorie des entrepôts.")
        return
    selected_ticket = ticket.selectTicket(tickets)
    if selected_ticket:
        print(f"Vous avez sélectionné le ticket: {selected_ticket['title']}")

def serviceTicket():
    found, tickets = displayTicketsByCategory("service")
    if not found:
        print("Il n'y a pas de tickets dans la catégorie des services.")
        return
    selected_ticket = ticket.selectTicket(tickets)
    if selected_ticket:
        print(f"Vous avez sélectionné le ticket: {selected_ticket['title']}")

def planningTicket():
    found, tickets = displayTicketsByCategory("planning")
    if not found:
        print("Il n'y a pas de tickets dans la catégorie des plannings.")
        return
    selected_ticket = ticket.selectTicket(tickets)
    if selected_ticket:
        print(f"Vous avez sélectionné le ticket: {selected_ticket['title']}")

def activityTicket():
    found, tickets = displayTicketsByCategory("activity")
    if not found:
        print("Il n'y a pas de tickets dans la catégorie des activités.")
        return
    selected_ticket = ticket.selectTicket(tickets)
    if selected_ticket:
        print(f"Vous avez sélectionné le ticket: {selected_ticket['title']}")
