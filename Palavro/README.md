# Palavro

## Objetivo

Desenvolver um jogo de palavras em Python, inspirado no conceito do Wordle, com diferentes modos de jogo e uma interface construída com PyQt5.

O objetivo principal foi criar uma aplicação completa e funcional, desde a lógica das partidas até à interface e às diferentes interações com o utilizador.

---

## Descrição

Para este projeto, desenvolvi uma aplicação de jogo de palavras com vários modos de jogo, cada um com regras e mecânicas próprias:

* **Palavro:** modo clássico de adivinhação de uma palavra em até 6 tentativas.
* **Parelha:** duas palavras são jogadas simultaneamente no mesmo tabuleiro.
* **Quadra:** quatro palavras são jogadas em paralelo.
* **Contratempo:** modo baseado em tempo, no qual o objetivo é acertar o maior número possível de palavras antes de o tempo terminar.

A aplicação inclui, entre outras funcionalidades:

* Validação de palavras através de um dicionário.
* Normalização de palavras, permitindo lidar com acentos e cedilhas.
* Feedback visual através de cores para letras corretas, presentes na palavra ou incorretas.
* Animações durante a escrita, validação e vitória.
* Navegação entre diferentes interfaces.
* Sistema de tentativas e condições de vitória/derrota.
* Histórico de palavras jogadas no modo Contratempo.
* Diferentes interfaces e lógicas específicas para cada modo de jogo.

Um dos principais objetivos durante o desenvolvimento foi manter as diferentes variantes do jogo organizadas, evitando duplicação desnecessária da lógica sempre que esta pudesse ser partilhada entre os vários modos.

> **Nota:** os ficheiros `.py` contêm índices no início das principais classes e blocos de lógica, de forma a facilitar a navegação pelo código.

---

## Estrutura

**Palavro/**

* **code_game.py:** ficheiro de desenvolvimento da aplicação, contendo a interface gráfica, lógica dos diferentes modos de jogo, validação de palavras, animações e navegação entre interfaces.
* **main.py:** ficheiro que executa a aplicação.
* **iphone_frame:** ficheiro que desenha um frame de telemóvel, que dá molde ao jogo. 
* **dicionario.txt:** ficheiro com as palavras utilizadas para validar as tentativas do utilizador.
* **respostas.txt:** ficheiro com as palavras sorteadas para cada partida. 

> **Nota:** é importante manter a estrutura da pasta e a localização do ficheiro `dicionario.txt`, uma vez que este é utilizado diretamente pela aplicação durante a validação das palavras.

---

## Linguagem e Ferramentas

* **Linguagem:** Python
* **Framework de interface gráfica:** PyQt5
* **Editor:** VS Code
* **Dados:** ficheiro `.txt`
* **Bibliotecas principais:** PyQt5, random, QTimer

---

## Objetivos futuros

Apesar de o projeto estar funcional, existem várias possibilidades de evolução:

* Adicionar novos modos de jogo.
* Criar níveis de dificuldade.
* Adicionar estatísticas permanentes das partidas.
* Guardar histórico de resultados.
* Melhorar a responsividade das interfaces.
* Adicionar efeitos sonoros.
* Criar um sistema de pontuação mais completo para o modo Contratempo.

---
