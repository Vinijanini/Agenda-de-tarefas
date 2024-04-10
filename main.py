
import time
import sqlite3 #biblioteca do banco de dados
banco = sqlite3.connect('banco_de_dados.db') #cria banco de dados#
cursor = banco.cursor() #conecta o cursor

cursor.execute("CREATE TABLE IF NOT EXISTS infos (nome text, desc text, dia int, hora text)")

#funções
def lin():
    print('-=' * 10)
def menu():
    lin()
    print('[1] Criar tarefa')
    print('[2] Visualizar tarefas')
    print('[3] Excluir tarefa')
    print('[4] Sair do programa')
    lin()


while True:
    menu()

    while True:
        try:
            esc = int(input('>>>>>>>>>>>>>>>'))
            while esc not in range(1, 5):
                print('Opção inválida!')
                esc = str(input('>>>>>>>>>>>>>>>'))
            break
        except ValueError:
            print('Opção inválida!')

    #Cadastrar uma tarefa
    if esc == 1:
        nome = str(input('Nome da tarefa:'))
        desc = str(input('Descrição:'))
        while True:
            try:
                dia = int(input('Dia:'))
                while dia not in range(1, 32):
                    print('Dia inválido!')
                    dia = int(input('Dia:'))
                break
            except:
                print('Dia inválido!')
        hora = str(input('Hora:'))
        lin()
        cursor.execute("INSERT INTO infos VALUES ('" + nome + "','" + desc + "','" + str(dia) + "','" + hora + "')")
        banco.commit()
        print('Tarefa cadastrada com sucesso!')

    #Acessar tarefas
    elif esc == 2:
        cursor.execute("SELECT * FROM infos")
        tarefas = (cursor.fetchall())
        if len(tarefas) == 0:
            print('Ainda não há tarefas cadastradas')
        for cont2, tarefa in enumerate(tarefas):
            time.sleep(0.8)
            lin()
            print(f"{cont2+1}º Tarefa")
            for cont, c in enumerate(tarefa):
                if cont == 0:
                    print(f'Nome: {c}')
                if cont == 1:
                    print(f'Descrição: {c}')
                if cont == 2:
                    print(f'Dia: {c}')
                if cont == 3:
                    print(f'Hora: {c}')
            lin()

    ##Apagar tarefa##
    elif esc == 3:
        cursor.execute("SELECT * FROM infos")
        tarefas = (cursor.fetchall())
        if len(tarefas) == 0:
            print('Ainda não há tarefas cadastradas')
        else:
            apagar = int(input(f'Id da tarefa para apagar 1/{len(tarefas)}:'))
            while len(tarefas) < apagar:
                print('Id não existe!')
                apagar = int(input(f'Id da tarefa para apagar 1/{len(tarefas)}:'))
        for cont3, tarefa2 in enumerate(tarefas):
            if cont3+1 == apagar:
                for cont, c2 in enumerate(tarefa2):
                    cursor.execute("DELETE from infos WHERE nome = '" + c2 + "'")
                    banco.commit()
                    lin()
                    print('Tarefa apagada com sucesso!')
                    break
    ##Sair do programa##
    elif esc == 4:
        print('Programa finalizado!')
        quit()
