
import sqlite3
from kivy.core.window import Window

from kivy.clock import Clock

import os
from kivy.uix.button import ButtonBehavior
from kivy.properties import StringProperty
from kivymd.uix.screen import MDScreen
from kivymd.uix.swiper import MDSwiperItem

class CinebotSwiperItem(ButtonBehavior,MDSwiperItem):
	source = StringProperty()
	name=StringProperty()
	film_id=StringProperty()
	def detail(self):
		self.parent.parent.parent.parent.parent.film_object.film_id=self.parent.parent.parent.get_current_item().film_id
		self.parent.parent.parent.parent.parent.current="DETAIL"


class CinebotOverviewScreen(MDScreen):

	def swiper_display(self,dt):
		if len(self.ids.Swiper.get_items()) ==0 :
			images=[]
			names=[]
			film_id=[]
			conn=sqlite3.connect(r"libs\cinema.db", check_same_thread=False)
			print("success!")
			sql="""SELECT image,title,film_id from Film"""
			cursor=conn.cursor()
			cursor.execute(sql)
			records = cursor.fetchall()
			for row in records:
				images.append(row[0])
				names.append(row[1])
				film_id.append(str(row[2]))
			for item in range(len(images)):
				self.ids.Swiper.add_widget(
					CinebotSwiperItem(
						source=images[item],name=names[item],film_id=film_id[item]
					)
				)
		else:
			return 0
	def on_enter(self):
		Clock.schedule_once(self.swiper_display, 1)

