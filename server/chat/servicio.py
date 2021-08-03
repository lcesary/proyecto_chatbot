from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
nombre = "luis"
chats = ChatBot(nombre)
talk=['hola','que tal','tengo una pregunta',
      'si, dime','como te llamas','mi nombre es '+nombre]
trainer = ChatterBotCorpusTrainer(chats)
trainer = ListTrainer(chats)
trainer.train(talk)
#trainer.train("chatterbot.corpus.spanish")
while True:
    peticion = input('Tu; ')
    respuesta = chats.get_response(peticion)
    print(nombre+': ',respuesta)
