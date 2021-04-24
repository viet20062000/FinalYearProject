from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard, MDSeparator
from kivy.uix.button import ButtonBehavior
from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.image import AsyncImage
from kivymd.utils.fitimage import FitImage 
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import speech_recognition as sr 
from datetime import date
import os
from chatterbot.comparisons import LevenshteinDistance
import chatterbot.filters
import playsound
import time
import pyttsx3
import calendar 
import wikipedia
import random
from threading import Thread
import sqlite3
class CinebotFitImage(ButtonBehavior,FitImage):
	film_id=StringProperty()
class CinebotAssistantScreen(MDScreen):
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')       
	engine.setProperty('rate', 150)   
	engine.setProperty('voice', voices[2].id)

	cinebot = ChatBot('Cinebot',
			storage_adapter='chatterbot.storage.SQLStorageAdapter',
	    	logic_adapters=[
	    		{
	    			'import_path':'chatterbot.logic.BestMatch',
	    			'default_response':"I'm sorry but i can't understand, please try again.",
	    		},
	    		{
	    			'import_path':'chatterbot.logic.MathematicalEvaluation'
	    		}
	    	],
	    	statement_comparison_function=LevenshteinDistance,
	    	database_uri='sqlite:///cinebotDB.db',
	    	read_only=True,
	    	filters=[chatterbot.filters.get_recent_repeated_responses]

	)

	# # # Create a new trainer for the chatbot
	# trainer = ChatterBotCorpusTrainer(cinebot)
	# trainer.train("chatterbot.corpus.english.cinema")
	# # trainer.train("chatterbot.corpus.english.greetings")
	# # trainer.train("chatterbot.corpus.english.botprofile")
	

	def detail(self,string):
		self.parent.film_object.film_id=string
		self.parent.current="DETAIL"
	def getCommand(self):
		for i in range(3):
			text=self.recordAudio()
			if text:
				return text.lower()
			elif i<2:
				self.add_response("Can you speak again?")
		return 0

	def recordAudio(self):
		 #create a recognizer object
		r = sr.Recognizer()
		#initialize the micro
		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source)
			print("You said: ",end="")
			audio = r.listen(source,phrase_time_limit=5)
		#Use google recognition
		data=''
		try:
			data=r.recognize_google(audio, language="en")
			print(data)
			self.add_speech(data)
			return data
		except sr.UnknownValueError:
			print("...")
			return 0
		except sr.RequestError as e:
			print(e)
			return 0

	def speak(self,text):
		self.engine.say(str(text))
		self.engine.runAndWait()
			
	def say_bye(self):
		text="Hope I helped you. See you again!"
		return text

	def assistant(self):
		start_speech="What can I help you?"
		self.add_response(start_speech)
		while True:
			text=self.getCommand()
			# text=input()
			if text==0 or "bye" in text:
				time.sleep(1)
				self.add_response(self.say_bye())
				self.ids.controller.text="Start"
				return False
			else:
				response=self.cinebot.get_response(text)
				self.add_response(response)
	def start_assistant(self):
		thread=Thread(target=self.assistant)
		if self.ids.controller.text=="Start":
			self.ids.controller.text="Stop"
			thread.start()
		else:
			self.ids.controller.text="Start"
			return False

	def add_speech(self,speech):
		text=str(speech)
		text_speech=MDLabel(text=text,halign="right")
		speech_card= MDCard(
			orientation= "vertical",
			size_hint=[None,None],
			size=[self.size[0]-20,text_speech.size[1]],
			spacing=8,
			padding=30,

			radius= [25,25,0,25 ]
			)
		speech_card.add_widget(text_speech)
		self.ids.all_conversations.add_widget(speech_card)
		self.ids.speech_scroll_view.scroll_to(speech_card)

	def film_query(self,sql):
		film_imgs=[]
		film_ids=[]
		conn=sqlite3.connect(r"C:\sqlite\db\cinema.db")
		cursor=conn.cursor()
		cursor.execute(sql)
		records=cursor.fetchall()
		for row in records:
			film_imgs.append(row[1])
			film_ids.append(row[0])
		return film_ids,film_imgs
	def add_response(self,response):
		text=str(response)
		text_speech=MDLabel(text=text,halign="left",size_hint_x=None,width=self.size[0]-50)
		space=MDLabel(size_hint=(None,None),height=50)
		film_result=MDBoxLayout(orientation="horizontal",spacing=(20,0), adaptive_width=True)
		keywords=["trending film","high rating film","you to pick","coming soon film","map of our cinema","services price","recently released film"]
		if any(keyword in text for keyword in keywords):
			if "high rating film" in text:
				sql_rating=f"SELECT film_id,image from film order by rating desc limit 3"
				rating_ids,rating_imgs=self.film_query(sql_rating)
				for item in range(len(rating_imgs)):
					film_result.add_widget(CinebotFitImage(source=rating_imgs[item],
						film_id=str(rating_ids[item]),size_hint=(None,None),width=200,radius=[15,15,15,15],on_release=lambda wdt:self.detail(wdt.film_id)))
					film_result.add_widget(MDLabel(text="",size_hint_x=None,width=40))
			elif "coming soon film" in text:
				today=date.today()
				sql_date=f"SELECT film_id,image from film where release_date > '{today}'order by release_date asc limit 3"
				date_ids,date_imgs=self.film_query(sql_date)
				for item in range(len(date_imgs)):
					film_result.add_widget(CinebotFitImage(source=date_imgs[item],
						film_id=str(date_ids[item]),size_hint=(None,None),width=200,radius=[15,15,15,15],on_release=lambda wdt:self.detail(wdt.film_id)))
					film_result.add_widget(MDLabel(text="",size_hint_x=None,width=40))
			elif "recently released film" in text:
				today=date.today()
				sql_recently=f"SELECT film_id,image from film where release_date < '{today}'order by release_date desc limit 1"
				recently_ids,recently_imgs=self.film_query(sql_recently)
				for item in range(len(recently_imgs)):
					film_result.add_widget(CinebotFitImage(source=recently_imgs[item],
						film_id=str(recently_ids[item]),size_hint=(None,None),width=200,radius=[15,15,15,15],on_release=lambda wdt:self.detail(wdt.film_id)))
					film_result.add_widget(MDLabel(text="",size_hint_x=None,width=40))
			elif "trending film" in text or "you to pick" in text:
				sql_trending=f"SELECT film_id,image from film order by popularity desc limit 3"
				trending_ids,trending_imgs=self.film_query(sql_trending)
				for item in range(len(trending_imgs)):
					film_result.add_widget(CinebotFitImage(source=trending_imgs[item],
						film_id=str(trending_ids[item]),size_hint=(None,None),width=200,radius=[15,15,15,15],on_release=lambda wdt:self.detail(wdt.film_id)))
					film_result.add_widget(MDLabel(text="",size_hint_x=None,width=40))
			speech_card= MDCard(
				orientation= "vertical",
				size_hint=[None,None],
				size=[self.size[0]-20,text_speech.size[1]+film_result.size[1]],
				spacing=8,
				padding=30,
				ripple_behavior= True,
				radius= [25,25,25,0 ]
				)
			speech_card.add_widget(text_speech)
			speech_card.add_widget(space)
			speech_card.add_widget(film_result)
		else:
			speech_card= MDCard(
				orientation= "vertical",
				size_hint=[None,None],
				size=[self.size[0]-20,text_speech.size[1]],
				spacing=8,
				padding=30,
				ripple_behavior= True,
				radius= [25,25,25,0 ]
				)
			speech_card.add_widget(text_speech)
		self.ids.all_conversations.add_widget(speech_card)
		self.speak(text)
		self.ids.speech_scroll_view.scroll_to(speech_card)