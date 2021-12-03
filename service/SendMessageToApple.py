from model.MessageHeader import MessageHeader
import json

class SendMessage():
    authorization = "Bearer eyJhbGciOiJIUzI1NiIs.<truncated>"
    destination_id = "DEF123GH-b0ad <truncated>"
    id = "3608321f-<truncated>"
    source_id = "urn:mbid:AQ/quv4JIAJyVALyKtW <truncated>"
    header = MessageHeader(authorization, destination_id, id, source_id).sendMessageToApple()
    print(header)
    dataJson = json.dumps(header)
    print(dataJson)