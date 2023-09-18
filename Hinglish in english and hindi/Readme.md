## Note:- This code translates English sentences into Hinglish sentences which has English + Hindi words.

### Sample:-
English Statement: "Definitely share your feedback in the comment section." 
Expected Hinglish Translation: "Definitely share your feedback in the comment अनुभाग।"

English Statement: "So even if it's a big video, I will clearly mention all the products."
Expected Hinglish Translation: "So even if इसका a big वीडियो, I will clearly mention all the उत्पाद।"

English Statement: "I was waiting for my bag."
Expected Hinglish Translation: "I was waiting for my थैला।"

### Algorithm used:-
This code uses Google Translate API for translation. The algorithm used for translation within the Google Translate API is a neural machine translation (NMT) algorithm.
Neural machine translation is a type of machine translation that relies on artificial neural networks to learn and generate translations. It has become the dominant approach for machine translation in recent years because it can capture complex linguistic patterns and produce more accurate translations compared to older statistical machine translation methods.

### To run the code you've provided on your local system, you'll need to have Python installed, and you'll need to install the googletrans library, which is not part of the Python standard library. Here are the steps to set up and run this code:

#### 1) Install Python:
If you don't have Python installed on your local system, download and install it from the official 
Python website: "https://www.python.org/downloads/"

#### 2) Install the googletrans library:
You can install the googletrans library using pip, which is the Python package manager.
Open your terminal or command prompt and run the following command:-
  "pip install googletrans==4.0.0-rc1"
This will install the googletrans library version specified in the command.

#### 3) Create a Python script:
Copy the code you provided and paste it into a Python script file (e.g., translate.py).

#### 4) Run the Python script:
Open a terminal or command prompt, navigate to the directory where your Python script is located, and then run the script using the following command:
  "python translate.py"
Make sure you have an active internet connection because the code relies on the Google Translate API to perform translations.

The script will execute, and you should see the translated statements printed to the console.
