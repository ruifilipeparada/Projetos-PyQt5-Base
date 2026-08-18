import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

from iphone_frame import MockupWindow
from code_game import GameWidget


def main():

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True) # (High DPI - corrigir escala w)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)

    game_widget = GameWidget()

    window = MockupWindow(game_widget)
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()