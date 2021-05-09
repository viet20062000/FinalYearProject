import sqlite3
import os
import sys
from pathlib import Path
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.toast import toast
from kivy.core.window import Window

if getattr(sys, "frozen", False): 
    os.environ["CINEBOT"] = sys._MEIPASS
else:
    os.environ["CINEBOT"] = str(Path(__file__).parent)
CINEBOT_FILES = f"{os.environ['CINEBOT']}/libs/kv/"

for item in os.listdir(CINEBOT_FILES):
    with open(os.path.join(CINEBOT_FILES, item), encoding="utf-8") as layout:
        Builder.load_string(layout.read())

KV = """
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import CinebotLoginScreen libs.baseclass.login_screen.CinebotLoginScreen
#:import CinebotRootScreen libs.baseclass.root_screen.CinebotRootScreen
#:import CinebotLoginScreen libs.baseclass.signup_screen.CinebotSignUpScreen

ScreenManager:
    transition: FadeTransition()

    CinebotLoginScreen:
        name: "cinebot login screen"

    CinebotRootScreen:
        name: "cinebot root screen"

    CinebotSignUpScreen:
        name:"cinebot signup screen"

"""

class MDCinebot(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Cinebot"
        self.icon = f"{os.environ['CINEBOT']}/images/Cinebot-logos_black.png"
    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.theme_style = "Dark"
        FONT_PATH = f"{os.environ['CINEBOT']}/assets/fonts/"

        self.theme_cls.font_styles.update(
            {
                "H1": [FONT_PATH + "RobotoCondensed-Light", 96, False, -1.5],
                "H2": [FONT_PATH + "RobotoCondensed-Light", 60, False, -0.5],
                "H3": [FONT_PATH + "Eczar-Regular", 48, False, 0],
                "H4": [FONT_PATH + "RobotoCondensed-Regular", 34, False, 0.25],
                "H5": [FONT_PATH + "RobotoCondensed-Regular", 24, False, 0],
                "H6": [FONT_PATH + "RobotoCondensed-Bold", 20, False, 0.15],
                "Subtitle1": [
                    FONT_PATH + "RobotoCondensed-Regular",
                    16,
                    False,
                    0.15,
                ],
                "Subtitle2": [
                    FONT_PATH + "RobotoCondensed-Medium",
                    14,
                    False,
                    0.1,
                ],
                "Body1": [FONT_PATH + "Eczar-Regular", 16, False, 0.5],
                "Body2": [FONT_PATH + "RobotoCondensed-Light", 14, False, 0.25],
                "Button": [FONT_PATH + "RobotoCondensed-Bold", 14, True, 1.25],
                "Caption": [
                    FONT_PATH + "RobotoCondensed-Regular",
                    12,
                    False,
                    0.4,
                ],
                "Overline": [
                    FONT_PATH + "RobotoCondensed-Regular",
                    10,
                    True,
                    1.5,
                ]
            }
        )
        return Builder.load_string(KV)
    
    def change_screen(self, screen, *args):
        self.scr_mngr.current = screen

if __name__ == '__main__':
    #Window.size=(370,600)
    MDCinebot().run()
