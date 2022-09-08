from behave import given, when, then
import time

@when(u'adicionar um produto ao carrinho')
def add_produto(context):
    context.swaglabs.home.adicionar_produto_carrinho(context)


@then(u'o icone do carrinho deve ser atualizado')
def validar_produto_adicionado(context):
    context.swaglabs.home.validar_adicao_produto(context)

@given(u'que o produto tenha sido adicionado ao carrinho')
def adicionar_produto(context):
    context.swaglabs.home.adicionar_produto_carrinho(context)


@when(u'remover um produto do carrinho')
def remover_produto(context):
    context.swaglabs.home.remover_produto_carrinho(context)


@then(u'o icone do carrinho deve ser zerado')
def validar_produto_removido(context):
    context.swaglabs.home.validar_remocao_produto(context)