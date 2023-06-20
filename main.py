def create():
    print("Operação de criação")

def read():
    print("Operação de leitura")

def update():
    print("Operação de atualização")

def delete():
    print("Operaçao de Exclusão")

def main():
    while True:
        print("Seleclionar uma operação:")
        print("1. Criar")
        print("2. Ler")
        print("3. Atualizar")
        print("4. Excluir")
        print("0. Sair")

        choice = input("Digite o numero de operação desejada: ")
        if choice == '1':
            create()
        elif choice == '2':
            read()
        elif choice == '3':
            update()
        elif choice == '4':
            delete()
        elif choice == '0':
            break
        else:
            print("Operação invalida. Tente novamente.")

if __name__== "__main__":
    main()
