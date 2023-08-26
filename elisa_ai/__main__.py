import openai
import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()
listener = sr.Recognizer()
openai.api_key = "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"

while True:
    with sr.Mictophone() as source:
         print("Elisa a.i active.. how can I help you..?")
         voice = listener.listen(source)
         data = "listener.recognize_google(voice)
         model = "text-davinci-003"

         if "exit" in data:
             break
           
     completion = openai.Completion.create(model ="text-davinci-003",
       prompt = data,
       max_tokens = 4196,
       temperature = 0.5,
       n = 1,
       stop = None)
     response = completion.choices[0].text
     choice = int(input("press 1 for text response and 2 for a voice assisted response.."))

     if choice == 1:
         print(response)
     else:
         print(response)
         engine.say(response)
         engine.runAndWait()

      repeat = input("here is your answer , do you ask for something more..?")
      if repeat in ["No","no","No"]:
          break
