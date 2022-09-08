#language: pt

@produto
Funcionalidade: Manipular produtos no site de teste
    Como um usuário do site de teste
    Quero poder adicionar ou remover produtos do carrinho

Contexto: Acessar o site no ambiente selecionado e realizar login
    Dado que acesse o site
    E que esteja logado

Cenário: Adicionar ao carrinho
    Quando adicionar um produto ao carrinho
    Então o icone do carrinho deve ser atualizado

Cenário: Remover do carrinho
    Dado que o produto tenha sido adicionado ao carrinho
    Quando remover um produto do carrinho
    Então o icone do carrinho deve ser zerado
