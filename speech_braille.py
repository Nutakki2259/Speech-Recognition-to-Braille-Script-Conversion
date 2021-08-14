# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 23:02:09 2021

@author: Nutakki
"""

#import necessary libraries
import speech_recognition as sr
from pybraille import convertText

recognize = sr.Recognizer() #recognize the speech
with sr.Microphone() as source: #using miicrophone as source
    print("Iam Listenting, Speak Anything :")
    audio = recognize.listen(source) #listen to the source audio from the speaker
    try:
        speech = recognize.recognize_google(audio) #using Google speech recogniton
        print("Your speech formated language: {}".format(speech))
        braille_script = convertText(speech) #the speech is converted to Louis Braille script
        print("Your speech in Braille Script : {}".format(braille_script))

    except:
        print("Sorry could not recognize what you said")
        
        
#saving the data
braille_data = 'Speaker Version:' + '\n' + speech + '\n\n' + 'Braille Version:'+'\n' + braille_script

with open("speech_braille.txt", "w",encoding='utf-8') as f:
    f.write(braille_data)
