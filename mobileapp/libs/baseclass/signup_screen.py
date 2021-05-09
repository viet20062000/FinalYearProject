from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivy.properties import BooleanProperty
from kivymd.toast import toast
import sqlite3
import hashlib
from kivymd.uix.picker import MDDatePicker
class CinebotSignUpScreen(MDScreen):
	def sign_up(self):
		password=bytes(self.ids.password.text,encoding='utf-8')
		password_encrypted=hashlib.sha256(password).hexdigest()
		if self.ids.username.text and self.ids.password.text and self.ids.email.text and self.ids.dob.text:
			if "@" not in self.ids.email.text:
				toast("Invalid email, please check again!")
			elif self.ids.retypepassword.text!=self.ids.password.text:
				toast("Incorrect password re-typing, please check again!")
			else: 
				new_account=["User",self.ids.username.text,password_encrypted,self.ids.email.text,self.ids.dob.text]
				self.ids.username.text=""
				self.ids.password.text=""
				self.ids.retypepassword.text=""
				self.ids.email.text=""
				self.ids.dob.text=""
				conn=sqlite3.connect(r"libs\cinema.db")
				sql = ''' INSERT INTO Account(role_name,username,password,email,dob) VALUES(?,?,?,?,?) '''
				cur = conn.cursor()
				cur.execute(sql, new_account)
				conn.commit()
				self.parent.current="cinebot login screen"
				toast("Successfully sign up, you can now log in with your account")
	def show_date_picker(self):
		picker=MDDatePicker()
		picker.bind(on_save=self.set_date)
		picker.open()
	def set_date(self, instance, value, date_range):
		self.ids.dob.text=str(value)