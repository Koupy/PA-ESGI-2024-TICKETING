import requests
from datetime import datetime

def ticketAnswer(ticket_id, user_id, message, created_at, updated_at):
    url = "http://localhost:5000/api/ticketresponse/"
    headers = {'Content-Type': 'application/json'}
    
    data = {
        'ticket_id': ticket_id,
        'user_id': user_id,
        'message': message,
        'created_at': created_at.strftime('%Y-%m-%d %H:%M:%S'),
        'updated_at': updated_at.strftime('%Y-%m-%d %H:%M:%S') if updated_at else None
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        try:
            return response.json()
        except ValueError:
            return "Response did not contain valid JSON."
    else:
        raise Exception(f"Erreur lors de la création de la réponse au ticket: {response.status_code} {response.text}")


# @app.route('/api/ticketresponse/', methods=['POST'])
# def create_ticketresponse():
#     data = request.json
#     response, status_code = TicketResponseService.create_ticketresponse(data)
#     return response, status_code

# @app.route('/api/ticketresponse/', methods=['GET'])
# def get_ticketresponses():
#     response, status_code = TicketResponseService.get_ticketresponses()
#     return jsonify(response), status_code

# @app.route('/api/ticketresponse/<int:id>', methods=['GET'])
# def get_ticketresponse(id):
#     response, status_code = TicketResponseService.get_ticketresponse(id)
#     return jsonify(response), status_code

# @app.route('/api/ticketresponse/<int:id>', methods=['PUT'])
# def update_ticketresponse(id):
#     data = request.json
#     response, status_code = TicketResponseService.update_ticketresponse(id, data)
#     return jsonify(response), status_code

# @app.route('/api/ticketresponse/<int:id>', methods=['DELETE'])
# def delete_ticketresponse(id):
#     response, status_code = TicketResponseService.delete_ticketresponse(id)
#     return jsonify(response), status_code

# CREATE TABLE IF NOT EXISTS `TicketResponse` (
#     `id` INT AUTO_INCREMENT PRIMARY KEY,
#     `ticket_id` INT NOT NULL,
#     `user_id` INT NOT NULL,
#     `message` TEXT NOT NULL,
#     `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     `updated_at` DATE,
#     FOREIGN KEY (ticket_id) REFERENCES Ticket(id),
#     FOREIGN KEY (user_id) REFERENCES User(id)
# );