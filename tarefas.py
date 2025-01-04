def adicionar_tarefa(tarefa):
    with open("tarefas.txt", "a") as arquivo:
        arquivo.write(tarefa + "\n")
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def listar_tarefas():
    try:
        with open("tarefas.txt", "r") as arquivo:
            tarefas = arquivo.readlines()
            if not tarefas:
                print("Nenhuma tarefa encontrada.")
            else:
                print("\nTarefas:")
                for i, tarefa in enumerate(tarefas, start=1):
                    print(f"{i}. {tarefa.strip()}")
    except FileNotFoundError:
        print("Nenhuma tarefa encontrada.")

def remover_tarefa(numero):
    try:
        with open("tarefas.txt", "r") as arquivo:
            tarefas = arquivo.readlines()
        
        if numero < 1 or numero > len(tarefas):
            print("Número inválido!")
            return

        tarefa_removida = tarefas.pop(numero - 1)
        with open("tarefas.txt", "w") as arquivo:
            arquivo.writelines(tarefas)
        
        print(f"Tarefa '{tarefa_removida.strip()}' removida com sucesso!")
    except FileNotFoundError:
        print("Nenhuma tarefa para remover.")

def editar_tarefa(numero, nova_tarefa):
    try:
        with open("tarefas.txt", "r") as arquivo:
            tarefas = arquivo.readlines()
        
        if numero < 1 or numero > len(tarefas):
            print("Número inválido!")
            return

        tarefa_antiga = tarefas[numero - 1]
        tarefas[numero - 1] = nova_tarefa + "\n"
        
        with open("tarefas.txt", "w") as arquivo:
            arquivo.writelines(tarefas)
        
        print(f"Tarefa '{tarefa_antiga.strip()}' foi alterada para '{nova_tarefa}'.")
    except FileNotFoundError:
        print("Nenhuma tarefa para editar.")
