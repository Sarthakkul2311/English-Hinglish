# English to Hinglish Translator

## Overview
This project is a simple Python script that utilizes the Google Translate API, specifically its Neural Machine Translation (NMT) capabilities, to translate English text into Hinglish. Hinglish is a blend of Hindi and English, commonly used in India, where English and Hindi words are often mixed together.

#### Types of codes 
1) Hinglish in English and hindi: It translates english sentences into hinglish which contains English and hindi both.
2) English to hinglish with all hindi: It translates english sentences into hinglish which contains hindi only.

### Sample of Hinglish in english and hindi:-
English Statement: "Definitely share your feedback in the comment section." <br>
Expected Hinglish Translation: "Definitely share your feedback in the comment अनुभाग।"

English Statement: "So even if it's a big video, I will clearly mention all the products." <br>
Expected Hinglish Translation: "So even if इसका a big वीडियो, I will clearly mention all the उत्पाद।"

English Statement: "I was waiting for my bag." <br>
Expected Hinglish Translation: "I was waiting for my थैला।"

### Sample of hinglish all in hindi
English Statement: "Definitely share your feedback in the comment section."
Expected Hinglish Translation: "निश्चित रूप से टिप्पणी अनुभाग में अपनी प्रतिक्रिया साझा करें।"

English Statement: "So even if it's a big video, I will clearly mention all the products."
Expected Hinglish Translation: "तो भले ही यह एक बड़ा वीडियो है, मैं स्पष्ट रूप से सभी उत्पादों का उल्लेख करूंगा।"        

English Statement: "I was waiting for my bag."
Expected Hinglish Translation: "मैं अपने बैग का इंतजार कर रहा था।"

## Features
 - Translates English text into Hinglish.
 - Utilizes Google's powerful Neural Machine Translation (NMT) model for high-quality translations.
 - Can be used as a standalone script or integrated into other applications.

## Dependencies
Python 3.x
googletrans library (version 4.0.0-rc1 or later)


## Getting Started
### 1) Clone this repository to your local machine:
#### git clone https://github.com/Sarthakkul2311/English-Hinglish.git

### 2) Install the required dependencies using pip:
#### pip install googletrans==4.0.0-rc1

### 3)Run the script:
#### python translate.py

## Usage
 - Modify the english_statements list in the translate.py script to include the English statements you want to translate.
 - Run the script to see the translations from English to Hinglish.

#### Code:-
#Define the English statements
english_statements = [
    "Definitely share your feedback in the comment section.",
    "So even if it's a big video, I will clearly mention all the products.",
    "I was waiting for my bag."
]

#Translate and print the statements
for statement in english_statements:
    translated = translate_statement(statement)
    print(f'English Statement: "{statement}"')
    print(f'Hinglish Translation: "{translated}"\n')

## Notes
 - Ensure you have an active internet connection while running the script as it relies on the Google Translate API.
 - Be aware that usage of the Google Translate API may be subject to rate limits and usage policies by Google.

## Acknowledgments
This project makes use of the Google Translate API, which is provided by Google.
Feel free to customize and expand upon this README template to provide more details, instructions, or additional sections as needed for your project.
