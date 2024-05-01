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
    for ticket_item in tickets:
        if ticket_item['category'] == category:
            foundTickets = True
            print("\033[96m" + "."*10 + "\033[0m")
            print(ticket_item['title'])
            print(f"Description : {ticket_item['description']}")
            print("Quel ticket souhaitez vous voir ?")
    
    return foundTickets

def stockTicket():
    if not displayTicketsByCategory("stock"):
        print("Il n'y a pas de tickets dans la catégorie des stocks.")
        return
    
def truckTicket():
    if not displayTicketsByCategory("truck"):
        print("Il n'y a pas de tickets dans la catégorie des camions.")
        return

def warehouseTicket():
    if not displayTicketsByCategory("warehouse"):
        print("Il n'y a pas de tickets dans la catégorie des entrepôts.")
        return

def serviceTicket():
    if not displayTicketsByCategory("service"):
        print("Il n'y a pas de tickets dans la catégorie des services.")
        return

def planningTicket():
    if not displayTicketsByCategory("planning"):
        print("Il n'y a pas de tickets dans la catégorie des plannings.")
        return

def activityTicket():
    if not displayTicketsByCategory("activity"):
        print("Il n'y a pas de tickets dans la catégorie des activités.")
        return
