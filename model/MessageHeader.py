class MessageHeader():
    def __init__(self, authorization, destination_id, id, source_id):
        self.authorization = authorization
        self.destination_id = destination_id
        self.id = id
        self.source_id = source_id

    def sendMessageToApple(self):
        data = {
            "Destination-Id": self.destination_id, 
            "Source-Id": self.source_id, 
            "Content-Type": "application/json", 
            "id": self.id, 
            "Authorization": self.authorization
        }
        return data