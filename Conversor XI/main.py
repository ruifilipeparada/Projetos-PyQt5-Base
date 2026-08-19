import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit
)
from PyQt5.QtCore import Qt

from code import int_to_roman, roman_to_int
from moldura_iphone import MockupWindow


# ---------------- Styling ----------------

def style_menu_button(btn):
    btn.setStyleSheet("""
        QPushButton {
            background-color: #B22222;
            color: white;
            border-radius: 12px;
            font-weight: bold;
            font-size: 14px;
            padding: 8px;
        }
        QPushButton:hover {
            background-color: #D32F2F;
        }
    """)


def style_action_button(btn):
    btn.setStyleSheet("""
        QPushButton {
            background-color: #B22222;
            color: white;
            border-radius: 12px;
            font-weight: bold;
            font-size: 14px;
            padding: 8px;
        }
        QPushButton:hover {
            background-color: #D32F2F;
        }
    """)


def style_input(widget, width=180, height=40):
    widget.setFixedSize(width, height)
    widget.setStyleSheet("""
        QLineEdit {
            background-color: #D9D9D9;
            border-radius: 12px;
            padding: 8px;
            font-size: 16px;
        }
    """)


# ---------------- Main App ----------------

class RomanConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(260, 547)

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(5)
        self.setLayout(self.main_layout)

        self.build_menu()
        self.build_converter()
        self.show_menu()

    # ---------------- Menu ----------------
    def build_menu(self):
        self.menu_widget = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(20)

        title = QLabel()
        title.setText('CONVERSOR <span style="color:#B22222;">XI</span>')
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold; color: white;")

        self.btn_to_roman = QPushButton("Number to Roman")
        self.btn_to_number = QPushButton("Roman to Number")

        for btn in [self.btn_to_roman, self.btn_to_number]:
            btn.setFixedSize(200, 50)
            style_menu_button(btn)

        self.btn_to_roman.clicked.connect(self.open_to_roman)
        self.btn_to_number.clicked.connect(self.open_to_number)

        layout.addWidget(title)
        layout.addWidget(self.btn_to_roman)
        layout.addWidget(self.btn_to_number)
        self.menu_widget.setLayout(layout)
        self.main_layout.addWidget(self.menu_widget)

    # ---------------- Converter ----------------
    def build_converter(self):
        self.converter_widget = QWidget(self)
        self.converter_widget.setGeometry(0, 0, 260, 546)

        base_y = 150

        # Título da conversão
        self.title_label = QLabel("", self.converter_widget)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setGeometry(0, base_y, 260, 30)
        self.title_label.setStyleSheet("color: white; font-size: 18px; font-weight: bold;")

        # Input cinza centralizado horizontalmente
        self.input = QLineEdit(self.converter_widget)
        style_input(self.input)
        self.input.setAlignment(Qt.AlignCenter)
        self.input.move((260 - self.input.width()) // 2, base_y + 50)

        # Botões inferiores (criar antes de conectar Enter)
        self.buttons_widget = QWidget(self.converter_widget)
        self.buttons_widget.setGeometry(20, 470, 220, 50)
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(15)
        buttons_layout.setAlignment(Qt.AlignCenter)
        self.buttons_widget.setLayout(buttons_layout)

        self.btn_convert = QPushButton("Convert")
        self.btn_back = QPushButton("Back")
        for btn in [self.btn_convert, self.btn_back]:
            btn.setFixedSize(90, 35)
            style_action_button(btn)
            buttons_layout.addWidget(btn)

        self.btn_back.clicked.connect(self.show_menu)

        # Captura Enter para disparar botão Convert
        self.input.returnPressed.connect(lambda: self.btn_convert.click())

        # Resultado
        self.result = QLabel("", self.converter_widget)
        self.result.setAlignment(Qt.AlignCenter)
        self.result.setGeometry(0, base_y + 110, 260, 50)
        self.result.setStyleSheet("color: white; font-size: 24px; font-weight: bold;")

    # ---------------- Navigation ----------------
    def show_menu(self):
        self.menu_widget.show()
        self.converter_widget.hide()

    def open_to_roman(self):
        self.mode = "to_roman"
        self.title_label.setText("Number to Roman")
        self.input.clear()
        self.result.setText("")
        self.menu_widget.hide()
        self.converter_widget.show()
        try: self.btn_convert.clicked.disconnect()
        except: pass
        self.btn_convert.clicked.connect(self.convert_to_roman)

    def open_to_number(self):
        self.mode = "to_number"
        self.title_label.setText("Roman to Number")
        self.input.clear()
        self.result.setText("")
        self.menu_widget.hide()
        self.converter_widget.show()
        try: self.btn_convert.clicked.disconnect()
        except: pass
        self.btn_convert.clicked.connect(self.convert_to_number)

    # ---------------- Conversion ----------------
    def convert_to_roman(self):
        text = self.input.text()
        if not text.isdigit():
            self.result.setText("Invalid number")
            return
        number = int(text)
        if number < 1 or number > 3999:
            self.result.setText("1-3999 only")
            return
        self.result.setText(int_to_roman(number))

    def convert_to_number(self):
        text = self.input.text()
        number = roman_to_int(text)
        if number is None:
            self.result.setText("Invalid Roman")
        else:
            self.result.setText(str(number))


# ---------------- Main ----------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    content_widget = RomanConverterApp()
    window = MockupWindow(content_widget)
    window.show()
    sys.exit(app.exec_())