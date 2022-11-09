#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 02:11:45 2022

@author: colinxiong
"""

import tkinter as tk
from googletrans import Translator, LANGUAGES
import speech_recognition as sr
import pyttsx3 

r = sr.Recognizer()

root = tk.Tk()
root.title("Language Translator with GUI")
window_width = 1000
window_height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
 
input_language_choice = tk.StringVar()
translate_language_choice = tk.StringVar()

#language_choices = ('English', "Japanese", "C")
language_choices = tuple(LANGUAGES.values())
input_language_choice.set("Auto Detect Language")
translate_language_choice.set("...")

def Translate():
    translator = Translator()
    if input_language_choice != "Auto Detect Language":
        result = translator.translate(input_var.get(), dest=translate_language_choice.get())
    else:
        result = translator.translate(input_var.get(), src = input_language_choice.get(), dest=translate_language_choice.get())
    return output_var.set(result.text)

def Record():    
    with sr.Microphone() as source:
        audio = r.record(source, duration=(5))
        
        my_text = r.recognize_google(audio)
        return input_var.set(my_text)

def Speak():
    def speak_text(command):
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()
    
    speak_text(output_var)
    
input_choice_menu = tk.OptionMenu(root,input_language_choice,*language_choices)
tk.Label(root,text="Choose an Input Language").grid(row=0,column=0)
input_choice_menu.grid(row=0,column=1)

translation_choice_menu = tk.OptionMenu(root,translate_language_choice,*language_choices)
tk.Label(root,text="Choose a Translated Language").grid(row=0,column=2)
translation_choice_menu.grid(row=0,column=3)

tk.Label(root, text = "Enter Text").grid(row=1, column=0)
input_var = tk.StringVar()
text_box = tk.Entry(root,textvariable=input_var).grid(row=1,column = 1)


tk.Label(root,text = "Output Text").grid(row=1,column =2)
output_var = tk.StringVar()
text_box = tk.Entry(root,textvariable = output_var).grid(row=1,column = 3)


button = tk.Button(root, text="Translate", command=Translate, relief = 'groove').grid(row=3,column=1,columnspan = 3)
button_record = tk.Button(root, text="Record", command=Record, relief = 'groove').grid(row=3,column=0,columnspan = 3)
button_speak = tk.Button(root, text="Voice", command=Speak, relief = 'groove').grid(row=3,column=3,columnspan = 3)



root.mainloop()