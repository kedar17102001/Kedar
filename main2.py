import speech_recognition as sr
import pyttsx3
from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
voice=sr.Recognizer()
#part 3: Text_to_speech
#In this code we just converting the text file that are translated into audio file
def SpeakText(command):
    engine=pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

#Trough this we can get input as audio file/ through mic
#we also analyze that audio file and convert it into text file that we can use for translation purpose
while(1):
    try:
        with sr.AudioFile('data\i_don_t_know.wav') as source:
            voice.adjust_for_ambient_noise(source)
            print("speak")
            audio2=voice.record(source)
            Text_1=voice.recognize_google(audio2)
            Text_1=Text_1.lower()
            print("You say something :{}".format(Text_1))

      #SpeakText(Text)
    except sr.RequestError as e:
        print("could not here you :{0}",format(e))

    except sr.UnknownValueError:
        print("Unknown error occured ")

    break


# Part2: Translation using GUI

root = Tk()
root.geometry('1080x400')
root.resizable(0, 0)
root.title("Language Translator GUI ")
root.config(bg='ghost white')

# heading
Label(root, text="LANGUAGE TRANSLATOR", font="arial 20 bold", bg='white smoke').pack()
Label(root, text="Project for MNC's", font='arial 20 bold', bg='white smoke', width='20').pack(side='bottom')

# INPUT

Input_text = Text_1

#OUTPUT TEXT WIDGET

Label(root, text="Output", font='arial 13 bold', bg='white smoke').place(x=490, y=75)
Output_text = Text(root, font='arial 10', height=10, wrap=WORD, padx=10, pady=10, width=135)
Output_text.place(x=50, y=100)

##################
language = list(LANGUAGES.values())

dest_lang = ttk.Combobox(root, values=language, width=22)
dest_lang.place(x=450, y=45)
dest_lang.set('choose output language')


#######  Function Defination for Translation #######
# In this function the inputed text can translate into any language that we want

def Translate(command):
    translator = Translator()
    translated= translator.translate(text=Text_1,dest=dest_lang.get())
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)
    output = translated.text
    #SpeakText(output)
    return output



##########  Translate Button ########
trans_btn = Button(root, text='Translate', font='arial 12 bold', pady=5, command=lambda :Translate(Text_1), bg='royal blue1',
                   activebackground='sky blue')#calling Translate function Through this button

trans_btn.place(x=430, y=300)
trans_btn = Button(root, text='voice', font='arial 12 bold', pady=5, command=lambda :SpeakText(Translate(Text_1)), bg='royal blue1',
                   activebackground='sky blue')# calling Function SpeckText through this button
trans_btn.place(x=520, y=300)

root.mainloop()