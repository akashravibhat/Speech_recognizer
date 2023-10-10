import speech_recognition as sr
import time
# import pyaudio
from googletrans import Translator
import wikipedia


lan={'ASSAMESE':'as-IN',
    'BENGALI':'bn-IN',
    'BODO':'brx-IN',
    'DOGRI':'doi-IN',
    'ENGLISH':'eng-IN',
    'GUJARATI':'gu-IN',
    'HINDI':'hi-IN',
    'KANNADA':'kn-IN',
    'KASHMIRI':'ks-IN',
    'KONKANI':'gom-IN',
    'MAITHILI':'mai-IN',
    'MALAYALAM':'ml-IN',
    'MANIPURI':'mni-IN',
    'MARATHI':'mr-IN',
    'NEPALI':'ne-IN',
    'ORIYA':'or-IN',
    'PUNJABI':'pa-IN',
    'SANSKRIT':'sa-IN',
    'SANTALI':'sat-IN',
    'SINDHI':'sd-IN',
    'TAMIL':'ta-IN',
    'TELEGU':'te-IN',
    'URDU':'ur-IN'}

a=input("SELECT LANGUAGE:1.ENGLISH\n2.HINDI\n3.KANNADA\n")

if(a not in lan.keys()):
    print("sorry not available")
else:
    r = sr.Recognizer()

    # Reading Microphone as source
    # listening the speech and store in audio_text variable
    start=time.time()
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        audio_data = r.record(source, duration=5)
        print("Recognizing...:")
        # convert speech to text
        
        
        try:
            text = r.recognize_google(audio_data,language=lan[a])
            print("You said:",text)
            # translator = Translator()

            # engtext = translator.translate(text,src="kn-IN")

            # print(engtext)
            result = wikipedia.summary(text,sentences = 2)

            print(result)

        except:
            print(" PROBLEM! Sorry couldn't hear your voice")


# translator = Translator()
#         sample_text = 'Hi my name is subash'
#         det = translator.detect(sample_text)
#         print(det)
#         output= translator.translate(sample_text, dest="ta")
#         print(output)