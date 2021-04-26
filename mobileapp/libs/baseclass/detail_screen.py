from kivymd.uix.screen import MDScreen
import sqlite3

class CinebotDetailScreen(MDScreen):
	def on_enter(self, *largs):
		genres=[]
		casts=[]
		print(self.parent.film_object.film_id)
		ids=int(self.parent.film_object.film_id)
		conn=sqlite3.connect(r"libs\cinema.db")
		print("success!")
		sql=f"SELECT * from Film where film_id={ids}"
		cursor=conn.cursor()
		cursor.execute(sql)
		record = cursor.fetchone()
		self.ids.image.source=record[1]
		self.ids.film_title.text=record[3]
		self.ids.date.text=record[6]
		self.ids.director.text=record[8]
		if str(record[7])!="0.0":
			self.ids.rating.text=str(record[7])
		self.ids.overview.text=record[4]
		sql_genre_list=f"SELECT * from film_genre where film_id={ids}"
		cursor.execute(sql_genre_list)
		record_genre_list = cursor.fetchall()
		for row in record_genre_list:
			sql_genre=f"SELECT * from genre where genre_id={row[1]}"
			cursor.execute(sql_genre)
			record_genre=cursor.fetchone()
			genres.append(record_genre[1])
		for item in range(len(genres)):
			if item==0:
				data_genre=genres[item]
			else:
				data_genre+=f", {genres[item]}"
		self.ids.genre.text=data_genre
		sql_cast_list=f"SELECT * from actor_film where film_id={ids} limit 5"
		cursor.execute(sql_cast_list)
		record_cast_list=cursor.fetchall()
		for row in record_cast_list:
			sql_actor=f"SELECT * from actor where actor_id={row[0]}"
			cursor.execute(sql_actor)
			record_actor=cursor.fetchone()
			casts.append(record_actor[1])
		for item in range(len(casts)):
			if item==0:
				data_cast=casts[item]
			else:
				data_cast+=f", {casts[item]}"
		self.ids.cast.text=data_cast