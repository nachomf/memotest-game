from player import Player

class Element:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def print(self):
        if self.name > 9:
            print(" [ "+str(self.name)+" ] ", end="")
        else:
            print(" [  "+str(self.name)+" ] ", end="")

class MemotestGameBuilder:
    def disorder(self, elements):
        import random
        return random.sample(elements,len(elements))
    
    def initialize_elements(self):
        names = range(1, self.element_count + 1)

        values = []
        for value in range(1, int(self.element_count/2) + 1):
            values.append(value)
            values.append(value)
        values = self.disorder(values)

        elements = []
        for name, value in zip(names,self.disorder(values)):
            elements.append(Element(name,value))

        return elements
    
    def is_invalid_game(self,element_count, player_count):
        #Complete with more assertions
        return (element_count%2 != 0) and (player_count > 0)
    
    def __init__(self, element_count, player_count):
        if self.is_invalid_game(element_count,player_count): return print("Element count should be even")
    
        self.element_count = element_count
        self.player_count = player_count
    
    def initialize_players(self):
        players = []
        for index in range(1, self.player_count + 1):
            player_name = input("Player " + str(index) + " choose name:")
            players.append(Player(player_name))

        return players

    def build(self):
        return MemotestGame(self.initialize_elements(), self.initialize_players())


class MemotestGame:
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


def main():
    game = MemotestGameBuilder(16,2).build()
    game.start()
    input("\n")

main()
