"""
----- IMPORTS -----

"""

from PyQt5.QtCore import (Qt, QTimer, QPropertyAnimation, QPoint, QEasingCurve, QRect)
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QStackedWidget, QGridLayout)
import random



"""
--------------------------------------------------------------- CLASS PRINCIPAL GameWidget(QWidget) ---------------------------------------------------------------

----- ÍNDICE DA CLASS GameWidget(QWidget) -----

- STACK DE INTERFACES  
- INTERFACES 
    - Interface Menu 
    - Interface Modos de Jogo
    - Interface Palavro 
    - Interface Parelha 
    - Interface Quadra 
    - Interface Contratempo
    - Interface Vitória 
    - Interface Derrota
    - Interface Vitória Contratempo 
    - Interface Derrota Contratempo 
- TABULEIROS 
    - Tabuleiro Palavro / Contratempo 
    - Tabuleiro Parelha 
    - Tabuleiro Quadra 
- LÓGICA DE JOGO 
    - Lógicas Comuns Entre Modos 
    - Lógicas Individuais 
- ANIMAÇÕES 
- NAVEGAÇÃO 

"""



class GameWidget(QWidget):
   
    # =====================================================
    # STACK DE INTERFACES
    # =====================================================  

    def __init__(self):
        super().__init__()

        self.stack = QStackedWidget()

        self.timer_contratempo = QTimer(self)
        self.tempo_restante_contratempo = 300
        self.timer_contratempo.timeout.connect(
            self.atualizar_tempo_contratempo
        )        

        # ---------- Criar Interfaces ----------
        self.interface_menu = self.criar_interface_menu()
        self.interface_modos = self.criar_interface_modos()
        self.interface_jogo = self.criar_interface_jogo()
        self.interface_parelha = self.criar_interface_parelha()
        self.interface_quadra = self.criar_interface_quadra()
        self.interface_contratempo = self.criar_interface_contratempo()
        self.interface_vitoria = self.criar_interface_vitoria()
        self.interface_derrota = self.criar_interface_derrota()
        self.interface_vitoria_contratempo = self.criar_interface_vitoria_contratempo()
        self.interface_derrota_contratempo = self.criar_interface_derrota_contratempo()        

        # ---------- Adicionar ao Stack ----------
        self.stack.addWidget(self.interface_menu)
        self.stack.addWidget(self.interface_modos)
        self.stack.addWidget(self.interface_jogo)
        self.stack.addWidget(self.interface_parelha)
        self.stack.addWidget(self.interface_quadra)
        self.stack.addWidget(self.interface_contratempo)
        self.stack.addWidget(self.interface_vitoria)
        self.stack.addWidget(self.interface_derrota)
        self.stack.addWidget(self.interface_vitoria_contratempo)
        self.stack.addWidget(self.interface_derrota_contratempo)        

        # ---------- Layout Principal ----------
        layout_principal = QVBoxLayout()
        layout_principal.setContentsMargins(0, 0, 0, 0)
        layout_principal.addWidget(self.stack)

        self.setLayout(layout_principal)
        self.setFocusPolicy(Qt.StrongFocus)

        with open("dicionario.txt", "r", encoding="utf-8") as ficheiro:

            self.dicionario = [
                palavra.strip().upper()
                for palavra in ficheiro
                if palavra.strip()
            ]

        with open("respostas.txt", "r", encoding="utf-8") as ficheiro:

            self.respostas = [
                palavra.strip().upper()
                for palavra in ficheiro
                if palavra.strip()
            ]



    # =====================================================
    # INTERFACES
    # =====================================================

    # ============= INTERFACE MENU =============

    def criar_interface_menu(self):
        pagina = QWidget()

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 40, 20, 40)
        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignCenter)

        # ---------- Logótipo ----------

        logo = QLabel()

        logo.setText(
            "<span style='color:#8B1E2D;'>P</span>"
            "<span style='color:white;'>ALAVRO</span>"
        )

        logo.setAlignment(Qt.AlignCenter)
        logo.setFont(QFont("Arial", 30, QFont.Bold))

        # ---------- Botão ----------

        jogar_btn = QPushButton("Jogar")

        jogar_btn.setCursor(Qt.PointingHandCursor)
        jogar_btn.setFixedSize(170, 48)

        jogar_btn.setStyleSheet("""
            QPushButton {
                background-color: #8B1E2D;
                color: white;
                border: none;
                border-radius: 24px;
                font-size: 16px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #A32135;
            }

            QPushButton:pressed {
                background-color: #6F1622;
            }
        """)

        jogar_btn.clicked.connect(self.iniciar_jogo)

        # ---------- Layout ----------

        layout.addStretch()

        layout.addWidget(logo)

        layout.addSpacing(40)

        layout.addWidget(jogar_btn, alignment=Qt.AlignCenter)

        layout.addStretch()

        pagina.setLayout(layout)

        return pagina



    # ============= INTERFACE MODOS DE JOGO =============

    def criar_interface_modos(self):

        pagina = QWidget()

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 60, 20, 20)
        layout.setSpacing(40)

        # ---------- Título ----------

        titulo = QLabel()

        titulo.setText(
            "<span style='color:#8B1E2D;'>P</span>"
            "<span style='color:white;'>ALAVRO</span>"
        )

        titulo.setAlignment(Qt.AlignCenter)
        titulo.setFont(QFont("Arial", 24, QFont.Bold))

        layout.addWidget(titulo)

        layout.addSpacing(120)

        # ---------- Botões ----------

        self.botao_palavro = QPushButton("Palavro")
        self.botao_parelha = QPushButton("Parelha")
        self.botao_quadra = QPushButton("Quadra")
        self.botao_contratempo = QPushButton("Contratempo")

        botoes = [

            self.botao_palavro,
            self.botao_parelha,
            self.botao_quadra,
            self.botao_contratempo

        ]

        for botao in botoes:

            botao.setCursor(Qt.PointingHandCursor)
            botao.setFixedSize(170, 48)

            botao.setStyleSheet("""
                QPushButton {
                    background-color: #8B1E2D;
                    color: white;
                    border: none;
                    border-radius: 24px;
                    font-size: 16px;
                    font-weight: bold;
                }

                QPushButton:hover {
                    background-color: #A32135;
                }

                QPushButton:pressed {
                    background-color: #6F1622;
                }
            """)

            layout.addWidget(
                botao,
                alignment=Qt.AlignCenter
            )

        # ---------- Ligações ----------

        self.botao_palavro.clicked.connect(self.iniciar_palavro)
        self.botao_parelha.clicked.connect(self.iniciar_parelha)
        self.botao_quadra.clicked.connect(self.iniciar_quadra)
        self.botao_contratempo.clicked.connect(self.iniciar_contratempo)

        layout.addStretch()

        pagina.setLayout(layout)

        return pagina



    # ============= INTERFACE PALAVRO =============

    def criar_interface_jogo(self):
        pagina = QWidget()

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 60, 20, 20)
        layout.setSpacing(20)

        # ---------- Título ----------

        titulo = QLabel()

        titulo.setText(
            "<span style='color:#8B1E2D;'>P</span>"
            "<span style='color:white;'>ALAVRO</span>"
        )

        titulo.setAlignment(Qt.AlignCenter)
        titulo.setFont(QFont("Arial", 24, QFont.Bold))

        layout.addWidget(titulo)

        # ---------- Tabuleiro ----------

        self.tabuleiro = QWidget()

        self.tabuleiro.setFixedSize(320, 560)

        self.caixas_palavro = self.criar_tabuleiro(
            self.tabuleiro
        )        

        layout.addWidget(self.tabuleiro, alignment=Qt.AlignCenter)

        # ---------- Mensagem ----------

        self.label_mensagem = QLabel()

        self.label_mensagem.setAlignment(Qt.AlignCenter)
        self.label_mensagem.setFont(QFont("Arial", 14, QFont.Bold))
        self.label_mensagem.setStyleSheet("color: white;")

        layout.addWidget(self.label_mensagem)

        layout.addStretch()

        pagina.setLayout(layout)

        return pagina



    # ============= INTERFACE PARELHA =============

    def criar_interface_parelha(self):

        pagina = QWidget()

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 60, 20, 20)
        layout.setSpacing(20)

        # ---------- Título ----------

        titulo = QLabel()

        titulo.setText(
            "<span style='color:#8B1E2D;'>P</span>"
            "<span style='color:white;'>ALAVRO</span>"
        )

        titulo.setAlignment(Qt.AlignCenter)
        titulo.setFont(QFont("Arial", 24, QFont.Bold))

        layout.addWidget(titulo)

        layout.addSpacing(100)

        # ---------- Tabuleiro ----------

        layout_tabuleiros = QHBoxLayout()

        layout_tabuleiros.setSpacing(20)
        layout_tabuleiros.setAlignment(Qt.AlignCenter)

        self.tabuleiro_esquerdo = QWidget()
        self.tabuleiro_direito = QWidget()

        self.tabuleiro_esquerdo.setFixedSize(160, 460)
        self.tabuleiro_direito.setFixedSize(160, 460)

        self.criar_tabuleiro_parelha()

        layout_tabuleiros.addWidget(self.tabuleiro_esquerdo)
        layout_tabuleiros.addWidget(self.tabuleiro_direito)

        layout.addLayout(layout_tabuleiros)

        # ---------- Mensagem ----------

        self.label_mensagem_parelha = QLabel()

        self.label_mensagem_parelha.setAlignment(Qt.AlignCenter)
        self.label_mensagem_parelha.setFont(QFont("Arial", 14, QFont.Bold))
        self.label_mensagem_parelha.setStyleSheet("color: white;")

        layout.addWidget(self.label_mensagem_parelha)

        layout.addStretch()

        pagina.setLayout(layout)

        return pagina



    # ============= INTERFACE QUADRA =============

    def criar_interface_quadra(self):

        pagina = QWidget()

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        # ---------- Título ----------

        titulo = QLabel()

        titulo.setText(
            "<span style='color:#8B1E2D;'>P</span>"
            "<span style='color:white;'>ALAVRO</span>"
        )

        titulo.setAlignment(Qt.AlignCenter)
        titulo.setFont(QFont("Arial", 24, QFont.Bold))

        layout.addWidget(titulo)

        # ---------- Tabuleiros ----------

        layout_quadra = QVBoxLayout()

        layout_quadra.setSpacing(20)
        layout_quadra.setAlignment(Qt.AlignCenter)

        # ---------- Linha Superior ----------

        layout_superior = QHBoxLayout()

        layout_superior.setSpacing(20)
        layout_superior.setAlignment(Qt.AlignCenter)

        self.tabuleiro_1 = QWidget()
        self.tabuleiro_2 = QWidget()

        self.tabuleiro_1.setFixedSize(160, 310)
        self.tabuleiro_2.setFixedSize(160, 310)

        layout_superior.addWidget(self.tabuleiro_1)
        layout_superior.addWidget(self.tabuleiro_2)

        # ---------- Linha Inferior ----------

        layout_inferior = QHBoxLayout()

        layout_inferior.setSpacing(20)
        layout_inferior.setAlignment(Qt.AlignCenter)

        self.tabuleiro_3 = QWidget()
        self.tabuleiro_4 = QWidget()

        self.tabuleiro_3.setFixedSize(160, 310)
        self.tabuleiro_4.setFixedSize(160, 310)

        layout_inferior.addWidget(self.tabuleiro_3)
        layout_inferior.addWidget(self.tabuleiro_4)

        # ---------- Criar Tabuleiros ----------

        self.criar_tabuleiro_quadra()

        # ---------- Juntar Tabuleiros ----------

        layout_quadra.addLayout(layout_superior)
        layout_quadra.addLayout(layout_inferior)

        layout.addLayout(layout_quadra)

        # ---------- Mensagem ----------

        self.label_mensagem_quadra = QLabel()

        self.label_mensagem_quadra.setAlignment(Qt.AlignCenter)
        self.label_mensagem_quadra.setFont(
            QFont("Arial", 14, QFont.Bold)
        )
        self.label_mensagem_quadra.setStyleSheet(
            "color: white;"
        )

        layout.addWidget(self.label_mensagem_quadra)

        layout.addStretch()

        pagina.setLayout(layout)

        return pagina



    # ============= INTERFACE CONTRATEMPO =============

    def criar_interface_contratempo(self):

        pagina = QWidget()

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 60, 20, 20)
        layout.setSpacing(20)

        # ---------- Título ----------

        titulo = QLabel()

        titulo.setText(
            "<span style='color:#8B1E2D;'>P</span>"
            "<span style='color:white;'>ALAVRO</span>"
        )

        titulo.setAlignment(Qt.AlignCenter)
        titulo.setFont(QFont("Arial", 24, QFont.Bold))

        layout.addWidget(titulo)

        # ---------- Tabuleiro ----------

        self.tabuleiro_contratempo = QWidget()

        self.tabuleiro_contratempo.setFixedSize(
            320,
            560
        )

        self.caixas_contratempo = self.criar_tabuleiro(
            self.tabuleiro_contratempo
        )        

        layout.addWidget(
            self.tabuleiro_contratempo,
            alignment=Qt.AlignCenter
        )

        # ---------- Mensagem ----------

        self.label_mensagem_contratempo = QLabel()

        self.label_mensagem_contratempo.setAlignment(
            Qt.AlignCenter
        )

        self.label_mensagem_contratempo.setFont(
            QFont("Arial", 10, QFont.Bold)
        )

        self.label_mensagem_contratempo.setStyleSheet(
            "color: white;"
        )

        self.label_mensagem_contratempo.setFixedHeight(
            28
        )

        layout.addWidget(
            self.label_mensagem_contratempo
        )

        # ---------- Controlos ----------

        layout_controlos = QHBoxLayout()

        layout_controlos.setContentsMargins(
            0,
            0,
            0,
            0
        )

        layout_controlos.setSpacing(10)

        # ---------- Temporizador ----------

        self.label_tempo_contratempo = QLabel()

        self.label_tempo_contratempo.setText(
            "05:00"
        )

        self.label_tempo_contratempo.setAlignment(
            Qt.AlignCenter
        )

        self.label_tempo_contratempo.setFont(
            QFont("Arial", 11, QFont.Bold)
        )

        self.label_tempo_contratempo.setStyleSheet("""
            QLabel {
                background-color: #8B1E2D;
                color: white;
                border-radius: 14px;
            }
        """)

        self.label_tempo_contratempo.setFixedSize(
            155,
            36
        )

        layout_controlos.addWidget(
            self.label_tempo_contratempo
        )

        # ---------- Botão Desistir ----------

        self.botao_desistir_contratempo = QPushButton(
            "Desistir"
        )

        self.botao_desistir_contratempo.setCursor(
            Qt.PointingHandCursor
        )

        self.botao_desistir_contratempo.setFixedSize(
            155,
            36
        )

        self.botao_desistir_contratempo.setStyleSheet("""
            QPushButton {
                background-color: #8B1E2D;
                color: white;
                border: none;
                border-radius: 18px;
                font-size: 16px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #A32135;
            }

            QPushButton:pressed {
                background-color: #6F1622;
            }
        """)

        self.botao_desistir_contratempo.clicked.connect(
            self.terminar_contratempo
        )        

        layout_controlos.addWidget(
            self.botao_desistir_contratempo
        )

        layout.addLayout(
            layout_controlos
        )

        layout.addStretch()

        pagina.setLayout(layout)

        return pagina
 


    # ============= INTERFACE VITÓRIA =============

    def criar_interface_vitoria(self):
        pagina = QWidget()

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 60, 20, 40)
        layout.setSpacing(25)
        layout.setAlignment(Qt.AlignCenter)

        # ---------- Título ----------

        frases_vitoria = [
            "Olha quem afinal sabe jogar",
            "Contra todas as expectativas, acertaste",
            "Muito bem, até parece fácil",
            "Nada mau, quase impressionante",
            "Pelos vistos sabes umas coisas",
            "A cheatar também eu",
            "Fecha a Infopédia, por favor",
            "Sorte de principiante, for sure",
            "Pediste ajuda a quem?",
            "Mete isto no currículo, qualidade", 
            "O dev do jogo está proud"
        ]

        titulo = QLabel()

        titulo.setText(
            random.choice(frases_vitoria)
        )

        titulo.setAlignment(Qt.AlignCenter)

        titulo.setWordWrap(True)

        titulo.setFont(
            QFont("Arial", 12, QFont.Bold)
        )

        titulo.setStyleSheet(
            "color: white;"
        )

        # ---------- Palavra ----------

        self.label_palavra_vitoria = QLabel()

        self.label_palavra_vitoria.setText("A palavra era:")

        self.label_palavra_vitoria.setAlignment(Qt.AlignCenter)
        self.label_palavra_vitoria.setFont(QFont("Arial", 12, QFont.Bold))
        self.label_palavra_vitoria.setStyleSheet("color: white;")

        # ---------- Botão ----------

        jogar_novamente_btn = QPushButton("Jogar novamente")

        jogar_novamente_btn.setCursor(Qt.PointingHandCursor)
        jogar_novamente_btn.setFixedSize(170, 48)

        jogar_novamente_btn.setStyleSheet("""
            QPushButton {
                background-color: #8B1E2D;
                color: white;
                border: none;
                border-radius: 24px;
                font-size: 16px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #A32135;
            }

            QPushButton:pressed {
                background-color: #6F1622;
            }
        """)

        jogar_novamente_btn.clicked.connect(self.escolher_modo)

        # ---------- Layout ----------

        layout.addStretch()

        layout.addWidget(titulo)

        layout.addSpacing(20)

        layout.addWidget(self.label_palavra_vitoria)

        layout.addSpacing(40)

        layout.addWidget(jogar_novamente_btn, alignment=Qt.AlignCenter)

        layout.addStretch()

        pagina.setLayout(layout)

        return pagina



    # ============= INTERFACE DERROTA =============

    def criar_interface_derrota(self):
        pagina = QWidget()

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 60, 20, 40)
        layout.setSpacing(25)
        layout.setAlignment(Qt.AlignCenter)

        # ---------- Título ----------

        frases_derrota = [
            "Faltou só... acertares :)",
            "Upsi :>",
            "Pelo menos és consistente",
            'Level upgrade em "Falhado", parabéns',
            "Esconde a tela para ninguém ver a desgraça",
            "Nunca desiludes em desiludir",
            "Esta era difícil para quem anda na Primária",
            "Baixa a dificuldade para: Principiante",
            "Sorry not sorry",
            "Não te preocupes, para a próxima voltas a errar", 
            "For real, bro? :|"
        ]

        titulo = QLabel()

        titulo.setText(
            random.choice(frases_derrota)
        )

        titulo.setAlignment(Qt.AlignCenter)

        titulo.setWordWrap(True)

        titulo.setFont(
            QFont("Arial", 12, QFont.Bold)
        )

        titulo.setStyleSheet(
            "color: white;"
        )

        # ---------- Palavra ----------

        self.label_palavra_derrota = QLabel()

        self.label_palavra_derrota.setText("A palavra era:")

        self.label_palavra_derrota.setAlignment(Qt.AlignCenter)
        self.label_palavra_derrota.setFont(QFont("Arial", 12, QFont.Bold))
        self.label_palavra_derrota.setStyleSheet("color: white;")

        # ---------- Botão ----------

        jogar_novamente_btn = QPushButton("Jogar novamente")

        jogar_novamente_btn.setCursor(Qt.PointingHandCursor)
        jogar_novamente_btn.setFixedSize(170, 48)

        jogar_novamente_btn.setStyleSheet("""
            QPushButton {
                background-color: #8B1E2D;
                color: white;
                border: none;
                border-radius: 24px;
                font-size: 16px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #A32135;
            }

            QPushButton:pressed {
                background-color: #6F1622;
            }
        """)

        jogar_novamente_btn.clicked.connect(self.escolher_modo)

        # ---------- Layout ----------

        layout.addStretch()

        layout.addWidget(titulo)

        layout.addSpacing(20)

        layout.addWidget(self.label_palavra_derrota)

        layout.addSpacing(40)

        layout.addWidget(jogar_novamente_btn, alignment=Qt.AlignCenter)

        layout.addStretch()

        pagina.setLayout(layout)

        return pagina



    # ============= INTERFACE VITÓRIA CONTRATEMPO =============

    def criar_interface_vitoria_contratempo(self):

        pagina = QWidget()

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 60, 20, 40)
        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignCenter)

        # ---------- Resultado ----------

        self.label_palavras_contratempo_vitoria = QLabel()

        self.label_palavras_contratempo_vitoria.setAlignment(
            Qt.AlignCenter
        )

        self.label_palavras_contratempo_vitoria.setFont(
            QFont("Arial", 12, QFont.Bold)
        )

        self.label_palavras_contratempo_vitoria.setStyleSheet(
            "color: white;"
        )

        # ---------- Histórico de palavras ----------

        self.label_historico_contratempo_vitoria = QLabel()

        self.label_historico_contratempo_vitoria.setAlignment(
            Qt.AlignCenter
        )

        self.label_historico_contratempo_vitoria.setFont(
            QFont("Arial", 11, QFont.Bold)
        )

        self.label_historico_contratempo_vitoria.setStyleSheet(
            "color: white;"
        )

        self.label_historico_contratempo_vitoria.setWordWrap(True)

        # ---------- Botão ----------

        jogar_novamente_btn = QPushButton(
            "Jogar novamente"
        )

        jogar_novamente_btn.setCursor(
            Qt.PointingHandCursor
        )

        jogar_novamente_btn.setFixedSize(
            170,
            48
        )

        jogar_novamente_btn.setStyleSheet("""
            QPushButton {
                background-color: #8B1E2D;
                color: white;
                border: none;
                border-radius: 24px;
                font-size: 16px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #A32135;
            }

            QPushButton:pressed {
                background-color: #6F1622;
            }
        """)

        jogar_novamente_btn.clicked.connect(
            self.escolher_modo
        )

        # ---------- Layout ----------

        layout.addStretch()

        layout.addWidget(
            self.label_palavras_contratempo_vitoria
        )

        layout.addSpacing(20)

        layout.addWidget(
            self.label_historico_contratempo_vitoria
        )

        layout.addSpacing(30)

        layout.addWidget(
            jogar_novamente_btn,
            alignment=Qt.AlignCenter
        )

        layout.addStretch()

        pagina.setLayout(layout)

        return pagina



    # ============= INTERFACE DERROTA CONTRATEMPO =============

    def criar_interface_derrota_contratempo(self):

        pagina = QWidget()

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 60, 20, 40)
        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignCenter)

        # ---------- Resultado ----------

        self.label_palavras_contratempo_derrota = QLabel()

        self.label_palavras_contratempo_derrota.setAlignment(
            Qt.AlignCenter
        )

        self.label_palavras_contratempo_derrota.setFont(
            QFont("Arial", 12, QFont.Bold)
        )

        self.label_palavras_contratempo_derrota.setStyleSheet(
            "color: white;"
        )

        # ---------- Histórico de palavras ----------

        self.label_historico_contratempo_derrota = QLabel()

        self.label_historico_contratempo_derrota.setAlignment(
            Qt.AlignCenter
        )

        self.label_historico_contratempo_derrota.setFont(
            QFont("Arial", 11, QFont.Bold)
        )

        self.label_historico_contratempo_derrota.setStyleSheet(
            "color: white;"
        )

        self.label_historico_contratempo_derrota.setWordWrap(True)

        # ---------- Botão ----------

        jogar_novamente_btn = QPushButton(
            "Jogar novamente"
        )

        jogar_novamente_btn.setCursor(
            Qt.PointingHandCursor
        )

        jogar_novamente_btn.setFixedSize(
            170,
            48
        )

        jogar_novamente_btn.setStyleSheet("""
            QPushButton {
                background-color: #8B1E2D;
                color: white;
                border: none;
                border-radius: 24px;
                font-size: 16px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #A32135;
            }

            QPushButton:pressed {
                background-color: #6F1622;
            }
        """)

        jogar_novamente_btn.clicked.connect(
            self.escolher_modo
        )

        # ---------- Layout ----------

        layout.addStretch()

        layout.addWidget(
            self.label_palavras_contratempo_derrota
        )

        layout.addSpacing(30)

        layout.addWidget(
            self.label_historico_contratempo_derrota
        )

        layout.addSpacing(30)

        layout.addWidget(
            jogar_novamente_btn,
            alignment=Qt.AlignCenter
        )

        layout.addStretch()

        pagina.setLayout(layout)

        return pagina





    # =====================================================
    # TABULEIROS
    # =====================================================

    # ============= TABULEIRO PALAVRO E CONTRATEMPO =============

    def criar_tabuleiro(self, tabuleiro):

        caixas = []

        for linha in range(6):

            linha_caixas = []

            for coluna in range(5):

                caixa = CaixaLetra()

                x = coluna * 64
                y = linha * 96

                caixa.move(x, y)

                caixa.setParent(tabuleiro)

                linha_caixas.append(caixa)

            caixas.append(linha_caixas)

        return caixas



    # ============= TABULEIRO PARELHA =============

    def criar_tabuleiro_parelha(self):

        self.caixas_esquerda = []
        self.caixas_direita = []

        # ---------- Tabuleiro Esquerdo ----------

        for linha in range(7):

            linha_caixas = []

            for coluna in range(5):

                caixa = CaixaLetraPequena()

                x = coluna * 32
                y = linha * 56

                caixa.move(x, y)

                caixa.setParent(self.tabuleiro_esquerdo)

                linha_caixas.append(caixa)

            self.caixas_esquerda.append(linha_caixas)

        # ---------- Tabuleiro Direito ----------

        for linha in range(7):

            linha_caixas = []

            for coluna in range(5):

                caixa = CaixaLetraPequena()

                x = coluna * 32
                y = linha * 56

                caixa.move(x, y)

                caixa.setParent(self.tabuleiro_direito)

                linha_caixas.append(caixa)

            self.caixas_direita.append(linha_caixas)



    # ============= TABULEIRO QUADRA =============

    def criar_tabuleiro_quadra(self):

        self.caixas_1 = []
        self.caixas_2 = []
        self.caixas_3 = []
        self.caixas_4 = []

        tabuleiros = [
            (self.tabuleiro_1, self.caixas_1),
            (self.tabuleiro_2, self.caixas_2),
            (self.tabuleiro_3, self.caixas_3),
            (self.tabuleiro_4, self.caixas_4)
        ]

        for tabuleiro, lista_caixas in tabuleiros:

            for linha in range(9):

                linha_caixas = []

                for coluna in range(5):

                    caixa = CaixaLetraPequena()

                    x = coluna * 32
                    y = linha * 35

                    caixa.move(x, y)

                    caixa.setParent(tabuleiro)

                    linha_caixas.append(caixa)

                lista_caixas.append(linha_caixas)



    # =====================================================
    # LÓGICA DE JOGO
    # =====================================================

    # ============= LÓGICAS COMUNS ENTRE MODOS =============

    """
    ----- ÍNDICE -----

    - INICIAR UMA NOVA PARTIDA 
    - CAPTAR O TECLADO 
    - ESCREVER LETRAS 
    - APAGAR LETRAS 
    - VALIDAR TENTATIVA 
    - VALIDAR PALAVRA 
    - AVANÇAR PARA A PRÓXIMA TENTATIVA 
    - VERIFICAR VITÓRIA 
    - VERIFICAR DERROTA 
    - NORMALIZAR PALAVRA 
    - RESOLVER PALAVRA 

    """



    # ---------- INICIAR UMA NOVA PARTIDA ----------

    def nova_partida(self):

        if self.modo_jogo == "parelha":

            self.label_mensagem_parelha.setText("")

        elif self.modo_jogo == "quadra":

            self.label_mensagem_quadra.setText("")

        elif self.modo_jogo == "contratempo":

            self.label_mensagem_contratempo.setText("")

        else:

            self.label_mensagem.setText("")

        if self.modo_jogo == "parelha":

            self.palavra_resposta_esquerda = random.choice(
                self.respostas
            )

            while True:

                self.palavra_resposta_direita = random.choice(
                    self.respostas
                )

                if (
                    self.palavra_resposta_direita
                    !=
                    self.palavra_resposta_esquerda
                ):
                    break

        elif self.modo_jogo == "quadra":

            self.palavras_quadra = []

            while len(self.palavras_quadra) < 4:

                palavra = random.choice(
                    self.respostas
                )

                if palavra not in self.palavras_quadra:

                    self.palavras_quadra.append(
                        palavra
                    )

        elif self.modo_jogo == "contratempo":

            self.palavras_contratempo = list(
                self.respostas
            )

            self.palavras_acertadas_contratempo = []

            self.historico_contratempo = []

            self.palavra_resposta = random.choice(
                self.palavras_contratempo
            )

            self.palavras_contratempo.remove(
                self.palavra_resposta
            )

            self.historico_contratempo.append(
                {
                    "palavra": self.palavra_resposta,
                    "acertada": False
                }
            )

        else:

            self.palavra_resposta = random.choice(
                self.respostas
            )

        self.tentativa_atual = 0
        self.coluna_atual = 0
        self.jogo_terminado = False
        self.animacao = False

        if self.modo_jogo == "parelha":

            self.esquerda_resolvida = False
            self.direita_resolvida = False

        elif self.modo_jogo == "quadra":

            self.quadra_resolvida = [

                False,
                False,
                False,
                False

            ]

        if self.modo_jogo == "parelha":

            for linha in self.caixas_esquerda:

                for caixa in linha:

                    caixa.limpar()

            for linha in self.caixas_direita:

                for caixa in linha:

                    caixa.limpar()

        elif self.modo_jogo == "quadra":

            for grelha in [

                self.caixas_1,
                self.caixas_2,
                self.caixas_3,
                self.caixas_4

            ]:

                for linha in grelha:

                    for caixa in linha:

                        caixa.limpar()

        elif self.modo_jogo == "palavro":

            for linha in self.caixas_palavro:
                for caixa in linha:
                    caixa.limpar()

        elif self.modo_jogo == "contratempo":

            for linha in self.caixas_contratempo:
                for caixa in linha:
                    caixa.limpar()



    # ---------- CAPTAR O TECLADO ----------

    def keyPressEvent(self, event):     

        if self.stack.currentWidget() not in (
            self.interface_jogo,
            self.interface_parelha,
            self.interface_quadra,
            self.interface_contratempo,
        ):
            return

        if self.jogo_terminado:
            return
        
        if self.animacao:
            return

        texto = event.text().upper()

        if texto.isalpha() and len(texto) == 1:
            self.escrever_letra(texto)

        elif event.key() == Qt.Key_Backspace:
            self.apagar_letra()

        elif event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.validar_tentativa()



    # ---------- ESCREVER LETRAS ----------

    def escrever_letra(self, letra):      

        if self.modo_jogo == "parelha":

            self.label_mensagem_parelha.setText("")

        elif self.modo_jogo == "quadra":

            self.label_mensagem_quadra.setText("")

        elif self.modo_jogo == "contratempo":

            self.label_mensagem_contratempo.setText("")

        else:

            self.label_mensagem.setText("")

        if self.coluna_atual >= 5:
            return

        # ---------- Parelha ----------

        if self.modo_jogo == "parelha":

            if not self.esquerda_resolvida:

                caixa = self.caixas_esquerda[
                    self.tentativa_atual
                ][
                    self.coluna_atual
                ]

                caixa.escrever(letra)
                caixa.animar_pop()

            if not self.direita_resolvida:

                caixa = self.caixas_direita[
                    self.tentativa_atual
                ][
                    self.coluna_atual
                ]

                caixa.escrever(letra)
                caixa.animar_pop()

        # ---------- Quadra ----------

        elif self.modo_jogo == "quadra":

            tabuleiros = [

                self.caixas_1,
                self.caixas_2,
                self.caixas_3,
                self.caixas_4

            ]

            for indice, tabuleiro in enumerate(tabuleiros):

                if self.quadra_resolvida[indice]:
                    continue

                caixa = tabuleiro[
                    self.tentativa_atual
                ][
                    self.coluna_atual
                ]

                caixa.escrever(letra)

                caixa.animar_pop()

        # ---------- Palavro ----------

        elif self.modo_jogo == "palavro":

            caixa = self.caixas_palavro[
                self.tentativa_atual
            ][
                self.coluna_atual
            ]

            caixa.escrever(letra)

            caixa.animar_pop()

        # ---------- Contratempo ----------

        elif self.modo_jogo == "contratempo":

            caixa = self.caixas_contratempo[
                self.tentativa_atual
            ][
                self.coluna_atual
            ]

            caixa.escrever(letra)

            caixa.animar_pop()

        self.coluna_atual += 1



    # ---------- APAGAR LETRAS ----------

    def apagar_letra(self):

        if self.modo_jogo == "parelha":

            self.label_mensagem_parelha.setText("")

        elif self.modo_jogo == "quadra":

            self.label_mensagem_quadra.setText("")

        elif self.modo_jogo == "contratempo":

            self.label_mensagem_contratempo.setText("")

        else:

            self.label_mensagem.setText("")

        if self.coluna_atual == 0:
            return

        self.coluna_atual -= 1

        # ---------- Parelha ----------

        if self.modo_jogo == "parelha":

            if not self.esquerda_resolvida:

                caixa = self.caixas_esquerda[
                    self.tentativa_atual
                ][
                    self.coluna_atual
                ]

                caixa.apagar()

            if not self.direita_resolvida:

                caixa = self.caixas_direita[
                    self.tentativa_atual
                ][
                    self.coluna_atual
                ]

                caixa.apagar()

        # ---------- Quadra ----------

        elif self.modo_jogo == "quadra":

            tabuleiros = [

                self.caixas_1,
                self.caixas_2,
                self.caixas_3,
                self.caixas_4

            ]

            for indice, tabuleiro in enumerate(tabuleiros):

                if self.quadra_resolvida[indice]:
                    continue

                caixa = tabuleiro[
                    self.tentativa_atual
                ][
                    self.coluna_atual
                ]

                caixa.apagar()

        # ---------- Palavro ----------

        elif self.modo_jogo == "palavro":

            caixa = self.caixas_palavro[
                self.tentativa_atual
            ][
                self.coluna_atual
            ]

            caixa.apagar()

        # ---------- Contratempo ----------

        elif self.modo_jogo == "contratempo":

            caixa = self.caixas_contratempo[
                self.tentativa_atual
            ][
                self.coluna_atual
            ]

            caixa.apagar()



    # ---------- VALIDAR TENTATIVA ----------

    def validar_tentativa(self):

        if self.coluna_atual < 5:
            return

        tentativa = ""

        if self.modo_jogo == "parelha":

            caixas = (
                self.caixas_direita
                if self.esquerda_resolvida
                else self.caixas_esquerda
            )

            for caixa in caixas[self.tentativa_atual]:
                tentativa += caixa.text()

        elif self.modo_jogo == "quadra":

            tentativa = self.ler_tentativa_quadra()

        elif self.modo_jogo == "palavro":

            for caixa in self.caixas_palavro[
                self.tentativa_atual
            ]:

                tentativa += caixa.text()

        elif self.modo_jogo == "contratempo":

            for caixa in self.caixas_contratempo[
                self.tentativa_atual
            ]:

                tentativa += caixa.text()

        tentativa = self.resolver_palavra(tentativa)

        if tentativa is None:

            self.animacao = True

            self.animar_shake_linha()

            if self.modo_jogo == "parelha":

                self.label_mensagem_parelha.setText(
                    "Palavra inválida"
                )

            elif self.modo_jogo == "quadra":

                self.label_mensagem_quadra.setText(
                    "Palavra inválida"
                )

            elif self.modo_jogo == "contratempo":

                self.label_mensagem_contratempo.setText(
                    "Palavra inválida"
                )

            else:

                self.label_mensagem.setText(
                    "Palavra inválida"
                )

            QTimer.singleShot(
                320,
                lambda: setattr(self, "animacao", False)
            )

            return

        if self.modo_jogo == "parelha":

            if not self.esquerda_resolvida:

                for i, letra in enumerate(tentativa):

                    self.caixas_esquerda[
                        self.tentativa_atual
                    ][
                        i
                    ].setText(letra)

            if not self.direita_resolvida:

                for i, letra in enumerate(tentativa):

                    self.caixas_direita[
                        self.tentativa_atual
                    ][
                        i
                    ].setText(letra)

        elif self.modo_jogo == "palavro":

            for i, letra in enumerate(tentativa):

                self.caixas_palavro[
                    self.tentativa_atual
                ][
                    i
                ].setText(letra)

        elif self.modo_jogo == "contratempo":

            for i, letra in enumerate(tentativa):

                self.caixas_contratempo[
                    self.tentativa_atual
                ][
                    i
                ].setText(letra)

        elif self.modo_jogo == "quadra":

            self.escrever_palavra_quadra(tentativa)

        if self.modo_jogo == "parelha":

            resultado_esquerda, resultado_direita = (
                self.comparar_resposta_parelha(tentativa)
            )

            self.colorir_tentativa_parelha(
                resultado_esquerda,
                resultado_direita
            )

            QTimer.singleShot(
                2700,
                lambda: self.finalizar_tentativa_parelha(
                    tentativa,
                    resultado_esquerda,
                    resultado_direita
                )
            )

        elif self.modo_jogo == "quadra":

            resultados = self.comparar_resposta_quadra(
                tentativa
            )

            self.colorir_tentativa_quadra(
                resultados
            )

            QTimer.singleShot(

                2700,

                lambda: self.finalizar_tentativa_quadra(
                    tentativa,
                    resultados
                )

            )

        elif self.modo_jogo == "contratempo":

            resultado = self.comparar_resposta(
                tentativa
            )

            self.colorir_tentativa(
                resultado
            )

            QTimer.singleShot(
                2700,
                lambda: self.finalizar_tentativa_contratempo(
                    tentativa
                )
            )

        else:

            resultado = self.comparar_resposta(
                tentativa
            )

            self.colorir_tentativa(
                resultado
            )

            QTimer.singleShot(
                2700,
                lambda: self.finalizar_tentativa(
                    tentativa
                )
            )



    # ---------- VALIDAR PALAVRA ----------

    def validar_palavra(self, tentativa):

        with open("dicionario.txt", "r", encoding="utf-8") as ficheiro:

            palavras_validas = {
                palavra.strip().upper()
                for palavra in ficheiro
                if palavra.strip()
            }

        return tentativa in palavras_validas



    # ---------- AVANÇAR PARA A PRÓXIMA TENTATIVA ----------

    def avancar_tentativa(self):

        self.tentativa_atual += 1
        self.coluna_atual = 0



    # ---------- VERIFICAR VITÓRIA ----------

    def verificar_vitoria(self, tentativa):

        if tentativa == self.palavra_resposta:

            self.jogo_terminado = True

            self.label_palavra_vitoria.setText(
                f"A palavra era: {self.palavra_resposta}"
            )

            self.animar_vitoria()

            QTimer.singleShot(1200, lambda: self.stack.setCurrentWidget(self.interface_vitoria))

            return True

        return False



    # ---------- VERIFICAR DERROTA ----------

    def verificar_derrota(self):

        if self.tentativa_atual >= 6:

            self.jogo_terminado = True

            self.label_palavra_derrota.setText(
                f"A palavra era: {self.palavra_resposta}"
            )

            QTimer.singleShot(1200, lambda: self.stack.setCurrentWidget(self.interface_derrota))

            return True

        return False



    # ---------- NORMALIZAR PALAVRA ----------

    def normalizar_palavra(self, palavra):

        tabela = str.maketrans(
            "ÁÀÂÃÉÊÍÓÔÕÚÜÇ",
            "AAAAEEIOOOUUC"
        )

        return palavra.translate(tabela)



    # ---------- RESOLVER PALAVRA ----------

    def resolver_palavra(self, palavra):

        palavra = palavra.upper()

        # ---------- Palavro / Contratempo ----------

        if self.modo_jogo in ("palavro", "contratempo"):

            if (
                self.normalizar_palavra(palavra)
                ==
                self.normalizar_palavra(self.palavra_resposta)
            ):

                return self.palavra_resposta

        # ---------- Parelha ----------

        elif self.modo_jogo == "parelha":    

            if (
                self.normalizar_palavra(palavra)
                ==
                self.normalizar_palavra(self.palavra_resposta_esquerda)
            ):

                return self.palavra_resposta_esquerda

            if (
                self.normalizar_palavra(palavra)
                ==
                self.normalizar_palavra(self.palavra_resposta_direita)
            ):

                return self.palavra_resposta_direita

        # ---------- Quadra ----------

        elif self.modo_jogo == "quadra":

            for palavra_resposta in self.palavras_quadra:

                if (

                    self.normalizar_palavra(palavra)
                    ==
                    self.normalizar_palavra(palavra_resposta)

                ):

                    return palavra_resposta

        # ---------- Dicionário ----------

        if palavra in self.dicionario:

            return palavra

        palavra_normalizada = self.normalizar_palavra(palavra)

        for candidata in self.dicionario:

            if self.normalizar_palavra(candidata) == palavra_normalizada:

                return candidata

        return None





    # ============= LÓGICAS INDIVIDUAIS =============

    """
    ----- ÍNDICE -----

    - PALAVRO / CONTRATEMPO 
        - Finalizar Tentativa
        - Comparar Resposta 
        - Colorir Tentativa 
        - Colorir Caixa 
    - PARELHA 
        - Finalizar Tentativa
        - Comparar Resposta 
        - Colorir Tentativa 
        - Colorir Caixa 
    - QUADRA 
        - Finalizar Tentativa
        - Comparar Resposta 
        - Colorir Tentativa 
        - Colorir Caixa 
        - Tabuleiros ativos 
        - Ler Tentativa 
        - Escrever Palavra 
    - CONTRATEMPO 
        - Escolher Próxima Palavra 
        - Finalizar Tentativa
        - Iniciar Próxima Palavra
        - Atualizar Tempo 
        - Terminar Partida 
        - Atualizar Histórico  
    """

    # ===================================
    #    --- PALAVRO / CONTRATEMPO ---
    # ===================================

    # ---------- FINALIZAR TENTATIVA (PALAVRO / CONTRATEMPO) ----------

    def finalizar_tentativa(self, tentativa):

        self.animacao = False

        if self.verificar_vitoria(tentativa):
            return

        self.avancar_tentativa()

        if self.verificar_derrota():
            return



    # ---------- COMPARAR COM A RESPOSTA (PALAVRO / CONTRATEMPO) ----------

    def comparar_resposta(self, tentativa):

        resultado = ["cinzento"] * 5

        resposta = list(
            self.normalizar_palavra(self.palavra_resposta)
        )

        tentativa = list(
            self.normalizar_palavra(tentativa)
        )

        for i in range(5):

            if tentativa[i] == resposta[i]:

                resultado[i] = "verde"

                resposta[i] = None
                tentativa[i] = None

        for i in range(5):

            if tentativa[i] is None:
                continue

            if tentativa[i] in resposta:

                resultado[i] = "amarelo"

                indice = resposta.index(tentativa[i])
                resposta[indice] = None

        return resultado



    # ---------- COLORIR TENTATIVA (PALAVRO / CONTRATEMPO) ----------

    def colorir_tentativa(self, resultado):

        self.animacao = True

        for coluna, cor in enumerate(resultado):

            QTimer.singleShot(
                (coluna + 1) * 500,
                lambda c=coluna, cor=cor: self.colorir_caixa(
                    c,
                    cor,
                    self.modo_jogo
                )
            )


    # ---------- COLORIR CAIXA (PALAVRO / CONTRATEMPO) ----------

    def colorir_caixa(self, coluna, cor, modo):

        if modo == "palavro":

            caixa = self.caixas_palavro[
                self.tentativa_atual
            ][
                coluna
            ]

        elif modo == "contratempo":

            caixa = self.caixas_contratempo[
                self.tentativa_atual
            ][
                coluna
            ]

        else:

            return

        caixa.mudar_cor(cor)




    # ===================================
    #           --- PARELHA ---
    # ===================================

    # ---------- FINALIZAR TENTATIVA (PARELHA) ----------

    def finalizar_tentativa_parelha(

        self,

        tentativa,
        resultado_esquerda,
        resultado_direita

    ):

        self.animacao = False

        # ---------- Coluna Esquerda ----------

        if (
            not self.esquerda_resolvida
            and
            tentativa == self.palavra_resposta_esquerda
        ):
            self.esquerda_resolvida = True

            self.animar_vitoria_parelha(
                "esquerda"
            )

        # ---------- Coluna Direita ----------

        if (
            not self.direita_resolvida
            and
            tentativa == self.palavra_resposta_direita
        ):

            self.direita_resolvida = True

            self.animar_vitoria_parelha(
                "direita"
            )

        # ---------- Vitória ----------

        if self.esquerda_resolvida and self.direita_resolvida:

            self.jogo_terminado = True

            self.label_palavra_vitoria.setText(

                "As palavras eram:\n\n"

                f"{self.palavra_resposta_esquerda}"
                "    "
                f"{self.palavra_resposta_direita}"

            )

            QTimer.singleShot(
                1200,
                lambda: self.stack.setCurrentWidget(
                    self.interface_vitoria
                )
            )

            return

        self.avancar_tentativa()

        # ---------- Derrota ----------

        if self.tentativa_atual >= 7:

            self.jogo_terminado = True

            self.label_palavra_derrota.setText(

                "As palavras eram:\n\n"

                f"{self.palavra_resposta_esquerda}"
                "    "
                f"{self.palavra_resposta_direita}"

            )

            QTimer.singleShot(

                1200,

                lambda: self.stack.setCurrentWidget(
                    self.interface_derrota
                )

            )


    # ---------- COMPARAR COM AS RESPOSTAS (PARELHA) ----------

    def comparar_resposta_parelha(self, tentativa):

        resultado_esquerda = ["cinzento"] * 5
        resultado_direita = ["cinzento"] * 5

        # ---------- Esquerda ----------

        resposta = list(
            self.normalizar_palavra(
                self.palavra_resposta_esquerda
            )
        )

        letras = list(
            self.normalizar_palavra(
                tentativa
            )
        )

        for i in range(5):

            if letras[i] == resposta[i]:

                resultado_esquerda[i] = "verde"

                resposta[i] = None
                letras[i] = None

        for i in range(5):

            if letras[i] is None:
                continue

            if letras[i] in resposta:

                resultado_esquerda[i] = "amarelo"

                indice = resposta.index(letras[i])
                resposta[indice] = None

        # ---------- Direita ----------

        resposta = list(
            self.normalizar_palavra(
                self.palavra_resposta_direita
            )
        )

        letras = list(
            self.normalizar_palavra(
                tentativa
            )
        )

        for i in range(5):

            if letras[i] == resposta[i]:

                resultado_direita[i] = "verde"

                resposta[i] = None
                letras[i] = None

        for i in range(5):

            if letras[i] is None:
                continue

            if letras[i] in resposta:

                resultado_direita[i] = "amarelo"

                indice = resposta.index(letras[i])
                resposta[indice] = None

        return resultado_esquerda, resultado_direita



    # ---------- COLORIR TENTATIVA (PARELHA) ----------

    def colorir_tentativa_parelha(

        self,

        resultado_esquerda,
        resultado_direita

    ):

        self.animacao = True

        for coluna in range(5):

            QTimer.singleShot(

                (coluna + 1) * 500,

                lambda c=coluna: self.colorir_caixa_parelha(

                    c,

                    resultado_esquerda[c],
                    resultado_direita[c]

                )

            )



    # ---------- COLORIR CAIXA (PARELHA) ----------

    def colorir_caixa_parelha(

        self,

        coluna,
        cor_esquerda,
        cor_direita

    ):

        if not self.esquerda_resolvida:

            caixa = self.caixas_esquerda[
                self.tentativa_atual
            ][
                coluna
            ]

            caixa.mudar_cor(cor_esquerda)

        if not self.direita_resolvida:

            caixa = self.caixas_direita[
                self.tentativa_atual
            ][
                coluna
            ]

            caixa.mudar_cor(cor_direita)






    # ===================================
    #            --- QUADRA ---
    # ===================================

    # ---------- FINALIZAR TENTATIVA (QUADRA) ----------

    def finalizar_tentativa_quadra(

        self,

        tentativa,
        resultados

    ):

        self.animacao = False

        # ---------- Verificar palavras resolvidas ----------

        for indice, palavra in enumerate(self.palavras_quadra):

            if (

                not self.quadra_resolvida[indice]
                and
                tentativa == palavra

            ):

                self.quadra_resolvida[indice] = True

                self.animar_vitoria_quadra(indice)

        # ---------- Vitória ----------

        if all(self.quadra_resolvida):

            self.jogo_terminado = True

            self.label_palavra_vitoria.setText(

                "As palavras eram:\n\n"

                f"{self.palavras_quadra[0]}    {self.palavras_quadra[1]}\n"
                f"{self.palavras_quadra[2]}    {self.palavras_quadra[3]}"

            )

            QTimer.singleShot(

                1200,

                lambda: self.stack.setCurrentWidget(
                    self.interface_vitoria
                )

            )

            return

        # ---------- Próxima Linha ----------

        self.avancar_tentativa()

        # ---------- Derrota ----------

        if self.tentativa_atual >= 9:

            self.jogo_terminado = True

            self.label_palavra_derrota.setText(

                "As palavras eram:\n\n"

                f"{self.palavras_quadra[0]}    {self.palavras_quadra[1]}\n"
                f"{self.palavras_quadra[2]}    {self.palavras_quadra[3]}"

            )

            QTimer.singleShot(

                1200,

                lambda: self.stack.setCurrentWidget(
                    self.interface_derrota
                )

            )



    # ---------- COMPARAR COM AS RESPOSTAS (QUADRA) ----------

    def comparar_resposta_quadra(self, tentativa):

        resultados = []

        for indice in self.tabuleiros_ativos_quadra():

            resposta = list(

                self.normalizar_palavra(

                    self.palavras_quadra[indice]

                )

            )

            letras = list(

                self.normalizar_palavra(

                    tentativa

                )

            )

            resultado = ["cinzento"] * 5

            # ---------- Verdes ----------

            for i in range(5):

                if letras[i] == resposta[i]:

                    resultado[i] = "verde"

                    resposta[i] = None
                    letras[i] = None

            # ---------- Amarelos ----------

            for i in range(5):

                if letras[i] is None:
                    continue

                if letras[i] in resposta:

                    resultado[i] = "amarelo"

                    resposta[
                        resposta.index(letras[i])
                    ] = None

            resultados.append(

                (

                    indice,
                    resultado

                )

            )

        return resultados



    # ---------- COLORIR TENTATIVA (QUADRA) ----------

    def colorir_tentativa_quadra(self, resultados):

        self.animacao = True

        for coluna in range(5):

            QTimer.singleShot(

                (coluna + 1) * 500,

                lambda c=coluna: self.colorir_caixa_quadra(

                    c,

                    resultados

                )

            )



    # ---------- COLORIR CAIXA (QUADRA) ----------

    def colorir_caixa_quadra(

        self,

        coluna,
        resultados

    ):

        tabuleiros = [

            self.caixas_1,
            self.caixas_2,
            self.caixas_3,
            self.caixas_4

        ]

        for indice_tabuleiro, resultado in resultados:

            if not self.quadra_resolvida[indice_tabuleiro]:

                caixa = tabuleiros[
                    indice_tabuleiro
                ][
                    self.tentativa_atual
                ][
                    coluna
                ]

                caixa.mudar_cor(
                    resultado[coluna]
                )



    # ---------- TABULEIROS ATIVOS (QUADRA) ----------

    def tabuleiros_ativos_quadra(self):

        return [

            indice

            for indice, resolvida in enumerate(
                self.quadra_resolvida
            )

            if not resolvida

        ]



    # ---------- LER TENTATIVA (QUADRA) ----------

    def ler_tentativa_quadra(self):

        ativos = self.tabuleiros_ativos_quadra()

        if not ativos:
            return ""

        tabuleiros = [

            self.caixas_1,
            self.caixas_2,
            self.caixas_3,
            self.caixas_4

        ]

        tentativa = ""

        for caixa in tabuleiros[
            ativos[0]
        ][
            self.tentativa_atual
        ]:

            tentativa += caixa.text()

        return tentativa



    # ---------- ESCREVER PALAVRA (QUADRA) ----------

    def escrever_palavra_quadra(self, palavra):

        tabuleiros = [

            self.caixas_1,
            self.caixas_2,
            self.caixas_3,
            self.caixas_4

        ]

        for indice in self.tabuleiros_ativos_quadra():

            for coluna, letra in enumerate(palavra):

                tabuleiros[
                    indice
                ][
                    self.tentativa_atual
                ][
                    coluna
                ].setText(letra)
    




    # ===================================
    #    --- CONTRATEMPO ---
    # ===================================

    # ---------- ESCOLHER PRÓXIMA PALAVRA (CONTRATEMPO) ----------

    def escolher_proxima_palavra_contratempo(self):

        if not self.palavras_contratempo:

            return False

        self.palavra_resposta = random.choice(
            self.palavras_contratempo
        )

        self.palavras_contratempo.remove(
            self.palavra_resposta
        )

        self.historico_contratempo.append(
            {
                "palavra": self.palavra_resposta,
                "acertada": False
            }
        )

        return True



    # ---------- FINALIZAR TENTATIVA (CONTRATEMPO) ----------

    def finalizar_tentativa_contratempo(self, tentativa):

        self.animacao = False

        # ---------- Palavra acertada ----------

        if tentativa == self.palavra_resposta:

            self.palavras_acertadas_contratempo.append(
                tentativa
            )

            self.historico_contratempo[-1]["acertada"] = True

            self.animacao = True

            QTimer.singleShot(
                1000,
                self.iniciar_proxima_palavra_contratempo
            )

            return

        # ---------- Palavra falhada ----------

        if self.tentativa_atual >= 5:

            self.animacao = True

            self.label_mensagem_contratempo.setText(
                "Tentativa falhada, a começar próxima"
            )

            QTimer.singleShot(
                2000,
                self.iniciar_proxima_palavra_contratempo
            )

            return

        # ---------- Próxima tentativa ----------

        self.avancar_tentativa()



    # ---------- INICIAR PRÓXIMA PALAVRA (CONTRATEMPO) ----------

    def iniciar_proxima_palavra_contratempo(self):

        self.label_mensagem_contratempo.setText("")

        self.tentativa_atual = 0
        self.coluna_atual = 0

        for linha in self.caixas_contratempo:

            for caixa in linha:

                caixa.limpar()

        if not self.escolher_proxima_palavra_contratempo():

            self.terminar_contratempo()

            return

        self.animacao = False



    # ---------- ATUALIZAR TEMPO (CONTRATEMPO) ----------

    def atualizar_tempo_contratempo(self):

        self.tempo_restante_contratempo -= 1

        minutos = self.tempo_restante_contratempo // 60
        segundos = self.tempo_restante_contratempo % 60

        self.label_tempo_contratempo.setText(
            f"{minutos:02d}:{segundos:02d}"
        )

        if self.tempo_restante_contratempo <= 0:

            self.tempo_restante_contratempo = 0

            self.label_tempo_contratempo.setText(
                "00:00"
            )

            self.terminar_contratempo()



    # ---------- TERMINAR PARTIDA (CONTRATEMPO) ----------

    def terminar_contratempo(self):

        self.timer_contratempo.stop()

        self.jogo_terminado = True
        self.animacao = False

        quantidade = len(
            self.palavras_acertadas_contratempo
        )

        if quantidade == 1:

            texto_resultado = "Acertaste 1 palavra"

        else:

            texto_resultado = (
                f"Acertaste {quantidade} palavras"
            )

        self.atualizar_historico_contratempo()

        if quantidade > 0:

            self.label_palavras_contratempo_vitoria.setText(
                texto_resultado
            )

            QTimer.singleShot(
                1200,
                lambda: self.stack.setCurrentWidget(
                    self.interface_vitoria_contratempo
                )
            )

        else:

            self.label_palavras_contratempo_derrota.setText(
                texto_resultado
            )

            QTimer.singleShot(
                1200,
                lambda: self.stack.setCurrentWidget(
                    self.interface_derrota_contratempo
                )
            )



    # ---------- ATUALIZAR HISTÓRICO (CONTRATEMPO) ----------

    def atualizar_historico_contratempo(self):

        linhas = []

        for indice, item in enumerate(
            self.historico_contratempo,
            start=1
        ):

            palavra = item["palavra"]

            if item["acertada"]:

                cor = "white"

            else:

                cor = "#666666"

            linhas.append(
                f"<span style='color:{cor};'>"
                f"{indice}. {palavra}"
                f"</span>"
            )

        texto = "<br>".join(linhas)

        self.label_historico_contratempo_vitoria.setText(
            texto
        )

        self.label_historico_contratempo_derrota.setText(
            texto
        )





    # =====================================================
    # ANIMAÇÕES
    # =====================================================

    # ---------- ANIMAR VITÓRIA (PALAVRO / CONTRATEMPO) ----------

    def animar_vitoria(self):

        if self.modo_jogo == "palavro":

            linha = self.caixas_palavro[
                self.tentativa_atual
            ]

        elif self.modo_jogo == "contratempo":

            linha = self.caixas_contratempo[
                self.tentativa_atual
            ]

        else:

            return

        for indice, caixa in enumerate(linha):

            QTimer.singleShot(
                indice * 100,
                caixa.animar_onda
            )



    # ---------- ANIMAR VITÓRIA (PARELHA) ----------

    def animar_vitoria_parelha(self, lado):

        if lado == "esquerda":

            linha = self.caixas_esquerda[
                self.tentativa_atual
            ]

        else:

            linha = self.caixas_direita[
                self.tentativa_atual
            ]

        for coluna, caixa in enumerate(linha):

            QTimer.singleShot(

                coluna * 120,

                caixa.animar_onda

            )



    # ---------- ANIMAR VITÓRIA (QUADRA) ----------

    def animar_vitoria_quadra(self, indice):

        grelhas = [

            self.caixas_1,
            self.caixas_2,
            self.caixas_3,
            self.caixas_4

        ]

        linha = grelhas[indice][
            self.tentativa_atual
        ]

        for coluna, caixa in enumerate(linha):

            QTimer.singleShot(

                coluna * 120,

                caixa.animar_onda

            )



    # ---------- ANIMAR PALAVRA INVÁLIDA ----------

    def animar_shake_linha(self):

        # ---------- Parelha ----------

        if self.modo_jogo == "parelha":

            if not self.esquerda_resolvida:

                for caixa in self.caixas_esquerda[
                    self.tentativa_atual
                ]:

                    caixa.animar_shake()

            if not self.direita_resolvida:

                for caixa in self.caixas_direita[
                    self.tentativa_atual
                ]:

                    caixa.animar_shake()

        # ---------- Quadra ----------

        elif self.modo_jogo == "quadra":

            grelhas = [

                self.caixas_1,
                self.caixas_2,
                self.caixas_3,
                self.caixas_4

            ]

            for indice, grelha in enumerate(grelhas):

                if not self.quadra_resolvida[indice]:

                    for caixa in grelha[
                        self.tentativa_atual
                    ]:

                        caixa.animar_shake()

        # ---------- Palavro ----------

        elif self.modo_jogo == "palavro":

            for caixa in self.caixas_palavro[
                self.tentativa_atual
            ]:

                caixa.animar_shake()

        # ---------- Contratempo ----------

        elif self.modo_jogo == "contratempo":

            for caixa in self.caixas_contratempo[
                self.tentativa_atual
            ]:

                caixa.animar_shake()



    # ---------- PISCAR MENSAGEM (CONTRATEMPO) ----------

    def piscar_mensagem_contratempo(self):

        self.label_mensagem.setText(
            "Tentativa falhada, a começar próxima"
        )

        self.label_mensagem.setVisible(True)

        for tempo in range(250, 2000, 250):

            QTimer.singleShot(
                tempo,
                lambda: self.label_mensagem.setVisible(
                    not self.label_mensagem.isVisible()
                )
            )

        QTimer.singleShot(
            2000,
            lambda: self.label_mensagem.setVisible(False)
        )





    # =====================================================
    # NAVEGAÇÃO
    # =====================================================

    # ---------- INICIAR JOGO ----------

    def iniciar_jogo(self):

        self.stack.setCurrentWidget(
            self.interface_modos
        )



    # ---------- INICIAR MODOS ----------

    def iniciar_palavro(self):

        self.modo_jogo = "palavro"

        self.nova_partida()

        self.stack.setCurrentWidget(
            self.interface_jogo
        )

    def iniciar_parelha(self):

        self.modo_jogo = "parelha"

        self.nova_partida()

        self.stack.setCurrentWidget(
            self.interface_parelha
        )

    def iniciar_quadra(self):

        self.modo_jogo = "quadra"

        self.nova_partida()

        self.stack.setCurrentWidget(
            self.interface_quadra
        )

    def iniciar_contratempo(self):

        self.modo_jogo = "contratempo"

        self.nova_partida()

        self.tempo_restante_contratempo = 300

        self.label_tempo_contratempo.setText(
            "05:00"
        )

        self.timer_contratempo.start(1000)

        self.stack.setCurrentWidget(
            self.interface_contratempo
        )



    # ---------- JOGAR NOVAMENTE ----------

    def jogar_novamente(self):

        self.nova_partida()

        self.stack.setCurrentWidget(
            self.interface_jogo
        )

        self.interface_jogo.setFocus()



    # ---------- ESCOLHER MODO ----------

    def escolher_modo(self):

        self.stack.setCurrentWidget(
            self.interface_modos
        )





# =================================================================================================================================================================





"""
---------------------------------------------------------------- CLASS AUXILIAR CaixaLetra(QLabel) ----------------------------------------------------------------

----- ÍNDICE DA CLASS CaixaLetra(QLabel) -----

- CONFIGURAÇÃO DA CAIXA 
- COMPORTAMENTO DA CAIXA 
- ANIMAÇÕES 

"""



class CaixaLetra(QLabel):

    # =====================================================
    # CONFIGURAÇÃO DA CAIXA
    # ===================================================== 

    def __init__(self):
        super().__init__()

        self.posicao_original = None

        self.setFixedSize(60, 60)

        self.setAlignment(Qt.AlignCenter)

        self.setFont(QFont("Arial", 18, QFont.Bold))

        self.setStyleSheet("""
            QLabel{
                background-color: rgb(75,75,75);
                border-radius: 8px;
                color: white;
            }
        """)

        self.letra = ""

        self.cor = "normal"

        self.animacao = None

        self.animacao_shake = None

        self.animacao_pop = None



    # =====================================================
    # COMPORTAMENTO DA CAIXA
    # ===================================================== 

    # ---------- ALTERAR COR ----------

    def mudar_cor(self, cor):
        
        self.cor = cor

        cores = {
            "verde": "#4CAF50",
            "amarelo": "#C9B458",
            "cinzento": "#3A3A3C"
        }

        self.setStyleSheet(f"""
            QLabel {{
                background-color: {cores[cor]};
                border-radius: 8px;
                color: white;
            }}
        """)

    # ---------- LIMPAR ----------

    def limpar(self):

        self.setText("")

        self.setStyleSheet("""
            QLabel{
                background-color: rgb(75,75,75);
                border-radius: 8px;
                color: white;
            }
        """)

    # ---------- ESCREVER LETRA ----------

    def escrever(self, letra):
        self.letra = letra
        self.setText(letra)

    # ---------- APAGAR LETRA ----------

    def apagar(self):

        self.setText("")



    # =====================================================
    # ANIMAÇÕES
    # ===================================================== 

    # ---------- ANIMAR ONDA ----------

    def animar_onda(self):

        posicao = self.pos()

        self.animacao = QPropertyAnimation(self, b"pos")

        self.animacao.setDuration(220)

        self.animacao.setStartValue(posicao)

        self.animacao.setKeyValueAt(
            0.5,
            QPoint(posicao.x(), posicao.y() - 10)
        )

        self.animacao.setEndValue(posicao)

        self.animacao.setEasingCurve(QEasingCurve.OutQuad)

        self.animacao.start()

    # ---------- ANIMAR SHAKE ----------

    def animar_shake(self):

        posicao = self.pos()

        self.animacao_shake = QPropertyAnimation(self, b"pos")

        self.animacao_shake.setDuration(300)

        self.animacao_shake.setKeyValueAt(
            0.00,
            posicao
        )

        self.animacao_shake.setKeyValueAt(
            0.20,
            QPoint(posicao.x() - 6, posicao.y())
        )

        self.animacao_shake.setKeyValueAt(
            0.40,
            QPoint(posicao.x() + 6, posicao.y())
        )

        self.animacao_shake.setKeyValueAt(
            0.60,
            QPoint(posicao.x() - 6, posicao.y())
        )

        self.animacao_shake.setKeyValueAt(
            0.80,
            QPoint(posicao.x() + 6, posicao.y())
        )

        self.animacao_shake.setEndValue(posicao)

        self.animacao_shake.setEasingCurve(QEasingCurve.Linear)

        self.animacao_shake.start()


    # ---------- ANIMAR POP ----------

    def animar_pop(self):

        geometria = self.geometry()

        margem = 3

        geometria_pop = QRect(
            geometria.x() - margem,
            geometria.y() - margem,
            geometria.width() + margem * 2,
            geometria.height() + margem * 2
        )

        self.animacao_pop = QPropertyAnimation(
            self,
            b"geometry"
        )

        self.animacao_pop.setDuration(120)

        self.animacao_pop.setStartValue(geometria)

        self.animacao_pop.setKeyValueAt(
            0.5,
            geometria_pop
        )

        self.animacao_pop.setEndValue(geometria)

        self.animacao_pop.setEasingCurve(
            QEasingCurve.OutQuad
        )

        self.animacao_pop.start()





# ================================================================================================================================================================





"""
---------------------------------------------------------- CLASS AUXILIAR CaixaLetraPequena(CaixaLetra) ----------------------------------------------------------

----- ÍNDICE DA CLASS CaixaLetraPequena(CaixaLetra) -----

- INIT 

"""



class CaixaLetraPequena(CaixaLetra):

    def __init__(self):
        super().__init__()

        self.setFixedSize(30, 30)

        self.setFont(QFont("Arial", 14, QFont.Bold))