class Message():
    def __init__(self, body, destination_id, id, source_id ):
        self.body = body
        self.destination_id = destination_id
        self.id = id
        self.source_id = source_id

    def ConverTostring(self):
        data = {
            "body": self.body,
            "destination_id": self.destination_id,
            "id": self.id,
            "source_id": self.source_id
        }
        return data
