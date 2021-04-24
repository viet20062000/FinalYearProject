from DBconnect import *
import json
import requests
path="https://image.tmdb.org/t/p/w500"
def insert_genre(conn):
	with open('genredata.json') as json_file:
		data=json.load(json_file)
		for item in data["genres"]:
			if item["name"].startswith("Phim"):
				name=item["name"][5:]
			else:
				name=item["name"]
			genre=(item["id"],name)
			sql = f' INSERT INTO Genre(genre_id,genre_name) VALUES(?,?)' 
			cur = conn.cursor()
			cur.execute(sql,genre)
			conn.commit()
			print("added 1 genre!")
def insert_film(conn):
	with open('filmdata.json') as json_file:
		data=json.load(json_file)
		for item in data["results"]:
			url3=f'https://api.themoviedb.org/3/movie/{item["id"]}?api_key=2cee99ff957a908fc907d6849d5d9009&language=vi&append_to_response=credits'
			r3=requests.get(url3)
			data=json.loads(r3.content)
			for genre in data["genres"]:
				film_genre=(item["id"],genre["id"])
				sql=f'INSERT INTO film_genre(film_id,genre_id) VALUES(?,?)'
				cur=conn.cursor()
				cur.execute(sql,film_genre)
				conn.commit()
				print("added 1 to film_genre!")
			image=''.join([path,data["poster_path"]])
			director=""
			for crew_item in data["credits"]["crew"]:
				if crew_item["job"] == "Director":
					director=crew_item["name"]
			film=(data["id"],image,data["adult"],data["title"],data["overview"],data["popularity"],data["release_date"],data["vote_average"],director)
			sql = f' INSERT INTO Film(film_id,image,adult,title,overview,popularity,release_date,rating,director) VALUES(?,?,?,?,?,?,?,?,?)' 
			cur = conn.cursor()
			cur.execute(sql,film)
			print("added 1 to film")
			conn.commit()
def insert_actor(conn):
	sql = """SELECT film_id from Film"""
	cursor=conn.cursor()
	cursor.execute(sql)
	records = cursor.fetchall()
	for row in records:
		url3=f'https://api.themoviedb.org/3/movie/{row[0]}?api_key=2cee99ff957a908fc907d6849d5d9009&append_to_response=credits'
		r3=requests.get(url3)
		data=json.loads(r3.content)
		for item in data["credits"]["cast"]:
			actor_film=(item["id"],data["id"],item["character"])
			sql=f'INSERT INTO actor_film(actor_id,film_id,actor_role) VALUES(?,?,?)'
			cur=conn.cursor()
			cur.execute(sql,actor_film)
			conn.commit()
			print("added 1 to actor_film!")
		for thing in data["credits"]["cast"]:
			existed=[]
			url4=f'https://api.themoviedb.org/3/person/{thing["id"]}?api_key=2cee99ff957a908fc907d6849d5d9009'
			r4=requests.get(url4)
			data_actor=json.loads(r4.content)
			profile_path=""
			if data_actor["profile_path"]:
				profile_path=data_actor["profile_path"]
			image=''.join([path,profile_path])
			actor_realname=""
			if not data_actor["also_known_as"]:
				pass
			else:
				actor_realname=data_actor["also_known_as"][0]
			actor=(data_actor["id"],data_actor["name"],image,data_actor["biography"],data_actor["homepage"],data_actor["birthday"],actor_realname)
			sql = """SELECT actor_id from Actor"""
			cursor=conn.cursor()
			cursor.execute(sql)
			records = cursor.fetchall()
			for row in records:
				existed.append(row[0])
			if data_actor["id"] not in existed:
				sql1 = f' INSERT INTO Actor(actor_id,actor_name,actor_image,actor_biography,actor_page,actor_dob,actor_realname) VALUES(?,?,?,?,?,?,?)' 
				cur = conn.cursor()
				cur.execute(sql1,actor)
				conn.commit()
				print("added 1 to actor!")
if __name__ == '__main__':
	database=r"C:\sqlite\db\cinema.db"
	conn=create_connection(database)
	insert_actor(conn)
