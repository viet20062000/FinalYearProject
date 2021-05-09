from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivy.properties import BooleanProperty
from kivymd.toast import toast
import sqlite3
import hashlib
class CinebotLoginScreen(MDScreen):
	def check_login(self):
		username=self.ids.username.text
		password=bytes(self.ids.password.text,encoding='utf-8')
		password_encrypted=hashlib.sha256(password).hexdigest()
		conn=sqlite3.connect(r"libs\cinema.db", check_same_thread=False)
		cursor=conn.cursor()
		sql="SELECT role_name,username,password from Account"
		cursor.execute(sql)
		records=cursor.fetchall()
		username_list=[]
		password_list=[]
		for row in records:
			username_list.append(row[1])
			password_list.append(row[2])
		if username not in username_list:
			toast("Wrong username or password, please check again!")
		else:
			if password_encrypted==password_list[username_list.index(username)]:
				self.ids.username.text=""
				self.ids.password.text=""
				self.parent.current="cinebot root screen"

	def goto_signup(self):
		self.parent.current="cinebot signup screen"
class CinebotMDTextField(MDTextField):
    show_password = BooleanProperty(True)

