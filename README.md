# Analisador Léxico para LALG

## Índice

- [Introdução](#introdução)
- [Requisitos](#requisitos)
- [Detalhes de Implementação](#detalhes-de-implementação)
  - [Tokens](#tokens)
  - [Estrutura](#estrutura)
- [Uso](#uso)
- [Referências](#referências)

## Introdução

O Analisador Léxico para LALG é uma ferramenta desenvolvida em Python destinada à identificação e categorização de tokens em códigos-fonte escritos em LALG, retornando sua respectiva categoria (tipo) e valor.


## Requisitos
- Python 3.11
- Bibliotecas: 
  - `re`
  - `tkinter`

## Detalhes de Implementação

Implementei o uso de uma interface Tkinter para erros e da biblioteca re para processamento de expressões regulares. O programa importa os tokens do arquivo "tokens.py"e os usa como base para ler o código LALG fornecido.

### Tokens

A lista de tokens definidos no programa inclui:

- Palavras reservadas como `PROGRAM`, `VAR`, `BEGIN`, `END`, `READ`, `WRITE`, `IF`, `THEN`, `ELSE`, `WHILE`, `DO`, `INTEGER` e `REAL`.
- Identificadores, categorizados como `IDENTIFIER`.
- Números inteiros, categorizados como `NUMBER`.
- Números reais, categorizados como `REAL_NUMBER`.
- Operadores como adição, subtração, multiplicação e divisão, categorizados como `OPERATOR`.
- Pontuações, incluindo ponto e vírgula (`SEMICOLON`), vírgula (`COMMA`) e parênteses (`OPEN_PAR` e `CLOSE_PAR`).
- Comentários, categorizados como `COMMENT`.

### Estrutura

A estrutura principal do programa se baseia no uso de expressões regulares para definir padrões dos tokens, permitindo assim a identificação de cada token em uma dada entrada de texto. A função `lexer` tem a responsabilidade de analisar o texto e gerar uma lista dos tokens identificados.

## Uso

Para utilizar o Analisador Léxico, execute o script Python. Incluso no código, há um exemplo de código LALG que é analisado pelo lexer, com os tokens identificados sendo exibidos ao usuário. É esperado que o exemplo pré-pronto aponte um erro, mas que o terminal retorne alguns dos dados processados.

## Referências

Para aprofundamento e referências adicionais sobre o assunto, consultei as seguintes fontes:

- [Compiladores em Python](https://github.com/DoctorWkt/acwj) - Um guia passo a passo para criar um compilador em C, adaptável para Python.
- [Awesome Compilers](https://github.com/aalhour/awesome-compilers) - Uma extensa lista de recursos e ferramentas relacionados à teoria e prática de compiladores.
- [Expressões Regulares em Python](https://docs.python.org/3/library/re.html) - Documentação oficial do módulo `re` do Python, utilizado extensivamente neste projeto para trabalhar com expressões regulares.
- [Analisador Léxico com PLY por Bredstone](https://github.com/Bredstone/Analisador-Lexico-Python) - Um projeto mantido pelo usuário Bredstone, demonstrando um analisador léxico com base em PLY e Python 3.8.
