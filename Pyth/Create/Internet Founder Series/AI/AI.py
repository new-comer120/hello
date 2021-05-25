import speech_recognition
import pyttsx3
from datetime import datetime

now = datetime.now()

name = input("Please enter your name before using this: ")
today = now.strftime("%B %D, %Y")

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

with speech_recognition.Microphone() as mic:
    print("Robot: I'm listening")
    audio = robot_ear.listen(mic)

print("Robot:...")

try:
    you = robot_ear.recognize_google(audio)
except:
    you = ""
print("you: " + you)

if "":
    robot_brain = "I can hear you, try again."
elif "hello" in you:
    robot_brain = "Hello " + name
elif "today" in you:
    robot_brain = today
elif you == "WWDC 2021":
    robot_brain = "WWDC 2021 will start from June 7 to 11. You can see details in https://developer.apple.com/wwdc21/"
else:
    robot_brain = "Sorry, we not supported this question."    
print("Robot:", robot_brain)

robot_mouth = pyttsx3.init()
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()