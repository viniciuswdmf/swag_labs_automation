from behave import given, when, then
import time

@given(u'que acesse o site')
def acesso_site(context):
    context.swaglabs.login.acessar_site_login(context)

@given(u'que esteja logado')
def estar_logado(context):
    context.swaglabs.login.acessar_site_login(context)
    context.swaglabs.login.efetuar_login_valido(context, "standard_user", "secret_sauce")    
