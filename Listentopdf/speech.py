import pyttsx3


def text_to_speech(text):
    """
    Function to convert text to speech
    :param text: text
    :param gender: gender
    :return: None
    """

    try:
        engine = pyttsx3.init()

        # Setting up voice rate
        engine.setProperty('rate', 125)

        # Setting up volume level  between 0 and 1
        engine.setProperty('volume', 0.8)

        engine.say(text)
        engine.runAndWait()
    except ValueError:
        return " Invalid input"
