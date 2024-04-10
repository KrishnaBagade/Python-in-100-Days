names = []
with open("./Input/Names/invited_names.txt",mode="r") as file:
    for i in range(8):
      x = file.readline()
      y = x.strip("\n")
      names.append(y)
for i in range(8):
    with open("./Input/Letters/starting_letter.txt",mode="r") as file_:
        sample_1 = file_.read()
        corrected_sample_1 = sample_1.replace("[name]",names[i])
        print(corrected_sample_1)
    with open(f"./Output/ReadyToSend/letter_for_{names[i]}.txt",mode="w") as file_a:
        file_a.write(corrected_sample_1)
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
