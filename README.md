Sistema de Notas de Alunos (Python)

Projeto de terminal desenvolvido em Python para simular o gerenciamento simples de alunos e notas.
Permite cadastrar alunos, registrar notas, consultar notas registradas e calcular médias.

Funcionalidades:
Cadastro de alunos
Adição de notas por aluno
Listagem de alunos e suas notas
Cálculo de média individual por aluno
Listagem de alunos aprovados com base na média
Estrutura de dados

Cada aluno é armazenado como um dicionário:

{
  "nome": "nome_do_aluno",
  "notas": [7.5, 8.0, 6.0]
}


Todos os alunos são mantidos em uma lista chamada lista.

Conceitos praticados:
Listas e dicionários
Lista dentro de dicionário
Funções
Condicionais e laços de repetição
Busca de dados em listas
Cálculo de média com sum() e len()
Formatação de números com casas decimais

Como executar:
Ter Python instalado
Executar no terminal:
python nome_do_arquivo.py

Próximas melhorias planejadas:
Validação de nota (intervalo permitido)
Evitar cadastro duplicado de alunos
Persistência em arquivo (JSON)
