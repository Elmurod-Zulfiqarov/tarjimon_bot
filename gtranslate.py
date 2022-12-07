from googletrans import Translator
translator = Translator()

def get_translate(text):
    tarjima = translator.translate(text)
    if tarjima.src == 'uz':
        trans = translator.translate(text, src='uz', dest='en')
    elif tarjima.src == 'en':
        trans = translator.translate(text, src='en', dest='uz')
    else:
        trans = tarjima
    result = f"to {trans.dest} - from {trans.src} \n\n{trans.text}"
    return result
