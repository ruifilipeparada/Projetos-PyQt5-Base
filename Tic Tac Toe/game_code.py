import random

class TicTacToe: 

    def __init__(self): 
        self.last_winner = None # guarda o último vencedor 
        self.last_player = None # guarda o último jogador (para casos de empate)
        self.reset() # utiliza o código abaixo

    def reset(self): 
        self.board = [""] * 9 # tabuleiro 3x3 vazio no início 
        self.winner = None # guarda o vencedor quando houver 
        self.game_over = False # indica se o jogo acabou 

        if self.last_winner is None and self.last_player is None: 
            self.current_player = random.choice(["X", "O"]) 
        elif self.last_winner is not None:
            self.current_player = self.last_winner
        else: 
            self.current_player = "O" if self.last_player == "X" else "X"

    def _is_valid_move(self, position):
        return 0 <= position < 9 and self.board[position] == "" and not self.game_over 

    def make_move(self, position): 
        if not self._is_valid_move(position):
            return False # jogada inválida 
        
        self.board[position] = self.current_player # aplica a jogada 

        self._check_winner() 

        if not self.winner:
            self._check_draw() 
        
        if not self.game_over:
            self._switch_player()
        else: # atualiza o histórico no final do jogo 
            if self.winner:
                self.last_winner = self.winner
                self.last_player = self.winner
            else:  # empate
                self.last_winner = None
                self.last_player = self.current_player

        return True 
    
    def _check_winner(self): 
        winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # colunas
        [0, 4, 8], [2, 4, 6]              # diagonais
    ]
        
        for combo in winning_combinations:
            a, b, c = combo
            if self.board[a] == self.board[b] == self.board[c] != "":
                self.winner = self.board[a]
                self.game_over = True
                return
            
    def _check_draw(self):
        if all(cell != "" for cell in self.board) and not self.winner:
            self.game_over = True 

    def _switch_player(self): 
        self.current_player = "O" if self.current_player == "X" else "X"

    

    # Getters para a interface 

    def get_board(self): 
        return self.board

    def get_current_player(self): 
        return self.current_player
    
    def is_game_over(self): 
        return self.game_over
    
    def get_winner(self): 
        return self.winner 