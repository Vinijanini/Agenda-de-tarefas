import time
import sqlite3 #biblioteca do banco de dados
banco = sqlite3.connect('banco_de_dados.db') #cria banco de dados#
cursor = banco.cursor() #conecta o cursor

#verifica se existe uma tabela, se não, uma é criada
ver = cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='infos';").fetchone()
if ver[0] == 0:
    cursor.execute("CREATE TABLE infos (nome text, desc text, dia int, hora text)")

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

    esc = str(input('>>>>>>>>>>>>>>>'))

    #mensagem de erro#
    while esc not in '1234':
        print('Opção inválida!')
        esc = str(input('>>>>>>>>>>>>>>>'))

    #Cadastrar uma tarefa
    if esc == "1":
        nome = str(input('Nome da tarefa:'))
        desc = str(input('Descrição:'))
        dia = str(input('Dia:'))
        hora = str(input('Hora:'))
        lin()
        cursor.execute("INSERT INTO infos VALUES ('" + nome + "','" + desc + "','" + dia + "','" + hora + "')")
        banco.commit()
        print('Tarefa cadastrada com sucesso!')

    #Acessar tarefas
    elif esc == "2":
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
    elif esc == "3":
        cursor.execute("SELECT * FROM infos")
        tarefas = (cursor.fetchall())
        if len(tarefas) == 0:
            print('Ainda não há tarefas cadastradas')
        else:
            apagar = int(input('Id da tarefa para apagar:'))
            while len(tarefas) < apagar:
                print('Id não existe!')
                apagar = int(input('Id da tarefa para apagar:'))
        for cont3, tarefa2 in enumerate(tarefas):
            if cont3+1 == apagar:
                for cont, c2 in enumerate(tarefa2):
                    cursor.execute("DELETE from infos WHERE nome = '" +c2+ "'")
                    banco.commit()
                    lin()
                    print('Tarefa apagada com sucesso!')
                    break
    ##Sair do programa##
    elif esc == "4":
        break
