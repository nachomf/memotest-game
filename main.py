from game_initializer import GameInitializer

def main():
    game = GameInitializer(16,2).initialize()
    game.start()

    retry_game = input("new the game? Y/N  ")
    if(retry_game.upper() == "Y"):
        main()

main()
