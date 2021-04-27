from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import speech_recognition as sr 
import os
from chatterbot.comparisons import LevenshteinDistance
import chatterbot.filters
import playsound
import time
from demopyttsx3 import *
import datetime
import calendar 
import wikipedia
import random
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
    	filters=[chatterbot.filters.get_recent_repeated_responses]

)

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(cinebot)

trainer.train("chatterbot.corpus.english.greetings")
trainer.train("chatterbot.corpus.english.cinema")


# def getCommand():
# 	for i in range(3):
# 		text=recordAudio()
# 		if text:
# 			return text.lower()
# 		elif i<2:
# 			speak("Can you speak again?")
# 	return 0

# def recordAudio():
# 	 #create a recognizer object
# 	r = sr.Recognizer()
# 	#initialize the micro
# 	with sr.Microphone() as source:
# 		r.adjust_for_ambient_noise(source)
# 		print("You said: ",end="")
# 		audio = r.listen(source,phrase_time_limit=5)
# 	#Use google recognition
# 	data=''
# 	try:
# 		data=r.recognize_google(audio, language="en")
# 		print(data)
# 		return data
# 	except sr.UnknownValueError:
# 		print("...")
# 		return 0
# 	except sr.RequestError as e:
# 		print('Error Code: '+e)
# 		return 0

# def speak(text):
# 	print(text)
# 	engine.say(str(text))
# 	engine.runAndWait()
		
# def say_bye():
# 	speak("Hope I helped you. See you again!")

# def assistant():
# 	speak("What can I help you?")
# 	while True:
# 		text=getCommand()
# 		if text==0:
# 			time.sleep(1)
# 			say_bye()
# 			break
# 		else:
# 			response=cinebot.get_response(text)
# 			speak(response)

# if __name__=="__main__":
# 	assistant()
