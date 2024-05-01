import requests

def getTickets():
    url = 'http://localhost:5000/api/ticket/'
    response = requests.get(url)
    return response.json()

def seeTickets():
    tickets = getTickets()
    for ticket in tickets:
        print("\033[96m" + "."*10 + "\033[0m")
        print(ticket)
        # print(ticket['title'])  
        # print(f"Description : {ticket['title']}")  

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

def selectTicket(ticket_list):
    print("Entrez le numéro du ticket (0 pour revenir au menu)")
    while True:
        try:
            choice = int(input("Votre choix: "))
            if choice == 0:
                return None
            if 1 <= choice <= len(ticket_list):
                return ticket_list[choice - 1]
            else:
                print("Choix invalide. Veuillez entrer un numéro de ticket valide.")
        except ValueError:
            print("Veuillez entrer un nombre.")
