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
    print(f"Quels tickets souhaitez-vous voir ?")
    for i, (key, value) in enumerate(value_map.items()):
        print(f"{i+1}. {value} ({counts.get(value, 0)})")