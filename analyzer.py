import re #Biblioteca para expressões regulares
import tkinter as tk 
from tkinter import messagebox, simpledialog #Biblioteca para interface de aviso
from tokens import tokens #Importando as tokens do outro módulo

def lexer(input_text):
    pos = 0
    line = 1
    char_pos = 1
    while pos < len(input_text):
        match = None
        
        # Ignora espaços em branco, tabulações e novas linhas
        while pos < len(input_text) and input_text[pos] in ' \t\n':
            if input_text[pos] == '\n':
                line += 1
                char_pos = 1
            pos += 1

        for token_name, token_re in tokens.items():
            pattern = re.compile(token_re)
            match = pattern.match(input_text, pos)
            if match:
                value = match.group(0)
                if token_name != 'COMMENT':  # Ignorar comentários
                    yield (token_name, value)
                pos = match.end()
                break
        if not match and pos < len(input_text):
            # Mostra um popup de erro e para a análise
            root = tk.Tk()
            root.withdraw()  # Esconde a janela principal
            messagebox.showerror("Erro Léxico", f"Erro léxico na linha {line}, posição {char_pos}: {input_text[pos]}")
            root.destroy()
            return
        char_pos += len(match.group(0)) if match else 1  # Atualiza a posição do caractere na linha
2
def show_error_popup(message): #popup de erros
    root = tk.Tk()
    root.withdraw()  # esconde a janela principal
    messagebox.showerror("Erro Léxico", message)
    root.destroy()

def main():
    print("Analisador Léxico para LALG")
    print("-" * 40)
    print("Escolha uma opção:")
    print("1. Usar o código de amostra")
    print("2. Inserir seu próprio código")
    
    choice = input("Digite 1 ou 2: ")

    if choice == "1":
        code = """
        program exemplo;
        var a, b: integer;
        begin
            read(a, b);
            if a >= b then
                write(a);
            else
                write(b);
        end;
        """
    elif choice == "2":
        root = tk.Tk()
        root.withdraw()  # Esconde a janela principal
        code = simpledialog.askstring("Insira seu código", "Digite ou cole o código LALG abaixo:")
        root.destroy()
    else:
        print("Opção inválida.")
        return

    print("-" * 40)
    print("Tokens identificados:")
    for token in lexer(code):
        print(token)

if __name__ == "__main__":
    main()
