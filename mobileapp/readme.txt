needed packages, libraries and configuration
pip install kivy 
pip install --force-reinstall git+https://github.com/HeaTTheatR/KivyMD.git
pip install speechrecognition
pip install pyttsx3
pip install spacy 
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.0.0/en_core_web_sm-3.0.0-py3-none-any.whl
pip install chatterbot



go to (user)\appdata\local\programs\python\python37\Lib\site-packages\chatterbot\tagging.py, change line 13 to:
	self.nlp = spacy.load("en_core_web_sm")







cinema.yml is the dataset file for training the chatbot, there's the following step needed to train your bot
- clone the chatterbot-corpus repo from github https://github.com/gunthercox/chatterbot-corpus
- add this dataset file into data file of chatterbot corpus/ english
- train the bot as the code in assistant-screen.py file

*cinebotDB.db is the result of training, it store every data that your chatbot has trained.

