from features.page_objects.Swaglabs.pages.login import *
from features.page_objects.Swaglabs.pages.commons import *
from features.page_objects.Swaglabs.pages.home import *

class SwaglabsIndex():

    def __init__(self, context):
        self.commons = SwaglabsCommons(context)
        self.login = SwaglabsLogin(context)
