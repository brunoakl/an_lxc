# Analisador Léxico para LALG

## Índice

- [Introdução](#introdução)
- [Detalhes de Implementação](#detalhes-de-implementação)
  - [Tokens](#tokens)
  - [Estrutura](#estrutura)
- [Uso](#uso)
- [Referências](#referências)

## Introdução

O Analisador Léxico para LALG é um programa simples escrito em Python que identifica e categoriza tokens em um código-fonte LALG, retornando sua categoria (tipo) e valor.

## Detalhes de Implementação

### Tokens

Os tokens definidos são os seguintes:

- Palavras reservadas (`PROGRAM`, `VAR`, `BEGIN`, `END`, `READ`, `WRITE`, `IF`, `THEN`, `ELSE`, `WHILE`, `DO`, `INTEGER`, `REAL`)
- Identificadores (`IDENTIFIER`)
- Números inteiros (`NUMBER`)
- Números reais (`REAL_NUMBER`)
- Operadores (`OPERATOR`)
- Pontuações como ponto e vírgula (`SEMICOLON`), vírgula (`COMMA`), parênteses aberto (`OPEN_PAR`) e fechado (`CLOSE_PAR`)
- Comentários (`COMMENT`)

### Estrutura

O código utiliza expressões regulares para definir os padrões dos tokens e, assim, identificar cada token em uma entrada de texto. O método `lexer` é responsável por analisar o texto e gerar os tokens identificados.

## Uso

Para usar o Analisador Léxico, basta executar o programa em Python. O código inclui um exemplo de código LALG que será analisado pelo lexer, e os tokens identificados serão impressos na tela.

## Referências

Para quem deseja se aprofundar mais no tema ou buscar outras implementações e utilidades, recomendo os seguintes repositórios e fontes:

- [Compiladores em Python](https://github.com/DoctorWkt/acwj) - Este repositório oferece uma caminhada através da criação de um compilador em C, mas os princípios podem ser adaptados para Python.
   
- [Awesome Compilers](https://github.com/aalhour/awesome-compilers) - Uma lista abrangente de recursos e ferramentas relacionadas a compiladores.

- [Regular Expressions in Python](https://docs.python.org/3/library/re.html) - Documentação oficial sobre o módulo `re` do Python, utilizado neste código para trabalhar com expressões regulares.

- [Analisador Léxico com PLY por Bredstone](https://github.com/Bredstone/Analisador-Lexico-Python) - Este repositório, mantido pelo usuário Bredstone, contém um analisador léxico escrito em Python 3.8 utilizando a biblioteca PLY.

- **Compiladores: Princípios e Práticas** por Alfred V. Aho, Monica S. Lam, Ravi Sethi e Jeffrey D. Ullman - Este é um livro clássico no campo da teoria dos compiladores.

Ao explorar essas fontes, tive mais facilidade com o desenvolvimento deste projeto e pude entender melhor alguns conceitos do tema.
