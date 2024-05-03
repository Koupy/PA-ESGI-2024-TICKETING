import requests
from datetime import datetime

def ticketAnswer(ticketId, userId, message):
    url = "http://localhost:5000/api/ticketresponse/"
    headers = {'Content-Type': 'application/json'}
    
    data = {
        'ticket_id': ticketId,
        'user_id': userId,
        'message': message,
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        try:
            return response.json()
        except ValueError:
            return "Response did not contain valid JSON."
    else:
        raise Exception(f"Erreur lors de la création de la réponse au ticket: {response.status_code} {response.text}")

def getTicketAnswers():
    url = f'http://localhost:5000/api/ticketresponse/'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed, Status Code: {response.status_code}")
        return []