import sys
from PySide.QtCore import *
from PySide.QtGui import *

class TicTacToe(QWidget):
    def __init__(self):
        super(TicTacToe, self).__init__()

        self.reset_btn = QPushButton("Reset", self)
        self.title_label = QLabel("Tic Tac Toe!", self)
        self.prompt_label = QLabel("Welcome to Tic Tac Toe!", self)

        self.tilesLayout = QGridLayout()

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
tic_tac_toe = TicTacToe()
tic_tac_toe.show()

# Enter Qt application main loop
app.exec_()
sys.exit()
