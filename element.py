class Element():
    def __init__(self, name, value):
        self.name = str(name)
        self.value = value

    def print(self, player, visible_names):
        name = ""
        make_visible = self.name in visible_names
        
        if make_visible:
            name = " "+self.value
        elif player.already_discover(self.value):
            name = " @"
        elif len(self.name) > 1:
            name = self.name
        else:
            name = " "+self.name

        print(" [ "+name+" ] ", end="")
      