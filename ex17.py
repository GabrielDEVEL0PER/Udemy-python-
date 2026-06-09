Tarefas = []
Desfazer = []

while True:
    comando=input("Comandos: listar, desfazer, refazer \nDigite uma tarefa ou comando:")

    if comando == "listar":
        if Tarefas:
            print("\nTarefas:")
            for tarefa in Tarefas:
                print(f"- {tarefa}")
        else:
            print("Nenhuma tarefa na lista!")

    elif comando == "desfazer":
        if Tarefas:
            removida = Tarefas.pop()
            Desfazer.append(removida)
            print(f"Tarefa '{removida}' desfeita!")
        else:
            print("Nada para desfazer!")
    elif comando == "refazer":
        if Desfazer:
            recuperada = Desfazer.pop()
            Tarefas.append(recuperada)
            print(f"Tarefa '{recuperada}' refeita!")
        else:
            print("Nada para refazer!")
    else:
        Tarefas.append(comando)
        print(f"Tarefa '{comando}' adicionada! ")
        
