import os
#Alunos:Marcel Gustavo e Marcelo Augusto.
class Stack:
    def __init__(self):
        # Método construtor que inicializa a pilha com uma lista vazia
        self.items = []

    def push(self, item):
        # Método para adicionar um item ao topo da pilha
        self.items.append(item)
        print("Adicionado:", item)

    def pop(self):
        # Método para remover e retornar o item do topo da pilha
        if self.is_empty():
            print("A pilha está vazia. Adicione um novo valor.")
        else:
            item = self.items.pop()
            print("Removido:", item)

    def is_empty(self):
        # Método para verificar se a pilha está vazia
        return len(self.items) == 0

    def show_stack(self):
        # Método para exibir todos os itens da pilha
        if self.is_empty():
            print("A pilha está vazia.")
        else:
            print("Pilha completa:", self.items)


def clear_screen():
    # Função para limpar a tela do console
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    stack = Stack()

    while True:
        print("\n--- Selecione a Opção Desejada ---")
        print("1. Adicionar")
        print("2. Remover")
        print("3. Imprimir pilha")
        print("4. Limpar tela")
        print("5. Sair")

        escolha = int(input("Digite a Opção=> "))

        if escolha == 1:
            valores_add = input("Digite o valor ou valores separados por vírgula a adicionar: ").split(",")
            for valor in valores_add:
                stack.push(int(valor.strip()))

        elif escolha == 2:
            stack.pop()

        elif escolha == 3:
            stack.show_stack()

        elif escolha == 4:
            clear_screen()

        elif escolha == 5:
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Por favor, escolha novamente.")


if __name__ == "__main__":
    main()
