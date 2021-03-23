from tictactoe import initial_state, player,actions, result, winner, terminal, utility, minimax

board = [['X',None, None],['X','O',None],['O','O','X']]

def main():
    print(result(board))

main()

