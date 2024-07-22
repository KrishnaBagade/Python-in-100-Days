# NATO Phonetic Alphabet Converter

## Overview
This script converts a given word or phrase into its corresponding NATO phonetic alphabet code words. The NATO phonetic alphabet assigns code words to the letters of the English alphabet to ensure clarity and avoid confusion during communication.

## Features
1. **Read NATO Phonetic Alphabet**: Reads the NATO phonetic alphabet from a CSV file and creates a dictionary.
2. **Convert Words to Phonetic Code**: Converts user-inputted words into their corresponding phonetic code words.

## File Structure
```
project_folder/
│
├── nato_phonetic_alphabet.csv
└── main.py
```

### `nato_phonetic_alphabet.csv`
This file contains the NATO phonetic alphabet in the following format:
```
letter,code
A,Alfa
B,Bravo
C,Charlie
...
```

### `main.py`
The main script that performs the conversion.

## How It Works
1. **Read and Parse CSV**: The script reads the `nato_phonetic_alphabet.csv` file and creates a dictionary where each letter maps to its corresponding phonetic code word.
2. **User Input**: Prompts the user to enter a word or phrase.
3. **Generate Phonetic Code**: Converts each letter of the input into its corresponding phonetic code word using the created dictionary.
4. **Display Result**: Prints the phonetic code words.

## Instructions

1. **Prepare the CSV File**:
   - Ensure the `nato_phonetic_alphabet.csv` file is in the same directory as the script.
   - The CSV file should contain the NATO phonetic alphabet with each row containing a letter and its corresponding code word.

2. **Run the Script**:
   - Execute the `main.py` script in your Python environment.

3. **Enter Words or Phrases**:
   - When prompted, enter the word or phrase you want to convert.
   - The script will display the corresponding phonetic code words.

## Dependencies
- Python 3.x
- Pandas library (for reading and parsing the CSV file)

## Notes
- The script assumes that the `nato_phonetic_alphabet.csv` file is correctly formatted and placed in the appropriate directory.
- Special characters and numbers are not processed and will be ignored in the conversion.