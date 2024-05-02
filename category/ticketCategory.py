import ticket
import menu.ticketMenu

def chooseCategory():
    apiCategoryNames = ["stock", "truck", "warehouse", "service", "planning", "activity"]
    displayCategoryNames = ["stocks", "camions", "entrepots", "services", "plannings", "activités"]
    categoryMap = dict(zip(apiCategoryNames, displayCategoryNames))
    ticket.displayChoices('category', categoryMap)
    
    menu.ticketMenu.categoryTicket()

def displayTicketsByCategory(category):
    tickets = ticket.getTickets()
    foundTickets = False
    ticketList = []
    index = 1
    for ticketItem in tickets:
        if ticketItem['category'].lower() == category.lower():
            foundTickets = True
            ticketList.append(ticketItem)
            print(f"\033[96m{index}. {ticketItem['title']}\033[0m")
            print(f"   Description : {ticketItem['description']}")
            index += 1

    return foundTickets, ticketList

def stockTicket():
    found, tickets = displayTicketsByCategory("stock")
    if not found:
        print("Il n'y a pas de tickets dans la catégorie des stocks.")
        return
    selectedTicket = ticket.selectTicket(tickets)
    if selectedTicket:
        print(f"Vous avez sélectionné le ticket: {selectedTicket['title']}")

def truckTicket():
    found, tickets = displayTicketsByCategory("truck")
    if not found:
        print("Il n'y a pas de tickets dans la catégorie des camions.")
        return
    selectedTicket = ticket.selectTicket(tickets)
    if selectedTicket:
        print(f"Vous avez sélectionné le ticket: {selectedTicket['title']}")

def warehouseTicket():
    found, tickets = displayTicketsByCategory("warehouse")
    if not found:
        print("Il n'y a pas de tickets dans la catégorie des entrepôts.")
        return
    selectedTicket = ticket.selectTicket(tickets)
    if selectedTicket:
        print(f"Vous avez sélectionné le ticket: {selectedTicket['title']}")

def serviceTicket():
    found, tickets = displayTicketsByCategory("service")
    if not found:
        print("Il n'y a pas de tickets dans la catégorie des services.")
        return
    selectedTicket = ticket.selectTicket(tickets)
    if selectedTicket:
        print(f"Vous avez sélectionné le ticket: {selectedTicket['title']}")

def planningTicket():
    found, tickets = displayTicketsByCategory("planning")
    if not found:
        print("Il n'y a pas de tickets dans la catégorie des plannings.")
        return
    selectedTicket = ticket.selectTicket(tickets)
    if selectedTicket:
        print(f"Vous avez sélectionné le ticket: {selectedTicket['title']}")

def activityTicket():
    found, tickets = displayTicketsByCategory("activity")
    if not found:
        print("Il n'y a pas de tickets dans la catégorie des activités.")
        return
    selectedTicket = ticket.selectTicket(tickets)
    if selectedTicket:
        print(f"Vous avez sélectionné le ticket: {selectedTicket['title']}")
