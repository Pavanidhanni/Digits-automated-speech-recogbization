#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pyaudio


# In[2]:


pip install speechrecognition


# In[3]:


pip install pydub


# In[ ]:


#importing requried libraries
import speech_recognition as sr
import pyttsx3


r = sr.Recognizer()


def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

while(1):

    try:
    # use the microphone as source for input.
        with sr.Microphone() as source2:
            # waiting time is 1sec for recognizer to adjust the energy threshold based on the surrounding noise level
        
            r.adjust_for_ambient_noise(source2, duration=0.2)
            #listens for the user's input
            audio2 = r.listen(source2)
           
            
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            
            #Printing what we said
            print("You said ",MyText)
            SpeakText(MyText)
            
    #exceptions handling to handle exceptions at the runtime      
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occurred")


# In[ ]:





# In[ ]:





# In[ ]:




