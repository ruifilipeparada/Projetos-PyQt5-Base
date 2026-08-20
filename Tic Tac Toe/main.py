import sys

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QGridLayout,
    QLabel,
    QVBoxLayout,
    QLineEdit,
    QHBoxLayout,
    QStackedLayout
)

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont

from game_code import TicTacToe
from iphone_frame import MockupWindow


class TicTacToeGUI(QWidget):

    def __init__(self):
        super().__init__()

        self.game = TicTacToe()

        self.player_names = {
            "X": "",
            "O": ""
        }

        self.blink_timer = None
        self.blink_state = False
        self.blink_buttons = []

        # ---------- Layout empilhado ----------

        self.stacked_layout = QStackedLayout()

        self.setLayout(
            self.stacked_layout
        )

        # ---------- Criar interfaces ----------

        self.init_name_screen()
        self.init_game_screen()

        self.stacked_layout.setCurrentIndex(0)



    # ==================================================
    #                    TELA DOS NOMES
    # ==================================================

    def init_name_screen(self):

        self.name_widget = QWidget()

        layout = QVBoxLayout()

        layout.setContentsMargins(
            25,
            200,
            25,
            25
        )

        layout.setSpacing(12)

        layout.setAlignment(
            Qt.AlignCenter
        )

        # ---------- Título ----------

        title = QLabel(
            "Insere os nomes\ndos jogadores"
        )

        title.setAlignment(
            Qt.AlignCenter
        )

        title.setFont(
            QFont(
                "Arial",
                14,
                QFont.Bold
            )
        )

        title.setStyleSheet(
            "color: white;"
        )

        layout.addWidget(
            title
        )

        layout.addSpacing(
            20
        )

        # ---------- Jogador X ----------

        label_x = QLabel(
            "Jogador X"
        )

        label_x.setAlignment(
            Qt.AlignCenter
        )

        label_x.setFont(
            QFont(
                "Arial",
                12,
                QFont.Bold
            )
        )

        label_x.setStyleSheet(
            "color: white;"
        )

        self.input_x = QLineEdit()

        self.input_x.setFont(
            QFont(
                "Arial",
                12
            )
        )

        self.input_x.setFixedHeight(
            34
        )

        self.input_x.setAlignment(
            Qt.AlignCenter
        )

        self.input_x.setPlaceholderText(
            "Nome do jogador X"
        )

        self.input_x.setStyleSheet("""
            QLineEdit {
                background-color: white;
                color: black;
                border: 1px solid #AAAAAA;
                border-radius: 6px;
                padding: 4px;
            }
        """)

        layout.addWidget(
            label_x
        )

        layout.addWidget(
            self.input_x
        )

        layout.addSpacing(
            8
        )

        # ---------- Jogador O ----------

        label_o = QLabel(
            "Jogador O"
        )

        label_o.setAlignment(
            Qt.AlignCenter
        )

        label_o.setFont(
            QFont(
                "Arial",
                12,
                QFont.Bold
            )
        )

        label_o.setStyleSheet(
            "color: white;"
        )

        self.input_o = QLineEdit()

        self.input_o.setFont(
            QFont(
                "Arial",
                12
            )
        )

        self.input_o.setFixedHeight(
            34
        )

        self.input_o.setAlignment(
            Qt.AlignCenter
        )

        self.input_o.setPlaceholderText(
            "Nome do jogador O"
        )

        self.input_o.setStyleSheet("""
            QLineEdit {
                background-color: white;
                color: black;
                border: 1px solid #AAAAAA;
                border-radius: 6px;
                padding: 4px;
            }
        """)

        layout.addWidget(
            label_o
        )

        layout.addWidget(
            self.input_o
        )

        layout.addSpacing(
            20
        )

        # ---------- Botão Jogar ----------

        play_btn = QPushButton(
            "Jogar"
        )

        play_btn.setCursor(
            Qt.PointingHandCursor
        )

        play_btn.setFixedSize(
            150,
            42
        )

        play_btn.setFont(
            QFont(
                "Arial",
                13,
                QFont.Bold
            )
        )

        play_btn.setStyleSheet("""
            QPushButton {
                background-color: orange;
                color: white;
                border: none;
                border-radius: 21px;
            }

            QPushButton:hover {
                background-color: #FFB52E;
            }

            QPushButton:pressed {
                background-color: #D88900;
            }
        """)

        play_btn.clicked.connect(
            self.start_game
        )

        layout.addWidget(
            play_btn,
            alignment=Qt.AlignCenter
        )

        layout.addStretch()

        self.name_widget.setLayout(
            layout
        )

        self.stacked_layout.addWidget(
            self.name_widget
        )



    # ==================================================
    #                      TELA DO JOGO
    # ==================================================

    def init_game_screen(self):

        self.game_widget = QWidget()

        layout = QVBoxLayout()

        layout.setContentsMargins(
            20,
            200,
            20,
            25
        )

        layout.setSpacing(
            12
        )

        layout.setAlignment(
            Qt.AlignCenter
        )

        # ---------- Informação do jogador ----------

        self.label = QLabel()

        self.label.setAlignment(
            Qt.AlignCenter
        )

        self.label.setWordWrap(
            True
        )

        self.label.setFont(
            QFont(
                "Arial",
                13,
                QFont.Bold
            )
        )

        self.label.setStyleSheet(
            "color: white;"
        )

        layout.addWidget(
            self.label
        )

        layout.addSpacing(
            5
        )

        # ---------- Tabuleiro ----------

        self.grid = QGridLayout()

        self.grid.setSpacing(
            5
        )

        self.grid.setContentsMargins(
            0,
            0,
            0,
            0
        )

        self.buttons = []

        for i in range(9):

            btn = QPushButton(
                ""
            )

            btn.setFixedSize(
                68,
                68
            )

            btn.setFont(
                QFont(
                    "Arial",
                    24,
                    QFont.Bold
                )
            )

            btn.clicked.connect(
                lambda checked, pos=i:
                self.handle_click(pos)
            )

            btn.setStyleSheet(
                self.get_button_style("")
            )

            self.grid.addWidget(
                btn,
                i // 3,
                i % 3
            )

            self.buttons.append(
                btn
            )

        layout.addLayout(
            self.grid
        )

        layout.addSpacing(
            8
        )

        # ---------- Botão Reset ----------

        reset_btn = QPushButton(
            "Reset"
        )

        reset_btn.setCursor(
            Qt.PointingHandCursor
        )

        reset_btn.setFixedSize(
            150,
            42
        )

        reset_btn.setFont(
            QFont(
                "Arial",
                13,
                QFont.Bold
            )
        )

        reset_btn.setStyleSheet("""
            QPushButton {
                background-color: orange;
                color: white;
                border: none;
                border-radius: 21px;
            }

            QPushButton:hover {
                background-color: #FFB52E;
            }

            QPushButton:pressed {
                background-color: #D88900;
            }
        """)

        reset_btn.clicked.connect(
            self.reset_game
        )

        layout.addWidget(
            reset_btn,
            alignment=Qt.AlignCenter
        )

        layout.addStretch()

        self.game_widget.setLayout(
            layout
        )

        self.stacked_layout.addWidget(
            self.game_widget
        )



    # ==================================================
    #                     TRANSIÇÃO
    # ==================================================

    def start_game(self):

        x_name = (
            self.input_x.text().strip()
            or "Jogador X"
        )

        o_name = (
            self.input_o.text().strip()
            or "Jogador O"
        )

        self.player_names["X"] = x_name
        self.player_names["O"] = o_name

        self.update_label()

        self.stacked_layout.setCurrentIndex(
            1
        )



    # ==================================================
    #                       ESTILO
    # ==================================================

    def get_button_style(
        self,
        value,
        force_bg=None
    ):

        bg = (
            force_bg
            if force_bg
            else "white"
        )

        color = "black"

        if value == "X":
            color = "red"

        elif value == "O":
            color = "blue"

        return f"""
            QPushButton {{
                border: 1px solid black;
                border-radius: 6px;
                font-weight: bold;
                font-size: 24px;
                background-color: {bg};
                color: {color};
            }}
        """



    # ==================================================
    #                        JOGO
    # ==================================================

    def handle_click(self, position):

        if self.game.make_move(position):

            val = self.game.get_board()[position]

            self.buttons[position].setText(
                val
            )

            self.buttons[position].setStyleSheet(
                self.get_button_style(val)
            )

            if self.game.is_game_over():

                winner = self.game.get_winner()

                if winner:

                    self.start_blink(
                        winner
                    )

                    self.label.setText(
                        f"Vitória de "
                        f"{self.player_names[winner]}!"
                    )

                else:

                    self.label.setText(
                        "Empate!"
                    )

            else:

                self.update_label()



    def update_label(self):

        cp = self.game.get_current_player()

        self.label.setText(
            f"Jogador atual: "
            f"{self.player_names[cp]}"
        )



    # ==================================================
    #                        BLINK
    # ==================================================

    def start_blink(self, winner):

        combos = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]

        board = self.game.get_board()

        for combo in combos:

            a, b, c = combo

            if (
                board[a]
                == board[b]
                == board[c]
                == winner
            ):

                self.blink_buttons = [
                    self.buttons[i]
                    for i in combo
                ]

                break

        self.blink_state = False

        self.blink_timer = QTimer()

        self.blink_timer.timeout.connect(
            self.blink
        )

        self.blink_timer.start(
            500
        )



    def blink(self):

        self.blink_state = (
            not self.blink_state
        )

        color = (
            "orange"
            if self.blink_state
            else "white"
        )

        for btn in self.blink_buttons:

            btn.setStyleSheet(
                self.get_button_style(
                    btn.text(),
                    color
                )
            )



    # ==================================================
    #                        RESET
    # ==================================================

    def reset_game(self):

        self.game.reset()

        if self.blink_timer:

            self.blink_timer.stop()

            self.blink_timer = None

        self.blink_buttons = []

        self.blink_state = False

        for btn in self.buttons:

            btn.setText("")

            btn.setStyleSheet(
                self.get_button_style("")
            )

        self.update_label()



# ======================================================
#                         MAIN
# ======================================================

def main():

    QApplication.setAttribute(
        Qt.AA_EnableHighDpiScaling,
        True
    )

    QApplication.setAttribute(
        Qt.AA_UseHighDpiPixmaps,
        True
    )

    app = QApplication(
        sys.argv
    )

    jogo = TicTacToeGUI()

    janela = MockupWindow(
        jogo
    )

    janela.show()

    sys.exit(
        app.exec_()
    )


if __name__ == "__main__":
    main()