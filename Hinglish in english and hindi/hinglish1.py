from googletrans import Translator

def translate_statement(statement):
    translator = Translator()
    # Split the statement into words
    words = statement.split()
    
    # Initialize an empty list to store the translated words
    translated_words = []
    
    # Translate each word individually
    for word in words:
        # If the word is a common noun or proper noun (e.g., a name), keep it in English
        if word.isalpha() and not word.isnumeric():
            translated_words.append(word)
        else:
            # Translate non-noun words to Hinglish
            translation = translator.translate(word, src='en', dest='hi')
            translated_words.append(translation.text)

    # Reconstruct the translated statement
    translated_statement = ' '.join(translated_words)
    
    return translated_statement

# Define the English statements
english_statements = [
    "Definitely share your feedback in the comment section.",
    "So even if it's a big video, I will clearly mention all the products.",
    "I was waiting for my bag."
]

# Translate and print the statements
for statement in english_statements:
    translated = translate_statement(statement)
    print(f'English Statement: "{statement}"')
    print(f'Expected Hinglish Translation: "{translated}"\n')
