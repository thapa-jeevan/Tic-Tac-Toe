class Tic_Tac_Toe_State():
    def __init__(self, config=None):
        if config is None:
            self.config = [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
            ]
        else:
            self.config = config

    def is_terminal(self):
        win_states = [
            [self.config[0][0], self.config[0][1], self.config[0][2]],
            [self.config[1][0], self.config[1][1], self.config[1][2]],
            [self.config[2][0], self.config[2][1], self.config[2][2]],
            [self.config[0][0], self.config[1][0], self.config[2][0]],
            [self.config[0][1], self.config[1][1], self.config[2][1]],
            [self.config[0][2], self.config[1][2], self.config[2][2]],
            [self.config[0][0], self.config[1][1], self.config[2][2]],
            [self.config[2][0], self.config[1][1], self.config[0][2]],
        ]
        if [1, 1, 1] in win_states:
            return 1
        elif [-1, -1, -1] in win_states:
            return -1
        elif len(self.empty_cells()) == 0:
            return 0
        else:
            return False

    def clone_and_move(self, pos, value):
        clone = [row.copy() for row in self.config]
        clone[pos[0]][pos[1]] = value

        return Tic_Tac_Toe_State(clone)

    def empty_cells(self):
        return [[x, y] for x, row in enumerate(self.config) for y, cell in enumerate(row) if cell == 0]

    def valid_move(self, x, y):
        return True if [x, y] in self.empty_cells() else False

    def set_move(self, x, y, player):
        if self.valid_move(x, y):
            self.config[x][y] = player
            return True
        else:
            return False

    def set(self, x, y, player):
        self.config[x][y] = player

    def render(self):
        chars = lambda x: {-1: 'X', +1: 'O', 0: ' '}[x]
        game_state = [list(map(chars, row)) for row in self.config]
        print()
        print(' ' + str(game_state[0][0]) + ' | ' + str(game_state[0][1]) + ' | ' + str(game_state[0][2]))
        print('-----------')
        print(' ' + str(game_state[1][0]) + ' | ' + str(game_state[1][1]) + ' | ' + str(game_state[1][2]))
        print('-----------')
        print(' ' + str(game_state[2][0]) + ' | ' + str(game_state[2][1]) + ' | ' + str(game_state[2][2]))
        print()
