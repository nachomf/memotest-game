from player import Player
from game_initializer import GameInitializer

def main():
    game = GameInitializer(16,2).initialize()
    game.start()
    input("\n")

main()
