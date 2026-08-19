## 1. IMPORTS ## 

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit 
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import Qt, QRect
from calculator_code import Calculator



## 2. INTERFACE ## 

class CalculatorUI(QWidget):

    def __init__(self):
        super().__init__()

        self.calculator = Calculator()
        self.setGeometry(200, 280, 320, 640)

        # Layout principal 
        self.main_layout = QVBoxLayout(self)
        self.setLayout(self.main_layout)

        # Calculadora 
        self.display = QLineEdit(self)
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setStyleSheet("""
            font-size: 24px;
            background: transparent;
            color: white;                        
            border-radius: 10px;
        """)
        self.display.setTextMargins(10, 0, 30, 0) 
        self.display.setFixedHeight(40)

        self.grid = QGridLayout()
        self.grid.setSpacing(10) 
        self.grid.setContentsMargins(32, 32, 30, 0)

        buttons = [
            ("⌫", 0, 0), ("AC", 0, 1), ("%", 0, 2), ("÷", 0, 3),
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("x", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("+", 3, 3),
            ("+/-", 4, 0), ("0", 4, 1), (",", 4, 2), ("=", 4, 3)
        ]

        button_size = 50  

        for text, row, col in buttons:
            button = QPushButton(text)
            button.setFixedSize(button_size, button_size)
            if text in ["+", "-", "x", "÷", "="]:
                color = "#CF6C1B"
            elif text in ["⌫", "AC", "%"]:
                color = "#B1B1B1"
            else: 
                color = "#666666"
            button.setStyleSheet(f"""
                font-size: {button_size//3}px;
                border-radius: {button_size//2}px;
                background-color: {color};
                color: white;
            """)
            button.clicked.connect(lambda checked, t=text: self.button_pressed(t))
            self.grid.addWidget(button, row, col)

        # Display e botões 
        self.main_layout.addSpacing(200)
        self.main_layout.addWidget(self.display)
        self.main_layout.addLayout(self.grid)
        self.main_layout.addStretch(1)

    def paintEvent(self, event):
        """Desenha o mockup do iphone - código criado num .py à parte e copiado para aqui"""
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

    def button_pressed(self, key):
        if key.isdigit():
            self.calculator.set_number(key)
            self.display.setText(self.calculator.current)
        elif key in "+-x÷":
            if key == "x":
                self.calculator.set_operator("*")
            elif key == "÷":
                self.calculator.set_operator("/")
            else:
                self.calculator.set_operator(key)
        elif key == ",":
            self.calculator.set_number(key)
            self.display.setText(self.calculator.current)
        elif key == "%":
            self.calculator.percent()
            self.display.setText(self.calculator.current)
        elif key == "+/-":
            self.calculator.toggle_sign()
            self.display.setText(self.calculator.current)
        elif key == "AC":
            self.calculator.clear()
            self.display.setText("")
        elif key == "⌫":
            self.calculator.backspace()
            self.display.setText(self.calculator.current) 
        elif key == "=":
            result = self.calculator.calculate()
            if result is not None:
                value = float(result)
                if value.is_integer():
                    value = int(value)
                self.display.setText(str(value))



## 3. APLICAÇÃO ## 

app = QApplication(sys.argv)



## 4. INSTANCIAR JANELA 

window = CalculatorUI()
window.setWindowTitle("Calculadora")
window.show() 



## 5. LOOP PRINCIPAL ## 

sys.exit(app.exec_())