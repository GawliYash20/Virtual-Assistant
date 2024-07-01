import speech_recognition as sr

def Listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as mic:
        print("Listening. . .")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(mic, 0, 2)


    try:
        print("recognizing...")
        query = recognizer.recognize_google(audio, language="en-in")
        print(f"You said: {query} \n")


    except:
        return ""

    query = str(query)
    return query.lower()

