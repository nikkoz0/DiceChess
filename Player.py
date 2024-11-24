from PyQt6.QtWidgets import QDialog
from PyQt6 import uic

PLAYER_WHITE = []
PLAYER_BLACK = []


class Player(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui/Player.ui', self)
        self.Ok_Button.clicked.connect(self.ok)
        self.Cancel_Button.clicked.connect(self.cancel)

    def ok(self):
        if self.White_name.text() and self.Black_name.text():
            if self.White_name.text() != self.Black_name.text():
                PLAYER_WHITE.append(self.White_name.text())
                PLAYER_BLACK.append(self.Black_name.text())
                self.close()
            else:
                self.statusBar().showMessage('Имена должны быть разными')

    def cancel(self):
        self.close()



