import speech_recognition as sr
import pyaudio
import keyboard
import turtle
import asyncio
import time

screen = turtle.Screen()
screen.tracer(0)
screen.setup(200, 200, -1, 550)
screen.setworldcoordinates(0,0,1,1)
turtle.speed(0)

turtle.penup()
turtle.goto(0,0)
turtle.pendown()

def square(color):
    turtle.color(color)
    turtle.begin_fill()
    turtle.goto(0,1)
    turtle.goto(1,1)
    turtle.goto(1,0)
    turtle.goto(0,0)
    turtle.end_fill()
    screen.update()

r = sr.Recognizer()
'''with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration = 5)
    r.energy_threshold += 100
    print(r.energy_threshold)'''
    
while True:
    with sr.Microphone() as source:
        #r.adjust_for_ambient_noise(source, duration = 1)
        r.energy_threshold = 3300
        print("Say something!")
        audio = r.listen(source)
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        command = r.recognize_google(audio)
        if command[0:8] == "for what":
            command = "forward"
        if command.find(" ") != -1:
            command = command[0:command.find(" ") + 1]
        if command in ("dawn", "doubt"):
            command = "down"
        if command in ("laugh", "less", "laugh "):
            command = "left"
        if command == "show":
            command = "shoot"
        if command == 'and':
            command = 'forward'
        
        print("Google Speech Recognition thinks you said " + command)
        
        #forward - black
        #down - blue
        #right - green
        #left - yellow
        #shoot - red
        #stop - white
        if command == "forward":
            for i in range(1):
                square('black')
                time.sleep(0.03)
                square('grey')
                time.sleep(0.03)
        if command == "down":
            for i in range(2):
                square('black')
                time.sleep(0.03)
                square('grey')
                time.sleep(0.03)
        if command == "right":
            for i in range(3):
                square('black')
                time.sleep(0.03)
                square('grey')
                time.sleep(0.03)
        if command == "left":
            for i in range(4):
                square('black')
                time.sleep(0.03)
                square('grey')
                time.sleep(0.03)
        if command == "shoot":
            for i in range(5):
                square('black')
                time.sleep(0.03)
                square('grey')
                time.sleep(0.03)
        if command == "stop":
            for i in range(6):
                square('black')
                time.sleep(0.03)
                square('grey')
                time.sleep(0.03)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
screen.mainloop()
