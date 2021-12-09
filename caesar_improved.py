alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text,shift_input,cipher_direction):
    final_string = ""
    if cipher_direction == "decode":
            shift_input *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        
        new_position = position + shift_input      
        new_letter = alphabet[new_position]
        final_string += new_letter
    print(f"{final_string}")    

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(start_text=text,shift_input=shift,cipher_direction=direction)

 

