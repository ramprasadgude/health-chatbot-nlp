from deep_translator import GoogleTranslator

def translate(text, target="en"):
    try:
        return GoogleTranslator(source='auto', target=target).translate(text)
    except:
        return text