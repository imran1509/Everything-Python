# Install an external module and use it to perform an operation of your interest.
# In this I used pyttsx3 module. which we can use to do text to speech conversion

import pyttsx3
engine = pyttsx3.init()
engine.say("I am Batman, I am vengeance")
engine.runAndWait()