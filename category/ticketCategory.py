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
    for ticket_item in tickets:
        if ticket_item['category'] == category:
            print("."*10)
            print(ticket_item['title'])
            print(f"Description : {ticket_item['description']}")
            print("Quel ticket souhaitez vous voir ?")

def stockTicket():
    displayTicketsByCategory("stock")

def truckTicket():
    displayTicketsByCategory("truck")

def warehouseTicket():
    displayTicketsByCategory("warehouse")

def serviceTicket():
    displayTicketsByCategory("service")

def planningTicket():
    displayTicketsByCategory("planning")

def activityTicket():
    displayTicketsByCategory("activity")