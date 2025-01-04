##### My first utility #####
#
# Hello World!

from ovito.gui import UtilityInterface
from traits.api import *

class MyFirstUtility(UtilityInterface):

    param = Int(0, ovito_group="Parameters")
    param2 = String("Hello World!", ovito_group="Parameters")
    button_trait = Button(ovito_label="Click me")

    @observe("button_trait")
    def run_command(self, event):
        print("hello world")
        raise RuntimeError("This is a test error message")
