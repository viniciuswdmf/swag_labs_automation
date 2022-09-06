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

Esquema do Cenário: Erro ao fazer login
    Quando realizar login com "<tipo_erro>" 
    Então deve ser exibida a mensagem de erro "<mensagem>"
    Exemplos:
        | tipo_erro                    | mensagem                                                                      | 
        | Username nao preenchido      | Epic sadface: Username is required                                            |
        | Senha nao preenchida         | Epic sadface: Password is required                                            |
        | Username ou senha incorretos | Epic sadface: Username and password do not match any user in this service     |