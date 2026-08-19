from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import sys


class MockupWindow(QMainWindow):
    def __init__(self, content_widget=None):
        super().__init__()

        self.setFixedSize(320, 640)

        self.screen_widget = QWidget(self)
        self.screen_widget.setGeometry(30, 65, 260, 546) 
        self.screen_widget.setStyleSheet("""
            background-color: rgb(50, 50, 50);
            border-bottom-left-radius: 30px;
            border-bottom-right-radius: 30px;
        """)

        if content_widget:
            content_widget.setParent(self.screen_widget)
            content_widget.setGeometry(0, 0, 260, 546)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Fundo branco
        painter.setBrush(QBrush(QColor(255, 255, 255)))
        painter.drawRect(self.rect())

        # Corpo
        painter.setBrush(QBrush(QColor(0, 0, 0)))
        painter.drawRoundedRect(QRect(20, 20, 280, 600), 40, 40)

        # Ecrã cinza desenhado
        painter.setBrush(QBrush(QColor(50, 50, 50)))
        painter.drawRoundedRect(QRect(30, 31, 260, 576), 30, 30)

        # Notch desenhada POR ÚLTIMO (fica sempre visível)
        painter.setBrush(QBrush(QColor(0, 0, 0)))
        painter.drawRoundedRect(QRect(122, 42, 80, 20), 10, 10)

        # Botões
        painter.drawRoundedRect(QRect(292, 170, 10, 80), 10, 10)
        painter.drawRoundedRect(QRect(17, 160, 10, 50), 10, 10)
        painter.drawRoundedRect(QRect(17, 215, 10, 50), 10, 10)

        painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MockupWindow()
    window.show()
    sys.exit(app.exec_())