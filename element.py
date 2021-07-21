class Element():
    def __init__(self, name, value):
        self.name = str(name)
        self.value = str(value)

    def print(self, player):
        name = ""
        
        if (player.already_discover(self.value)):
            name = " X"
        elif len(self.name) > 1:
            name = self.name
        else:
            name = " "+self.name

        print(" [ "+name+" ] ", end="")
      