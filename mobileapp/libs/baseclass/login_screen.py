from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivy.properties import BooleanProperty
class CinebotLoginScreen(MDScreen):
    pass


class CinebotMDTextField(MDTextField):
    show_password = BooleanProperty(True)

