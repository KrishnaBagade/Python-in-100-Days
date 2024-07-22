# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows() word in dict.keys()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
with open("nato_phonetic_alphabet.csv",mode="r") as v:
    lst = v.readlines()
    lst_1 = [letters.strip("\n") for letters in lst]
    lst1 = [letters.split(",") for letters in lst_1]
dict = {word[0]:word[1] for word in lst1}
print(dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
spec_list = [" ","!","#","$","%","&","(",")","*","+","-",".","/",":",";","<","=",">","?","@","[","'\'","]","^","_","{",
             "}","|","quotes","tilde"]
user_word__words = list(input("Enter your word or words to get the phonetic for,(press S to check for characters that will"
                         " not be processed including numbers): "))
# print(user_word__words)
dict_letter = dict.keys()
# user_phonetic_word = {letter:dict[f"{letter.upper()}"] for letter in user_word__words if letter.upper() in dict_letter}
# print(user_phonetic_word)
user_p_w = [dict[f"{letter.upper()}"] for letter in user_word__words]
print(user_p_w)

