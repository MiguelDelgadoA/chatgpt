import api_key
import os
#pip install openai
import openai
#pip install gTTS
from gtts import gTTS
#pip install SpeechRecognition
#pip install pyaudio
#sino no puede usar pyaudio instalar en ubuntu
#sudo apt-get install portaudio19-dev python-all-dev python3-all-dev
import speech_recognition as sr


##################################
#sudo apt install sox
#sudo apt install libsox-fmt-mp3
#play music.mp3
def select_option():
  error = True
  while error:
      option = input('''\nSelecione el idiona a usar o salir:
=================================== 
(1) For English. 
(2) Para español. 
(3) Per italiano. 
(4) Pour le français. 
(5) Für deutsch. 
(6) Exit.
Option: ''')
      language_select = language(option)
      if language_select != "x":
        error = False
        return language_select
      print("\nOpcion no valida, intente nuevamente\n")


      


##===========================================================
##Select option language
def language(option):
  if option == "1":
    return "en"
  elif option == "2":
    return "es"
  elif option == "3":
    return "it"
  elif option == "4":
    return "fr"
  elif option == "5":
    return "de"
  elif option == "6":
    return "6"
  else:
    return "x"



##===============================================================
##Grabador de audio


def listen(option_language):
  listener = sr.Recognizer()

  try:
      with sr.Microphone() as source:
           print("Escuchando...")
           audio = listener.listen(source)
           text = listener.recognize_google(audio, language=option_language)
           print(text)


  except:
      pass
  return text
 

###================================================================
##CHAT_GPT
def chat_gpt(pregunta):
  openai.api_key = api_key.key
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=pregunta,
    temperature=0.5,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  respuesta = response["choices"][0]["text"]
  return respuesta


##=================================================================
##gTTs text to audio
def text_to_audio(respuesta,option_language):
  tts = gTTS(text=respuesta, lang=option_language)
  tts.save("audio.mp3")


while True:
  option = select_option()

  
  if option == "6":
    break

  option_language = option

  text_record = listen(option_language)
  respuesta = chat_gpt(text_record)
  print(respuesta)
  text_to_audio(respuesta,option_language)
  
  os.system('play audio.mp3')
  os.system('rm audio.mp3')
 
  print("==============================================================")

print("El chat ha finalizado")