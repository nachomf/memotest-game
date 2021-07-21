class Game:
    def __init__(self, elements, players):
        self.elements = elements
        self.players = players

    def start(self):
        turn = 1
        end_game = False
        while(not end_game):
            turn_player = self.get_player(turn)
            print("Turn number: " + str(turn) + " player name: " + turn_player.name)
            self.play_turn(turn_player)
            end_game = self.is_win(turn_player)
            turn = turn + 1
        print("Congratulations " + turn_player.name + " you Won!!")

    def get_player(self, turn):
        return self.players[(turn -1)%len(self.players)]

    def play_turn(self, player):
        turn_finish = False
        while(not turn_finish):
            self.print_elements(player,[])
            #TODO add exceptions where the number is wrong
            first_element = self.select_value()
            self.print_elements(player,[first_element.name])
            second_element = self.select_value()
            self.print_elements(player,[first_element.name,second_element.name])

            if first_element.value == second_element.value:
                print("\nWell done you assert!!")
                player.remember_value(first_element.value)
                turn_finish = self.is_win(player)
            else:
                print("\nSorry try again in your next turn!!")
                input("next player, are you ready? press key..")
                turn_finish = True
            

    def select_value(self): return self.get_element(input("\nChoose element: "))

    def is_win(self, player): return player.has_all_values(len(self.elements)/2)

    def get_element(self,name): 
        return next(e for e in self.elements if e.name == name)

    def print_elements(self, player, visible_inputs):
        for index, element in enumerate(self.elements):
            if index%4 == 0: print("\n")
            element.print(player, visible_inputs)