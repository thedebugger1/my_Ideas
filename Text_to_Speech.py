import pyttsx3

convertor = pyttsx3.init()
convertor.setProperty('rate', 200)
convertor.setProperty('volume', 1)

text = input("Enter a phrase: ")
convertor.say(text)

convertor.runAndWait()

