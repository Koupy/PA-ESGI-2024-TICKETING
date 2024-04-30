import requests

priority = ["faible", "moyen", "élevé", "critique"]
status = ["Ouvert", "En cours", "Résolu"]


def seeTicket():
  return "ticket"

def seeTickets():
  url = 'http://localhost:5000/api/ticket/'
  response = requests.get(url)
  print('Response Content:', response.text)


def choosePriority():
  print("Quel tickets souhaitez vous voir ?")
  for i in range(len(priority)):
    print(f"{i+1}. {priority[i]} (/nmb_tickets/)")

def chooseStatus():
  print("Quel tickets souhaitez vous voir ?")
  for i in range(len(status)):
    print(f"{i+1}. {status[i]} (/nmb_tickets/)")


