#language: pt

@login
Funcionalidade: Login no site de teste
    Como um usuário do site de teste
    Quero realizar login 
    Para realizar tarefas no site

Contexto: Acessar o site no ambiente selecionado
    Dado que acesse o site

Cenário: Fazer login com sucesso
    Quando realizar login com usuario e senha válidos
    Então deve validar que o login foi realizado com sucesso

# Esquema do Cenário: Erro ao fazer login
#     Quando realizar login com "<tipo_erro>" 
#     Então deve ser exibida a mensagem de erro "<mensagem>"
#     Exemplos:
#         | tipo_erro                | mensagem                          | 
#         | Email nao preenchido     | Email não pode ficar em branco    |
#         | Senha nao preenchida     | Password não pode ficar em branco |
#         | Email incorreto          | Email e/ou senha inválidos        |
#         | Senha incorreta          | Email e/ou senha inválidos        |