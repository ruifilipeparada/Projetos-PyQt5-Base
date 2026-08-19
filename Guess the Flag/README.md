# Guess the Flag

## Objetivo

Desenvolver um jogo em Python baseado no reconhecimento de **bandeiras de países**, utilizando uma interface gráfica criada com **PyQt5** e diferentes níveis de dificuldade.

---

## Descrição

O **Guess the Flag** é um jogo em que o jogador deve identificar o país correspondente à bandeira apresentada.

O jogo está dividido em cinco níveis de dificuldade:

* **Iniciante:** bandeiras de países mais conhecidos;
* **Fácil:** aumenta a variedade de bandeiras apresentadas;
* **Moderado:** inclui bandeiras menos óbvias;
* **Difícil:** apresenta um conjunto mais exigente de bandeiras;
* **Geógrafo:** inclui bandeiras de países menos conhecidos e exige um maior conhecimento geográfico.

As imagens das bandeiras são armazenadas em formato `.png`. Cada ficheiro utiliza uma sigla associada ao respetivo país, sendo essa correspondência definida no código do jogo.

---

## Estrutura

**Guess the Flag/**

* **mockup_iphone.py:** ficheiro utilizado como referência para a interface visual da aplicação
* **code.py:** contém a lógica do jogo, incluindo a associação entre as siglas das bandeiras e os respetivos países
* **main.py:** instancia a aplicação e inicia a sua execução
* **flags: ficheiros `.png` correspondentes às bandeiras utilizadas no jogo**

> **Nota:** a pasta `flags` foi carregada como ficheiro zip. Deve ser feita a sua descompressão, mantendo o nome `flags` e a estrutura de ficheiros incluídos.

---

## Linguagem e Ferramentas

* **Linguagem:** Python
* **Framework:** PyQt5
* **Editor:** VS Code
