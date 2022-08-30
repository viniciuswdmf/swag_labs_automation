from features.helper.page_helper import *
from features.page_objects.Swaglabs.pages.components.el_home import *
from features.page_objects.Swaglabs.pages.components.el_login import *
from playwright.sync_api import expect
import time

class SwaglabsLogin():
    
    def __init__(self, context):
        pass

    def acessar_site_login(self, context):
        context.page_helper.acessar(context, "")

    def acessar_cadastro(self, context):
        context.page.click(login_elements['LINK_CADASTRO'])

    def efetuar_login_valido(self, context, email, senha):
        context.page.fill(login_elements['INP_USER'], email)
        context.page.fill(login_elements['INP_PASS'], senha)
        context.page.click(login_elements['BTN_LOGIN'])

    def validar_login_correto(self, context):
        locator = context.page.locator(body_elements['CART_ICON'])
        expect(locator).to_be_visible()

