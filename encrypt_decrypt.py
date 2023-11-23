alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']


def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
           position = alphabet.index(char)
           new_position = (position + shift_key) % 26
           cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"Here's is the text after encrytpion: {cipher_text}")


def decryption(cipher_text, shift_key):
    palin_text = ""
    for char in cipher_text:
        if char in alphabet:
           position = alphabet.index(char)
           new_position = (position + shift_key) % 26
           palin_text += alphabet[new_position]
        else:
            palin_text += char
    print(f"Here's is the text after decrytpion: {palin_text}")

wanna_end=False
while not wanna_end:
   what_to_do = input("Type 'encrypt' for encryption, type 'decrypt' for decryption:\n")
   text = input("Type your message:\n").lower()
   shift = int(input("Enter shift key:\n"))
   if what_to_do == "encrypt":
      encryption(plain_text=text, shift_key=shift)
   elif what_to_do=="decrypt":
      decryption(text, shift)
   play_again=input("Type 'yes' to continue, type 'no' to exit.\n")
   if play_again=='no':
       wanna_end=True
       print("Have a good day! Byeee.....")


