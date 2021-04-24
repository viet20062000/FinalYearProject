from kivy.properties import BooleanProperty

from kivymd.uix.list import OneLineListItem
from kivymd.uix.screen import MDScreen


class CinebotSettingScreen(MDScreen):
    created = BooleanProperty(False)

    def on_pre_enter(self):
        if not self.created:
            items = [
                "Sign Out"
            ]
            for i in items:
                list_obj = OneLineListItem(
                    text=i, divider="Inset", font_style="H6"
                )
                list_obj.bind(on_release=self.logout)
                self.ids._list.add_widget(list_obj)
            self.created = True

    def logout(self, obj):
        self.parent.parent.parent.parent.current = "cinebot login screen"
        self.parent.parent.parent.ids.nav_bar.set_current(-1)
