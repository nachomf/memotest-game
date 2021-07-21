from game import Game
from element import Element
from player import Player

class GameInitializer():
    def disorder(self, elements):
        import random
        return random.sample(elements,len(elements))
    
    def initialize_elements(self):
        names = range(1, self.element_count + 1)

        values = []
        for value in range(1, int(self.element_count/2) + 1):
            values.append(value)
            values.append(value)
        #values = self.disorder(values)

        elements = []
        for name, value in zip(names,values):
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
            player_name = input("Player " + str(index) + " choose name: ")
            players.append(Player(player_name))

        return players

    def initialize(self):
        return Game(self.initialize_elements(), self.initialize_players())
