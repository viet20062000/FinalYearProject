from DBconnect import *
from Insert import *
import requests
import json

# file=open("unicode.txt",encoding="utf8")
# unicode_table=file.read().split("\n")
# chars=[]
# codes=[]
# for code in unicode_table:
# 	x=code.split(" ")
# 	chars.append(x[0])
# 	codes.append(x[1])
# print(chars)
# print(codes)
# with open("filmdata.json","r") as json_data:
# 	content=json_data.read()
# 	for j in range(len(chars)):
# 		content = content.replace(codes[j],chars[j])
# 		with open("filmdata1.json","w") as json_data1:
# 			json.dump(content,json_data1)

# for i in r:
# 	for j in range(len(chars)):
# 		r[i]=r[i].replace(codes[j],chars[j])
# with open('filmdata.json','w') as json_data:
#     json.dump(data,json_data)

# with open('filmdata.json') as json_file:
#     film = json.load(json_file)
# for item in film["results"]:
# 	print(item["overview"])



# #Get genre details
# url = 'https://api.themoviedb.org/3/genre/movie/list?api_key=2cee99ff957a908fc907d6849d5d9009&language=vi'
# r = requests.get(url)
# data=json.loads(r.content)

# with open('genredata.json','w') as json_data:
#     json.dump(data,json_data)

# with open('genredata.json') as json_file:
#     film = json.load(json_file)
# for item in film["genres"]:
# 	print(item)

# Get list details
def get_list():
	url2 = 'https://api.themoviedb.org/4/list/7086790?page=2&api_key=2cee99ff957a908fc907d6849d5d9009&language=vi'
	r2=requests.get(url2)
	data=json.loads(r2.content)
	with open('filmdata.json','w',encoding="utf8") as json_data:
		json.dump(data,json_data)
	with open('filmdata.json') as json_file:
	    film = json.load(json_file)
	for item in film["results"]:
		print(item["overview"])

#Get credit details
def get_credit(conn,film_id):
	url3=f'https://api.themoviedb.org/3/movie/{film_id}?api_key=2cee99ff957a908fc907d6849d5d9009&language=vi&append_to_response=credits'
	r3=requests.get(url3)
	data=json.loads(r3.content)
	print(data)
	# with open('creditdata.json','w',encoding="utf8") as json_data:
	# 	json.dump(data,json_data)

# #Get actor details
# url4=f'https://api.themoviedb.org/3/person/{actor_id}?api_key=2cee99ff957a908fc907d6849d5d9009&language=vi'
# r4=requests.get(url4)
# data=json.loads(r4.content)
# print(data)

if __name__ == '__main__':
	database=r"C:\sqlite\db\cinema.db"
	conn=create_connection(database)
	# sql = """SELECT film_id from Film"""
	# cursor=conn.cursor()
	# cursor.execute(sql)
	# records = cursor.fetchall()
	# for row in records:
	# 	print(row[0])
	# get_credit(conn,787459)
	get_list()
