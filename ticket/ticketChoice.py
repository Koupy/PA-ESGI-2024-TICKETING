import requests

def getTickets():
    url = 'http://localhost:5000/api/ticket/'
    response = requests.get(url)
    return response.json()

def updateTicketStatus(selectedTicket):
    url = f"http://localhost:5000/api/ticket/{selectedTicket['id']}"
    headers = {'Content-Type': 'application/json'}
    data = {
        'status': selectedTicket['status']
    }

    response = requests.put(url, json=data, headers=headers)

    if response.status_code == 200:
        return
    else:
        print(f"Failed to update ticket status: {response.status_code}")
        print("Response message:", response.text)
    
def seeTickets():
    tickets = getTickets()
    for ticket in tickets:
        print("\033[96m" + "."*10 + "\033[0m")
        print(ticket)
        # print(ticket['title'])  
        # print(f"Description : {ticket['title']}")  

def countTicketsByAttribute(tickets, attribute, valueMap):
    counts = {value: 0 for value in valueMap.values()}
    for ticket in tickets:
        ticketAttribute = ticket[attribute]

        if isinstance(ticketAttribute, str):
            ticketAttribute = ticketAttribute.lower()
        
        ticketAttribute = valueMap.get(ticketAttribute, ticketAttribute)

        if ticketAttribute in counts:
            counts[ticketAttribute] += 1
            
    return counts

def displayChoices(attribute, valueMap):
    tickets = getTickets()
    counts = countTicketsByAttribute(tickets, attribute, valueMap)
    print(f"Quels tickets souhaitez-vous voir ?")
    for i, (key, value) in enumerate(valueMap.items()):
        print(f"{i+1}. {value} ({counts.get(value, 0)})")

def selectTicket(ticketList):
    print("Entrez le numéro du ticket (0 pour revenir au menu)")
    while True:
        try:
            choice = int(input("Votre choix: "))
            if choice == 0:
                return None
            if 1 <= choice <= len(ticketList):
                return ticketList[choice - 1]
            else:
                print("Choix invalide. Veuillez entrer un numéro de ticket valide.")
        except ValueError:
            print("Veuillez entrer un nombre.")