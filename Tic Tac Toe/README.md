# Tic Tac Toe

## Objetivo

Desenvolver um pequeno jogo de **Tic Tac Toe** em Python com recurso ao **PyQt5**, permitindo a dois jogadores jogar numa interface gráfica adaptada a um mockup de iPhone.

O projeto foi desenvolvido como uma aplicação simples para explorar a criação de interfaces gráficas, interação com o utilizador e separação entre a lógica do jogo e a interface.

---

## Descrição

O jogo permite a dois jogadores introduzir os seus nomes e jogar uma partida de Tic Tac Toe.

No início de cada partida, o jogador que começa é escolhido aleatoriamente. Durante o jogo, a interface indica qual é o jogador atual e permite selecionar as posições disponíveis no tabuleiro.

A lógica do jogo encontra-se separada da interface gráfica, permitindo manter as regras do jogo independentes da implementação visual.

---

## Estrutura

**Tic Tac Toe/**

* **iphone_frame.py:** ficheiro responsável pelo mockup de iPhone onde a aplicação é apresentada.
* **game_code.py:** ficheiro que contém a classe `TicTacToe` e a lógica principal do jogo.
* **main.py:** ficheiro responsável pela interface gráfica, interação com o utilizador e execução da aplicação.

> **Nota:** os três ficheiros devem ser mantidos na mesma estrutura de pasta para que os imports e a execução do projeto funcionem corretamente.

---

## Linguagem e Ferramentas

* **Linguagem:** Python
* **Framework:** PyQt5
* **Editor:** VS Code
