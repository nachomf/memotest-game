class Game:
    def __init__(self, elements, players):
        self.elements = elements
        self.players = players
        self.turn_number = 1

    def start(self):
        self.next_turn()

    def next_turn(self):
        print("Turn number: " + str(self.turn_number))
        self.print_elements()

    def print_elements(self):
        for index, element in enumerate(self.elements):
            if index%4 == 0: print("\n")
            element.print()