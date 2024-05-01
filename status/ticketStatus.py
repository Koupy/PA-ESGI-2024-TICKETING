import ticket

def chooseStatus():
    status_map = {1: "ouvert", 2: "en cours", 3: "résolu"}
    ticket.displayChoices('status', status_map)
