class Game:
    def __init__(self, elements, players):
        self.elements = elements
        self.players = players

    def start(self):
        turn = 1
        end_game = False
        while(not end_game):
            turn_player = self.get_player(turn)
            print("Turn number: " + str(turn) + " play player name: " + turn_player.name)
            self.play_turn(turn_player)
            end_game = self.is_win(turn_player)
            turn = turn + 1
        print("Congratulations " + turn_player.name + " you Won!!")

    def get_player(self, turn):
        return self.players[(turn -1)%len(self.players)]

    def play_turn(self, player):
        turn_finish = False
        while(not turn_finish):
            self.print_elements(player)
            user_input = self.read_user_input()
            #TODO add exceptions where the number is wrong
            first_element = self.get_element(user_input[0])
            second_element = self.get_element(user_input[-1])
            if first_element.value == second_element.value:
                print("Well done you assert!!")
                player.remember_value(first_element.value)
                turn_finish = self.is_win(player)
            else:
                print("Sorry try again in your next turn!!")
                turn_finish = True
            

    def is_win(self, player): return player.has_all_values(len(self.elements)/2)

    def get_element(self,name): 
        return next(e for e in self.elements if e.name == name)

    def read_user_input(self):
        #TODO Add handlers
        separator = ","
        player_input = input("\nChoose 2 element separate by "+ separator +": ")
        return player_input.split(separator)

    def print_elements(self, player):
        for index, element in enumerate(self.elements):
            if index%4 == 0: print("\n")
            element.print(player)