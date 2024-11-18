from PyQt6.QtWidgets import QMainWindow, QLabel


class End(QMainWindow):
    def __init__(self, winner):
        super().__init__()
        self.label = QLabel(self)
        self.setFixedSize(300, 300)
        if winner == 1:
            text = ('Выйграли белые')
        else:
            text = ('Выйграли чёрные')
        self.label.setText(text)
        self.setWindowTitle('Конец')
