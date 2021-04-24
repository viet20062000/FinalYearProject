from kivy.properties import ColorProperty, StringProperty,ObjectProperty

from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.event import EventDispatcher
from kivy.uix.screenmanager import ScreenManager
class CinebotRootScreen(MDScreen):
    pass


class CinebotListItem(ThemableBehavior, RectangularRippleBehavior, MDBoxLayout):
    text = StringProperty()
    secondary_text = StringProperty()
    tertiary_text = StringProperty()
    bar_color = ColorProperty((1, 0, 0, 1))

class FilmInfor(EventDispatcher):
	film_id=StringProperty()
class CinebotManager(ScreenManager):
	film_object=ObjectProperty(FilmInfor())

class CinebotSeeAllButton(RectangularRippleBehavior, MDBoxLayout):
    pass
