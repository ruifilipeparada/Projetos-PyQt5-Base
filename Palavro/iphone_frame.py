from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDesktopWidget
import sys

class MockupWindow(QMainWindow):
    def __init__(self, content_widget=None):
        super().__init__()

        # --- DETETAR O TAMANHO DO ECRÃ ---
        ecran = QDesktopWidget().screenGeometry()
        largura_ecran = ecran.width()
        altura_ecran = ecran.height()

        # A altura da janela vai ser 85% do teu ecrã
        altura_janela = int(altura_ecran * 0.85)

        # Calcular a escala com base na altura
        self.scale = altura_janela / 640.0

        # A largura da janela abraça perfeitamente o telemóvel
        largura_janela = int(320 * self.scale)

        # Definir o tamanho fixo da janela
        self.setFixedSize(largura_janela, altura_janela)
        self.setWindowTitle("Mockup iPhone")

        # --- NOVO: CALCULAR AS COORDENADAS PARA CENTRAR ---
        pos_x = int((largura_ecran - largura_janela) / 2)
        pos_y = int((altura_ecran - altura_janela) / 2)
        
        # Mover a janela para o centro exato do ecrã
        self.move(pos_x, pos_y)

        # --- CRIAR A ÁREA DO ECRÃ INTERNO ---
        self.screen_widget = QWidget(self)
        self.screen_widget.setGeometry(
            int(30 * self.scale), 
            int(65 * self.scale), 
            int(260 * self.scale), 
            int(546 * self.scale)
        )
        
        # Ajustar as bordas arredondadas do ecrã com base na escala
        radius = int(30 * self.scale)
        self.screen_widget.setStyleSheet(f"""
            background-color: rgb(50, 50, 50);
            border-bottom-left-radius: {radius}px;
            border-bottom-right-radius: {radius}px;
        """)

        if content_widget:
            content_widget.setParent(self.screen_widget)
            content_widget.setGeometry(0, 0, int(260 * self.scale), int(546 * self.scale))

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Escalar o desenho do QPainter
        painter.scale(self.scale, self.scale)

        # Fundo branco da janela
        painter.setBrush(QBrush(QColor(255, 255, 255)))
        painter.drawRect(0, 0, 320, 640)

        # Corpo do telemóvel
        painter.setBrush(QBrush(QColor(0, 0, 0)))
        painter.drawRoundedRect(QRect(20, 20, 280, 600), 40, 40)

        # Ecrã cinza
        painter.setBrush(QBrush(QColor(50, 50, 50)))
        painter.drawRoundedRect(QRect(30, 31, 260, 576), 30, 30)

        # Notch
        painter.setBrush(QBrush(QColor(0, 0, 0)))
        painter.drawRoundedRect(QRect(122, 42, 80, 20), 10, 10)

        # Botões laterais
        painter.drawRoundedRect(QRect(292, 170, 10, 80), 10, 10)
        painter.drawRoundedRect(QRect(17, 160, 10, 50), 10, 10)
        painter.drawRoundedRect(QRect(17, 215, 10, 50), 10, 10)

        painter.end()


if __name__ == "__main__":
    # Correção da escala do Windows (High DPI)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    
    window = MockupWindow()
    window.show()
    
    sys.exit(app.exec_())