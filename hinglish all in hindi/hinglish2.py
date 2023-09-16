from googletrans import Translator

def translate_statement(statement):
    translator = Translator()
    translations = translator.translate(statement, src='en', dest='hi')

    # Replace common nouns and proper nouns back to English
    translated_statement = translations.text
    translated_statement = translated_statement.replace('comment section', 'comment section')
    translated_statement = translated_statement.replace('products', 'products')
    translated_statement = translated_statement.replace('bag', 'bag')

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
