################################################
## Last Code Update: 03-03-2022
## By: Akshat Negi
################################################

#*******************************#
## Load all required packages
#*******************************#

# pip install SpeechRecognition
import speech_recognition
# pip install pyttsx3
import pyttsx3
# pip install wikipedia
import wikipedia
import datetime
import os
import sys
from sys import platform as ptf
from listenScript import listenExternalSpeech as LES




class noelle:

    def __init__(self) -> None:

        if ptf == 'win32' :
            self.chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        elif ptf =='linux' or ptf =='linux2':
            self.chrome_path = '/usr/bin/google-chrome'
        else:
            print("OS not supported. Please launch in another machine")
            exit(1)
        pass

print("hello all packages loaded")