
from features.page_objects.Swaglabs.swaglabs_page_index import *


class PageHelper():

    def __init__(self, context):
        pass

    def acessar(self, context, url_complemento):
        context.ambiente = context.config.userdata["ambiente"]
        context.url_dev = "https://saucedemo.com"
        context.url_stage = "https://saucedemo.com"
        context.url_prod = "https://saucedemo.com"

        if context.ambiente == "dev":
            context.page.goto(context.url_dev+url_complemento)

        elif context.ambiente == "stage":
            context.page.goto(context.url_stage+url_complemento)

        elif context.ambiente == "prod":
            context.page.goto(context.url_prod+url_complemento)
            
        else:
            print("Digite o ambiente!")