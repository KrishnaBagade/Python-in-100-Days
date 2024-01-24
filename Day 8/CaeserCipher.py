from art import logo

def caesar(word,shift,direction):
  end_word=""
  if direction == "encode":
    if shift > 25:
      shift%25
    for char in word:
      if char in alphabet:
        index_num=alphabet.index(char)
        index_num+=shift
        while index_num>25:
          index_num-=25
        end_word+=alphabet[index_num]
      else:
        end_word+=char
    print(f'The encoded text is {end_word}')
  elif direction == "decode":
    if shift > 25:
      shift%25
    for char in word:
      if char in alphabet:
        index_num=alphabet.index(letter)
        index_num-=shift
        while index_num<0:
          index_num+=25
        end_word+=(alphabet[index_num])
      else:
        end_word+=char
    print(f'The decoded text is {end_word}')
  else:
    print("Please specify if you wish to encode or decode your message.")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
while True:  
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift1 = input("Type the shift number:\n")
  if shift1.isdigit():
    shift=int(shift1)
    caesar(word=text,shift=shift,direction=direction)
  else:
    print("Please enter a proper whole number by which you want to encode/decode your message by.")
  run_again=input("Type yes if you wish to run the program again otherwise type no?\n").lower()
  if run_again == "no" :
    print("Goodbye")
    break