import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer

from code import GameLogic
from mockup_iphone import MockupWindow


class DifficultyWidget(QWidget):
    def __init__(self, start_callback):
        super().__init__()
        self.start_callback = start_callback
        self.setStyleSheet("background-color: rgb(50, 50, 50);")

        self.title = QLabel("Escolhe a dificuldade", self)
        self.title.setStyleSheet("color: white; font-weight: bold; font-size: 16px;")
        self.title.setAlignment(Qt.AlignCenter)

        self.buttons = {}
        levels = ["iniciante", "facil", "moderado", "dificil", "geografo"]
        btn_height = 35
        spacing = 12  
        total_height_buttons = btn_height*len(levels) + spacing*(len(levels)-1)
        total_widget_height = 546
        top_margin = (total_widget_height - total_height_buttons - 50) // 2
        self.title.setGeometry(30, top_margin, 200, 30)

        for i, level in enumerate(levels):
            btn = QPushButton(level.capitalize(), self)
            btn.setStyleSheet("""
                background-color: rgb(0, 120, 255);
                color: white;
                border-radius: 12px;
                font-weight: bold;
                font-size: 14px;
            """)
            btn_top = top_margin + 50 + i*(btn_height + spacing)
            btn.setGeometry(80, btn_top, 100, btn_height)
            btn.clicked.connect(lambda _, l=level: self.choose_level(l))
            self.buttons[level] = btn

    def choose_level(self, level):
        self.start_callback(level)


class GameWidget(QWidget):
    def __init__(self, game_logic, end_callback):
        super().__init__()

        self.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.game = game_logic
        self.end_callback = end_callback

        # ---------------- SCORE ----------------
        self.score_text = QLabel("Score:", self)
        self.score_text.setStyleSheet("""
            color: white;
            font-weight: bold;
            font-size: 16px;
        """)
        self.score_text.setAlignment(Qt.AlignRight)

        self.score_box = QLabel("0/10", self)
        self.score_box.setAlignment(Qt.AlignCenter)
        self.score_box.setStyleSheet("""
            background-color: rgb(0, 120, 255);
            color: white;
            border-radius: 15px;
            font-weight: bold;
            font-size: 14px;
        """)

        # ---------------- FLAG ----------------
        self.flag_label = QLabel(self)
        self.flag_label.setAlignment(Qt.AlignCenter)

        # ---------------- INPUT ----------------
        self.input = QLineEdit(self)
        self.input.setAlignment(Qt.AlignCenter)
        self.input.setPlaceholderText("Adivinha o país")
        self.input.setStyleSheet("""
            background-color: rgb(200, 200, 200);
            border-radius: 10px;
            padding-left: 10px;
            font-weight: bold;
            font-size: 14px;
            color: black;
        """)

        # ---------------- BUTTON ----------------
        self.btn = QPushButton("Verificar", self)
        self.btn.setStyleSheet("""
            background-color: rgb(0, 120, 255);
            color: white;
            border-radius: 12px;
            font-weight: bold;
            font-size: 14px;
        """)

        # ---------------- FEEDBACK ----------------
        self.feedback = QLabel("", self)
        self.feedback.setAlignment(Qt.AlignCenter)
        self.feedback.setStyleSheet("""
            color: white;
            font-weight: bold;
        """)

        # ---------------- EVENTS ----------------
        self.btn.clicked.connect(self.check_answer)
        self.input.returnPressed.connect(self.btn.click)

        # ---------------- LAYOUT ----------------
        self.reposition_elements()

        # ---------------- START ----------------
        self.load_new_flag()

    def reposition_elements(self):
        total_height = 546
        total_width = 260

        # Alturas fixas
        score_height = 30
        score_box_size = 45
        flag_height = 150
        input_height = 40
        btn_height = 35
        feedback_height = 30

        # Espaçamentos
        spacing_flag_input = 15
        spacing_input_btn = 15
        spacing_btn_feedback = 12

        # Margem topo/fundo
        used_space = (score_height + flag_height + input_height + btn_height + feedback_height +
                      spacing_flag_input + spacing_input_btn + spacing_btn_feedback)
        margin = (total_height - used_space) // 2

        # ---------------- SCORE ----------------
        score_y = margin
        # centralizar horizontalmente o score e a caixa
        center_x = (total_width - 120) // 2
        self.score_text.setGeometry(center_x + 15, score_y, 50, score_height)
        self.score_box.setGeometry(center_x + 70, score_y - 4, 50, 30)

        # ---------------- BANDEIRA ----------------
        flag_top = score_y + score_height + spacing_flag_input
        self.flag_label.setGeometry(30, flag_top, 200, flag_height)

        # ---------------- INPUT ----------------
        input_top = flag_top + flag_height + spacing_flag_input
        self.input.setGeometry(30, input_top, 200, input_height)

        # ---------------- BOTÃO ----------------
        btn_top = input_top + input_height + 50
        self.btn.setGeometry(80, btn_top, 100, btn_height)

        # ---------------- FEEDBACK ----------------
        feedback_top = btn_top + btn_height + spacing_btn_feedback
        self.feedback.setGeometry(30, feedback_top, 200, feedback_height)

    def load_new_flag(self):
        code = self.game.next_flag()
        if code is None:
            self.end_callback(self.game.get_score())
            return

        pixmap = QPixmap(f"flags/{code}.png")
        if pixmap.isNull():
            print(f"Erro ao carregar: flags/{code}.png")

        self.flag_label.setPixmap(
            pixmap.scaled(200, 150, Qt.KeepAspectRatio)
        )

        self.input.clear()
        self.feedback.setText("")
        self.input.setStyleSheet("""
            background-color: rgb(200, 200, 200);
            border-radius: 10px;
            padding-left: 10px;
            font-weight: bold;
            font-size: 14px;
            color: black;
        """)
        self.score_box.setStyleSheet("""
            background-color: rgb(0, 120, 255);
            color: white;
            border-radius: 15px;
            font-weight: bold;
            font-size: 14px;
        """)
        self.score_box.setText(f"{self.game.get_score()}/{self.game.round - 1}")

    def check_answer(self):
        user_input = self.input.text()
        result, correct = self.game.check_answer(user_input)

        if result:
            input_original = self.input.styleSheet()
            score_original = self.score_box.styleSheet()

            self.input.setStyleSheet("""
                background-color: rgb(0, 150, 0);
                border-radius: 10px;
                padding-left: 10px;
                font-weight: bold;
                font-size: 14px;
                color: white;
            """)
            self.score_box.setStyleSheet("""
                background-color: rgb(0, 150, 0);
                color: white;
                border-radius: 15px;
                font-weight: bold;
                font-size: 14px;
            """)
            QTimer.singleShot(500, lambda: self.input.setStyleSheet(input_original))
            QTimer.singleShot(500, lambda: self.score_box.setStyleSheet(score_original))
        else:
            input_original = self.input.styleSheet()
            score_original = self.score_box.styleSheet()

            self.input.setText(correct)
            self.input.setStyleSheet("""
                background-color: rgb(255, 0, 0);
                border-radius: 10px;
                padding-left: 10px;
                font-weight: bold;
                font-size: 14px;
                color: white;
            """)
            self.score_box.setStyleSheet("""
                background-color: rgb(200, 0, 0);
                color: white;
                border-radius: 15px;
                font-weight: bold;
                font-size: 14px;
            """)
            QTimer.singleShot(500, lambda: self.input.setStyleSheet(input_original))
            QTimer.singleShot(500, lambda: self.score_box.setStyleSheet(score_original))

        self.score_box.setText(f"{self.game.get_score()}/{self.game.round - 1}")
        QTimer.singleShot(700, self.load_new_flag)


class EndWidget(QWidget):
    def __init__(self, score, restart_callback):
        super().__init__()
        self.restart_callback = restart_callback
        self.setStyleSheet("background-color: rgb(50, 50, 50);")

        # ---------------- SCORE FINAL TEXTO ----------------
        self.score_text_label = QLabel("Score final", self)
        self.score_text_label.setAlignment(Qt.AlignCenter)
        self.score_text_label.setStyleSheet("color: white; font-weight: bold; font-size: 16px;")
        self.score_text_label.setGeometry(30, 150, 200, 30)

        # ---------------- SCORE FINAL (RETÂNGULO + TEXTO JUNTOS) ----------------
        self.label = QLabel(f"{score}/10", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("""
            background-color: rgb(0, 120, 255);
            color: white;
            border-radius: 15px;
            font-weight: bold;
            font-size: 16px;
        """)
        self.label.setGeometry(100, 200, 60, 40)

        # ---------------- BOTÃO VOLTAR AO MENU ----------------
        self.btn = QPushButton("Voltar ao menu", self)
        self.btn.setStyleSheet("""
            background-color: rgb(0, 120, 255);
            color: white;
            border-radius: 12px;
            font-weight: bold;
            font-size: 14px;
        """)
        self.btn.setGeometry(60, 300, 140, 35)
        self.btn.clicked.connect(self.restart_callback)


class MainWindow(QApplication):
    def __init__(self, sys_argv):
        super().__init__(sys_argv)
        self.mockup = None
        self.current_widget = None
        self.game_logic = GameLogic()
        self.show_difficulty()

    def show_difficulty(self):
        self.show_widget(DifficultyWidget(self.start_game))

    def start_game(self, level):
        self.game_logic.choose_difficulty(level)
        self.show_widget(GameWidget(self.game_logic, self.show_end))

    def show_end(self, score):
        self.show_widget(EndWidget(score, self.show_difficulty))

    def show_widget(self, widget):
        if self.mockup:
            self.mockup.close()
        self.current_widget = widget
        self.mockup = MockupWindow(self.current_widget)
        self.mockup.show()


if __name__ == "__main__":
    app = MainWindow(sys.argv)
    sys.exit(app.exec_())