from features.helper.page_helper import *
from features.page_objects.Swaglabs.pages.components.el_home import *
from features.page_objects.Swaglabs.pages.components.el_login import *
from playwright.sync_api import expect
import time

class SwaglabsHome():
    
    def __init__(self, context):
        pass

    def adicionar_produto_carrinho(self, context):
        context.page.click(body_elements['BTN_ADDTOCART_PRODUCT1']) 
    
    def validar_adicao_produto(self, context):
        locator = context.page.locator(body_elements['CART_COUNT_ICON'])
        expect(locator).to_have_text("1")

    def remover_produto_carrinho(self, context):
        context.page.click(body_elements['BTN_REMOVECART_PRODUCT1'])

    def validar_remocao_produto(self, context):
        locator = context.page.locator(body_elements['CART_COUNT_ICON'])
        expect(locator).not_to_be_visible