import sys
from PySide.QtCore import *
from PySide.QtGui import *

class TicTacToeTile(QPushButton):
    def __init__(self, parent, row, col):
        super(TicTacToeTile, self).__init__(parent)
        self.row = row
        self.col = col
        self.setIcon(QIcon("Beebee.jpg"))
        self.setIconSize(QSize(180,180))

class TicTacToeBoard(QWidget):
    def __init__(self):
        super(TicTacToeBoard, self).__init__()

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

        self.messageAndResetLayout = QHBoxLayout()
        self.messageAndResetLayout.addWidget(self.prompt_label)
        self.messageAndResetLayout.addWidget(self.reset_btn)
        
        self.masterLayout = QVBoxLayout()
        self.masterLayout.addWidget(self.title_label)
        self.masterLayout.addLayout(self.messageAndResetLayout)
        self.masterLayout.addLayout(self.tilesLayout)
        
        self.setLayout(self.masterLayout)


# Create a QT application
app = QApplication(sys.argv)
tic_tac_toe = TicTacToeBoard()
tic_tac_toe.show()

# Enter Qt application main loop
app.exec_()
sys.exit()
