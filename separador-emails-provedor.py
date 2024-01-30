import colorama
import sys
import signal

def print_banner():
    print("+==================================================+")
    print("| Autor: Marcio Cruz                               |")
    print("| Sobre: SEPARADOR DE E-MAIL/PROVEDOR              |")
    print("|                                                  |")
    print("| Linkedin: linkedin.com/in/marciosecurity/        |")
    print("| Telegram: @eth0root                              |")
    print("+==================================================+")
    print()

def handle_ctrl_c(signal, frame):
    confirm = input("\nVocê pressionou Ctrl+C. Tem certeza de que deseja encerrar o script? (S/N): ").strip().lower()
    if confirm == 's':
        print("\nPrograma encerrado pelo usuário.")
        sys.exit(0)
    else:
        print("\nContinuando a execução do script...\n")

# Configurando o tratamento do sinal Ctrl+C
signal.signal(signal.SIGINT, handle_ctrl_c)

# Definir o encoding padrão para UTF-8
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

from colorama import Fore

colorama.init(autoreset=True)

providers = {
    "@globo.com.br": "globo.txt",
    "@gmail.com": "gmail.txt",
    "@outlook.com": "outlook.com.txt",
    "@yahoo.com": "yahoo.com.txt",
    "@yahoo.com.br": "yahoo.com.br.txt",
    "@bol.com.br": "bol.com.br.txt",
    "@hotmail.com": "hotmail.com.txt",
    "@aol.com": "aol.com.txt",
    "@zipmail.com.br": "zipmail.com.br.txt",
    "@terra.com.br": "terra.com.br.txt",
    "@uol.com.br": "uol.com.br.txt",
    "@ig.com.br": "ig.com.br.txt",
    # Adicione mais provedores, se necessário
}

def get_test():
    processed_items = set()  # Conjunto para armazenar itens processados
    while True:
        try:
            combo = input("Digite o caminho da lista de e-mails (.txt): -> ")
            
            while combo == "":
                print("\n\033[1;91mErro: O caminho da lista não pode ser vazio. Por favor, insira o caminho corretamente.\033[1;m\n")
                combo = input("Digite o caminho da lista de e-mails (.txt): -> ")

            with open(combo, "rb") as arquivo:
                file = arquivo.read().decode("latin-1")  # Decodifica a sequência de bytes usando a codificação "latin-1"
                file = file.splitlines()
                for line in file:
                    try:
                        for provider, filename in providers.items():
                            if provider in line.lower() and line not in processed_items:
                                with open(filename, 'a', encoding="utf8") as file2:
                                    file2.write(line + '\n')
                                processed_items.add(line)  # Adiciona o item ao conjunto de itens processados
                                print(f"+1   ->   {line}")
                                break
                        else:
                            with open('outros.txt', 'a', encoding="utf8") as file2:
                                file2.write(line + '\n')
                                processed_items.add(line)  # Adiciona o item ao conjunto de itens processados
                                print(f"+1   ->   {line}")
                    except Exception as e:
                        print(f"\n\nErro ao processar a linha -> {e}")

                input('\n               Processo Finalizado! Pressione ENTER Para Continuar!')
        except Exception as ee:
            print(f'\n\nErro Crítico -> {ee}')
            input()
            exit()

if __name__ == "__main__":
    print_banner()
    get_test()
