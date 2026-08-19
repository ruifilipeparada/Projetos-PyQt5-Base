# display mockup iphone 

from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

class MockupWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(320, 640)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        central_widget.setLayout(layout)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Fundo branco
        painter.setBrush(QBrush(QColor(255, 255, 255)))
        painter.drawRect(self.rect())

        # Corpo do iPhone 
        painter.setBrush(QBrush(QColor(0, 0, 0)))
        body_rect = QRect(20, 20, 280, 600)
        painter.drawRoundedRect(body_rect, 40, 40)

        # Ecrã cinza escuro 
        painter.setBrush(QBrush(QColor(50, 50, 50)))
        screen_rect = QRect(30, 31, 260, 576)
        painter.drawRoundedRect(screen_rect, 30, 30)

        # Câmara frontal 
        painter.setBrush(QBrush(QColor(0, 0, 0)))
        dynamic_island_rect = QRect(122, 42, 80, 20) 
        painter.drawRoundedRect(dynamic_island_rect, 10, 10)

        # Botão ligar/desligar
        painter.setBrush(QBrush(QColor(0, 0, 0)))
        dynamic_island_rect = QRect(292, 170, 10, 80) 
        painter.drawRoundedRect(dynamic_island_rect, 10, 10)

        # Botão +som
        painter.setBrush(QBrush(QColor(0, 0, 0)))
        dynamic_island_rect = QRect(17, 160, 10, 50) 
        painter.drawRoundedRect(dynamic_island_rect, 10, 10)

        # Botão -som
        painter.setBrush(QBrush(QColor(0, 0, 0)))
        dynamic_island_rect = QRect(17, 215, 10, 50) 
        painter.drawRoundedRect(dynamic_island_rect, 10, 10)

        painter.end()

if __name__ == "__main__":
    app = QApplication([])
    window = MockupWindow()
    window.show()
    app.exec_()

