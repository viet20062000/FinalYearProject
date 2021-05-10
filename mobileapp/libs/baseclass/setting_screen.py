from kivy.properties import BooleanProperty

from kivymd.uix.list import OneLineListItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton,MDRaisedButton
class CinebotSettingScreen(MDScreen):
    dialog=None
    created = BooleanProperty(False)
    def show_logout_alert(self):
        self.dialog = MDDialog(
            title='LOG OUT',
            text="Are you sure?",
            buttons=[
                MDRaisedButton(
                    text="CANCEL", font_style="H6",on_release=self.dialog_close
                ),
                MDFlatButton(
                    text="YES", font_style="H6",on_release=self.logout
                ),
            ],
        )
        self.dialog.open()
    def dialog_close(self, *args):
        self.dialog.dismiss(force=True)
    def on_pre_enter(self):
        if not self.created:
            items = [
                "Sign Out",
                "About Us - Cinebot team",
                "Change background"
            ]
            for i in items:
                list_obj = OneLineListItem(
                    text=i, divider="Inset", font_style="H6"
                )
                list_obj.bind(on_release=lambda wdt:self.show_logout_alert())
                self.ids._list.add_widget(list_obj)
            self.created = True
    def logout(self, *args):
        self.dialog_close()
        self.parent.parent.parent.parent.current = "cinebot login screen"
        self.parent.parent.parent.ids.nav_bar.set_current(-1)
    def multi_function(self, text):
        if text=="Sign Out":
            self.show_logout_alert()
            # self.parent.parent.parent.parent.current = "cinebot login screen"
            # self.parent.parent.parent.ids.nav_bar.set_current(-1)
        if text=="Change background":
            print("hello")
            self.parent.parent.parent.parent.parent.parent.md_bg_color='gch("#ffffff")'
        