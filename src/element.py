class Element():
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def print(self):
        if self.name > 9:
            print(" [ "+str(self.name)+" ] ", end="")
        else:
            print(" [  "+str(self.name)+" ] ", end="")