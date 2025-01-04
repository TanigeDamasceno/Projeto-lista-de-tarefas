from tarefas import adicionar_tarefa, listar_tarefas, remover_tarefa, editar_tarefa

def menu():
    while True:
        print("\n=== Gerenciador de Tarefas ===")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Remover tarefa")
        print("4. Editar tarefa")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            tarefa = input("Digite a tarefa: ")
            adicionar_tarefa(tarefa)
        elif escolha == "2":
            listar_tarefas()
        elif escolha == "3":
            tarefa = input("Digite o número da tarefa para remover: ")
            remover_tarefa(int(tarefa))
        elif escolha == "4":
            tarefa = input("Digite o número da tarefa para editar: ")
            nova_tarefa = input("Digite o novo nome da tarefa: ")
            editar_tarefa(int(tarefa), nova_tarefa)
        elif escolha == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()