from kivymd.uix.screen import MDScreen
from kivy.properties import ListProperty, StringProperty
from kivy.uix.widget import Widget
from datetime import date
import sqlite3

from kivymd.uix.list import TwoLineAvatarListItem
class CinebotBookingTicketScreen(MDScreen):
	def on_enter(self):
		today=date.today()
		conn=sqlite3.connect(r"\libs\cinema.db")
		cursor=conn.cursor()
		sql=f"SELECT film_id, image, title, overview from film where release_date < '{today}'order by release_date desc limit 5"
		cursor.execute(sql)
		records=cursor.fetchall()
		for row in records:
			self.ids.container.add_widget(CinebotTwoLineLeftAvatarItem(image=row[1], text=row[2],film_id=str(row[0])))
class CinebotTwoLineLeftAvatarItem(TwoLineAvatarListItem):
    image = StringProperty()
    title = StringProperty()
    overview= StringProperty()
    film_id=StringProperty()
    secondary_font_style = "Caption"