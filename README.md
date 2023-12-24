O objetivo deste projeto é criar um gerenciador de tarefas simples utilizando Python e o banco de dados SQLite. O programa permite ao usuário cadastrar tarefas, visualizar as tarefas cadastradas, excluir tarefas e sair do programa.

Estrutura do Código:
Conexão com o Banco de Dados:
O código inicia estabelecendo uma conexão com o banco de dados SQLite, verificando se a tabela "infos" já existe. Caso não exista, a tabela é criada para armazenar informações sobre as tarefas.

Funções Definidas:
lin(): Imprime uma linha decorativa para melhorar a visualização no console.
menu(): Exibe o menu principal com opções para criar tarefas, visualizar tarefas, excluir tarefas e sair do programa.
Loop Principal:
O programa entra em um loop infinito, exibindo o menu e aguardando a entrada do usuário. Dependendo da escolha do usuário, diferentes ações são executadas.

Opção 1 - Criar Tarefa:
O usuário pode cadastrar uma nova tarefa, fornecendo informações como nome, descrição, dia e hora. Os dados são então inseridos na tabela do banco de dados.

Opção 2 - Visualizar Tarefas:
O programa recupera todas as tarefas cadastradas na tabela "infos" e exibe as informações no console. Caso não haja tarefas cadastradas, uma mensagem informa ao usuário.

Opção 3 - Excluir Tarefa:
O usuário pode escolher uma tarefa para excluir fornecendo o ID da tarefa. O programa verifica se o ID é válido e, em seguida, remove a tarefa correspondente do banco de dados.

Opção 4 - Sair do Programa:
Encerra o loop principal, encerrando o programa.

Conclusão:
O projeto fornece uma base funcional para um gerenciador de tarefas simples, utilizando um banco de dados SQLite para armazenar informações.
