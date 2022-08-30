from behave import given, when, then
import time

@given(u'que acesse o site')
def acesso_site(context):
    context.swaglabs.login.acessar_site_login(context)

# @given(u'que esteja logado')
# def estar_logado(context):
#     context.swaglabs.login.acessar_site_login(context)
#     context.swaglabs.login.fazer_login_com_parametros(context, "tarcisio@cy.com", "1")