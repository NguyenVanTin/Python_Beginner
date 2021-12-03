from Parrot import Parrot

class main:
    tin = Parrot("Tin", 23)
    print("Tin is a {}".format(tin.__class__.species))
    print("{} is {} years old.".format(tin.name, tin.age))
    print(tin.getJson())
    nam = Parrot("Nam", 24)
    print("{} is {} years old.".format(nam.name, nam.age))