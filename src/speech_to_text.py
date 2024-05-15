import speech_recognition as sr
from textwrap import TextWrapper

print(sr.__version__)

def speech_text():
    # Set up mic
    my_mic = sr.Microphone(device_index=1)

    # Set up speech to text
    r = sr.Recognizer()

    # Define text wrapper options (adjust width and subsequent_indent as needed)
    wrapper = TextWrapper(width=80)

    with my_mic as source:
        print("Speak")
        audio = r.listen(source)

    try:
        # Recognize speech
        text = r.recognize_google(audio)

        # Wrap text using TextWrapper
        wrapped_text = wrapper.fill(text)

        # Write wrapped text to file
        with open("../data/raw/transcript.txt", 'w') as file:
            file.write(wrapped_text)

    except sr.UnknownValueError:
        print("Could not understand audio.")
