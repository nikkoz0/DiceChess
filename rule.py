from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic


class Rule(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui/rule.ui', self)
        self.setFixedSize(300, 300)
        text = ('Игроки по-очереди кидают 3 кости,\n'
                'на которых изображены шахматные фигуры.\n'
                'Игрок может сходить только теми фигурами,\n'
                'которые изображены на костях.\n'
                'Цель- срубить вражеского короля.\n'
                'В остольном, правила, как в обычных шаматах.\n')
        self.label.setText(text)
