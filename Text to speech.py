import pyttsx3

def text_to_speech(text):
    

    engine = pyttsx3.init()

    # Set desired voice and rate (optional)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) 
    engine.setProperty('rate', 150)  

    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    text_input = input("Enter the text you want to convert to speech: ")
    text_to_speech(text_input)
