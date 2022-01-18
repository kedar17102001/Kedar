import speech_recognition as sr
import pyttsx3
from googletrans import Translator
voice = sr.Recognizer()
def SpeakText(command):
    engine=pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
with sr.AudioFile('data\Songs.PK_-01-Saturday-Saturday.aiff') as source:
    voice.adjust_for_ambient_noise(source)
    print("speak")
    audio2 = voice.record(source)
    Text = voice.recognize_google(audio2)
    Text = Text.lower()
    print("You say something :{}".format(Text))
T=Text

"""print(sr.Microphone.list_microphone_names())
mic = sr.Microphone(device_index=0)
with mic as source:
    print("speak:")
    voice.adjust_for_ambient_noise(source)
    audio = voice.listen(source)
result = voice.recognize_google(audio)
print(result)"""

source_text=T
translator = Translator()
result_1=translator.translate(source_text, dest='fr')
P=result_1.text
print(P)
SpeakText(P)