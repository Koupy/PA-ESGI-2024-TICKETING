import requests
import menu.ticketMenu

def getTickets():
    url = 'http://localhost:5000/api/ticket/'
    response = requests.get(url)
    return response.json()

def seeTickets():
    tickets = getTickets()
    for ticket in tickets:
        print("."*10)
        print(ticket['title'])  
        print(f"Description : {ticket['title']}")  

def countTicketsByAttribute(tickets, attribute, value_map):
    counts = {value: 0 for value in value_map.values()}
    for ticket in tickets:
        ticket_attribute = ticket[attribute]

        if isinstance(ticket_attribute, str):
            ticket_attribute = ticket_attribute.lower()
        
        ticket_attribute = value_map.get(ticket_attribute, ticket_attribute)

        if ticket_attribute in counts:
            counts[ticket_attribute] += 1
            
    return counts

def displayChoices(attribute, value_map):
    tickets = getTickets()
    counts = countTicketsByAttribute(tickets, attribute, value_map)
    print(f"Quels tickets souhaitez-vous voir pour {attribute} ?")
    for i, (key, value) in enumerate(value_map.items()):
        print(f"{i+1}. {value} ({counts.get(value, 0)} tickets)")

def chooseCategory():
    api_category_names = ["stock", "truck", "warehouse", "service", "planning", "activity"]
    display_category_names = ["stocks", "camions", "entrepots", "services", "plannings", "activités"]
    category_map = dict(zip(api_category_names, display_category_names))
    displayChoices('category', category_map)

def choosePriority():
    priority_map = {1: "faible", 2: "moyen", 3: "élevé", 4: "critique"}
    displayChoices('priority', priority_map)

def chooseStatus():
    status_map = {1: "ouvert", 2: "en cours", 3: "résolu"}
    displayChoices('status', status_map)
