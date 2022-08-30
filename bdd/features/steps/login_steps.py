from behave import given, when, then
import time

@when(u'realizar login com usuario e senha válidos')
def realizar_login_valido(context):
    context.swaglabs.login.acessar_site_login(context)
    context.swaglabs.login.efetuar_login_valido(context, "standard_user", "secret_sauce")    


@then(u'deve validar que o login foi realizado com sucesso')
def verificar_login(context):
    context.swaglabs.login.validar_login_correto(context)

