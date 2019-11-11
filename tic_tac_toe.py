from random import randint
from tic_tac_toe_state import Tic_Tac_Toe_State
from minimax_ import *


def ai_turn_state_cost_alpha_beta(state: Tic_Tac_Toe_State):
    cells = state.empty_cells()
    if state.is_terminal() is not False:
        return
    max_step = [-1, -1]
    if len(cells) == 9:
        max_step[0], max_step[1] = randint(0, 2), randint(0, 2)
    else:
        max_step, _, _ = maximize_(state, -inf, inf, 0)

    state.set(*max_step, 1)
    state.render()


def human_turn(state: Tic_Tac_Toe_State):
    if state.is_terminal() is not False:
        return

    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    move = moves[int(input('Enter Move: '))]
    state.set_move(*move, -1)
    state.render()


def main():
    state = Tic_Tac_Toe_State()

    while not state.is_terminal():
        ai_turn_state_cost_alpha_beta(state)
        human_turn(state)

    state.render()
    terminal_value = state.is_terminal()
    print(terminal_value)
    if terminal_value == -1:
        print(f'Human turn [X]')
        print('YOU WIN!')
    elif terminal_value == 1:
        print(f'Computer turn [O]')
        print('YOU LOSE!')
    else:
        print('DRAW!')

    exit()


if __name__ == '__main__':
    main()
