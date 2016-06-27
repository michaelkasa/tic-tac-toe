import sys
from PySide.QtCore import *
from PySide.QtGui import *

pics_by_choice = {-1:"Question_Mark.jpg",
                  0:"Courtney_C.jpg",
                  1:"Beebee.jpg"}
names_by_choice = {-1:"",
                   0:"Courtney",
                   1:"Beebee"}

class TicTacToeTile(QPushButton):
    def __init__(self, board, row, col):
        super(TicTacToeTile, self).__init__(board)
        self.board = board
        self.row = row
        self.col = col
        self.reset()

    def am_clicked(self, current_choice):
        if self.choice < 0:
            self.choice = current_choice
            self.setIcon(QIcon(pics_by_choice[current_choice]))
            winner = self.board.check_for_win()
            if not winner == False:
                x = 1
            else:
                self.board.lock_all_tiles()
            return True
        else:
            return False

    def reset(self):
        self.is_chosen = False
        self.choice = -1  # -1 for no choice
        self.setIcon(QIcon("Question_Mark.jpg"))
        self.setIconSize(QSize(180,180))

    def lock(self):
        self.is_chosen = True

    def get_choice(self):
        return self.choice


class TicTacToeBoard(QWidget):
    def __init__(self):
        super(TicTacToeBoard, self).__init__()

        self.current_choice = 0

        self.reset_btn = QPushButton("Reset", self)
        self.title_label = QLabel("Tic Tac Toe!", self)
        self.prompt_label = QLabel("Welcome to Tic Tac Toe!", self)

        self.tilesLayout = QGridLayout()
        self.tiles = []
        for i_row in range(3):
            for i_col in range(3):
                new_tile = TicTacToeTile(self, i_row, i_col)
                self.tiles.append(new_tile)
                self.tilesLayout.addWidget(new_tile,i_row,i_col)
                new_tile.clicked.connect(self.clicked_tile)

        self.messageAndResetLayout = QHBoxLayout()
        self.messageAndResetLayout.addWidget(self.prompt_label)
        self.messageAndResetLayout.addWidget(self.reset_btn)
        
        self.masterLayout = QVBoxLayout()
        self.masterLayout.addWidget(self.title_label)
        self.masterLayout.addLayout(self.messageAndResetLayout)
        self.masterLayout.addLayout(self.tilesLayout)
        
        self.setLayout(self.masterLayout)

        self.reset_btn.clicked.connect(self.reset)

    def clicked_tile(self):
        if self.sender().am_clicked(self.current_choice):
            self.current_choice = (self.current_choice + 1) % 2

    def reset(self):
        self.current_choice = 0
        for tile in self.tiles:
            tile.reset()

    def check_for_win(self):
        picks = [[],[],[]]
        for i_row in range(3):
            for i_col in range(3):
                i_tile = 3 * i_row + i_col
                picks[i_row].append(self.tiles[i_tile].get_choice())

        print(picks)
        
        for w in range(2):
            if [picks[0][0], picks[0][1], picks[0][2]] == [w]*3:
                return w
            elif [picks[1][0], picks[1][1], picks[1][2]] == [w]*3:
                return w
            elif [picks[2][0], picks[2][1], picks[2][2]] == [w]*3:
                return w
            elif [picks[0][0], picks[1][0], picks[2][0]] ==[w]*3:
                return w
            elif [picks[0][1], picks[1][1], picks[2][1]] == [w]*3:
                return w
            elif [picks[0][2], picks[1][2], picks[2][2]] == [w]*3:
                return w
            elif [picks[0][0], picks[1][1], picks[2][2]] == [w]*3:
                return w
            elif [picks[0][2], picks[1][1], picks[2][0]] == [w]*3:
                return w
            else:
                return False

    def lock_all_tiles(self):
        for tile in self.tiles:
            tile.lock()
        


# Create a QT application
app = QApplication(sys.argv)
tic_tac_toe = TicTacToeBoard()
tic_tac_toe.show()

# Enter Qt application main loop
app.exec_()
sys.exit()
