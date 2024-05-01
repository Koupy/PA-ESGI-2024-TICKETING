import menu.ticketMenu
import ticket

def chooseCategory():
    api_category_names = ["stock", "truck", "warehouse", "service", "planning", "activity"]
    display_category_names = ["stocks", "camions", "entrepots", "services", "plannings", "activités"]
    category_map = dict(zip(api_category_names, display_category_names))
    ticket.displayChoices('category', category_map)
    
    menu.ticketMenu.categoryTicket()
