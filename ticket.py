import requests
import menu.ticketMenu
import menu

priority = ["Faible", "Moyen", "Élevé", "Critique"]
status = ["Ouvert", "En cours", "Résolu"]
category = ["Stocks", "Camions", "Entrepots", "Services", "Plannings", "Activités"]

def getTickets():
  url = 'http://localhost:5000/api/ticket/'
  response = requests.get(url)
  return response

def seeTickets():
  response = getTickets()
  print('Response Content:', response.text)

def chooseCategory():
  getTickets()
  print("Quel tickets souhaitez vous voir ?")
  for i in range(len(category)):
    print(f"{i+1}. {category[i]} (/nmb_tickets/)")

  menu.ticketMenu.categoryTicket()
    
  











def choosePriority():
  print("Quel tickets souhaitez vous voir ?")
  for i in range(len(priority)):
    print(f"{i+1}. {priority[i]} (/nmb_tickets/)")

def chooseStatus():
  print("Quel tickets souhaitez vous voir ?")
  for i in range(len(status)):
    print(f"{i+1}. {status[i]} (/nmb_tickets/)")


