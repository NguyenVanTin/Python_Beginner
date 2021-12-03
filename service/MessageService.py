from model.Message import Message

class MessageService():
    m = Message("1", "2", "3", "4", "5", "6").ConverTostring()
    print(m)