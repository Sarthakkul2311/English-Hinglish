from googletrans import Translator, LANGUAGES

def translate_to_hinglish(text):
    # Create a Translator object
    translator = Translator()

    # Detect the input language (English)
    detected_language = translator.detect(text).lang

    # If the detected language is not English, return the input text as is
    if detected_language != 'en':
        return text

    # Translate the English text to Hindi
    hindi_translation = translator.translate(text, src='en', dest='hi')

    # Replace common English words with their Hinglish equivalents
    hinglish_translation = hindi_translation.text
    hinglish_translation = hinglish_translation.replace('feedback', 'feedback')
    hinglish_translation = hinglish_translation.replace('comment section', 'comment section')
    hinglish_translation = hinglish_translation.replace('products', 'products')
    hinglish_translation = hinglish_translation.replace('clearly', 'clearly')
    hinglish_translation = hinglish_translation.replace('mention', 'mention')
    hinglish_translation = hinglish_translation.replace('waiting', 'waiting')
    hinglish_translation = hinglish_translation.replace('bag', 'bag')

    # Replace 'video' with the same word in English
    hinglish_translation = hinglish_translation.replace('टिप्पणी अनुभाग', 'comment section')
    hinglish_translation = hinglish_translation.replace('प्रतिक्रिया', 'feedback')
    hinglish_translation = hinglish_translation.replace('वीडियो', 'video')
    hinglish_translation = hinglish_translation.replace('उत्पादों', 'products')
    hinglish_translation = hinglish_translation.replace('उल्लेख', 'mention')
    hinglish_translation = hinglish_translation.replace('बैग', 'bag')
    hinglish_translation = hinglish_translation.replace('इंतजार', 'wait')

    return hinglish_translation

# Test the translation function with your statements
statements = [
    "Definitely share your feedback in the comment section.",
    "So even if it's a big video, I will clearly mention all the products.",
    "I was waiting for my bag."
]

for statement in statements:
    hinglish_translation = translate_to_hinglish(statement)
    print(f"Statement: {statement}")
    print(f"Hinglish Translation: \"{hinglish_translation}\"\n")
