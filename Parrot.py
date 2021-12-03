class Parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getJson(self):
        data = {
            "name": self.name,
            "age": self.age
        }
        return data

