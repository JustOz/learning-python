import sys, random




"""
To play:
    >>>> python [path-to-file] [rock/paper/scissors]
"""


def game(decision: str, moves: list[str]) -> int:
    """
    Args:
        decision: str
        moves: list[str] ~ ["rock", "paper", "scissors"]

    Returns:
        -1 >> lose
        0 >> draw
        1 >> win
    """
    game_decision = random.randrange(0, 3)
    print("The game picked: {}".format(moves[game_decision]))
    player_decision = moves.index(decision)
    if player_decision == 1:
        if game_decision == 0:
            return 1
        elif game_decision == 1:
            return 0
    elif player_decision == 2:
        if game_decision == 1:
            return 1
        elif game_decision == 2:
            return 0
    else:
        if game_decision == 2:
            return 1
        if game_decision == 0:
            return 0
    return -1


def main() -> int:
    moves = ["rock", "paper", "scissors"]
    try:
        decision = sys.argv[1]
        if (str(decision) in moves):
            result = game(decision, moves)
            if (result == 1):
                print("You've won!")
            elif (result == 0):
                print("It's a draw!")
            else:
                print("You've lost.")
        else:
            print("The decision you've entered does not exist, the moves are:\n 1. rock\n 2. paper\n 3. scissors")

    except:
        print("You didn't enter anything.")


    return 0




if __name__ == "__main__":
    main()
