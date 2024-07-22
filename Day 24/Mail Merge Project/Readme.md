# Letter Generation Script

## Overview
This script generates personalized invitation letters by replacing placeholders in a template
letter with actual names from a list of invited guests. The final letters are saved in a
designated folder, ready to be sent out.

## File Structure
```
project_folder/
│
├── Input/
│   ├── Names/
│   │   └── invited_names.txt
│   └── Letters/
│       └── starting_letter.txt
│
└── Output/
    └── ReadyToSend/
        ├── letter_for_John.txt
        ├── letter_for_Jane.txt
        └── ...
```

## How It Works
1. **Read Invited Names**: The script reads names from `invited_names.txt`.
2. **Read Template Letter**: It reads a template letter from `starting_letter.txt`.
3. **Personalize Letters**: The script replaces the placeholder `[name]` in the template
with each name from the list.
4. **Save Personalized Letters**: Each personalized letter is saved in the `ReadyToSend`
folder with a filename indicating the recipient's name.

## Steps to Run the Script

1. **Prepare the Input Files**:
    - `invited_names.txt`: Place the list of invited names, one name per line, in this file.
    - `starting_letter.txt`: Create a template letter with a placeholder `[name]` where the
   recipient's name should be inserted.

2. **Run the Script**: Execute the script in your Python environment.

3. **Check the Output**: The personalized letters will be saved in the `ReadyToSend` folder.

## Notes
- Ensure that the `invited_names.txt` and `starting_letter.txt` files are correctly placed in
the `Input/Names/` and `Input/Letters/` directories, respectively.
- The script currently processes the first 8 names in `invited_names.txt`. Modify the range 
in the for loops if you have more or fewer names.
- The script assumes that the `ReadyToSend` folder exists. Ensure that this folder is created
beforehand.
