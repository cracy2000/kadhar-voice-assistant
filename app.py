import streamlit as st
import speech_recognition as sr

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def talk(text):
    engine.say(text)
    engine.runAndWait()

st.title("🧠 kadhar - Voice Assistant")

if st.button("🎙 Speak"):
    with sr.Microphone() as source:
        st.info("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            st.success(f"You said: {command}")
            if "time" in command:
                import datetime
                time = datetime.datetime.now().strftime('%I:%M %p')
                talk("Current time is " + time)
            elif "who is" in command:
                import wikipedia
                person = command.replace("who is", "")
                info = wikipedia.summary(person, sentences=1)
                talk(info)
                st.write(info)
            else:
                talk("Sorry I can't do that yet")
        except:

            st.error("Sorry, I didn't get that.")
