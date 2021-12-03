from Parrot import Parrot
from model.Message import Message
from service.MessageService import MessageService

class main:
    tin = Parrot("Tin", 23)
    print("Tin is a {}".format(tin.__class__.species))
    print("{} is {} years old.".format(tin.name, tin.age))
    print(tin.getJson())
    nam = Parrot("Nam", 24)
    print("{} is {} years old.".format(nam.name, nam.age))

    m = Message("1", "2", "3", "4", "1", "2").ConverTostring()

    msgService = MessageService()
    print(m)
    nam = Parrot("Nam", 24)
    print("{} is {} years old.".format(nam.name, nam.age))
    nam = Parrot("Coca", 5)
    print("{} is {} years old.".format(nam.name, nam.age))

    m = Message("1", "2", "3", "4").ConverTostring()
    print(m)
