alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 
'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
 'x', 'y', 'z']
import art
print(art.logo)
def ceasar(start_text,shift_input,direction_input):
    last_text = ""
    if direction_input == "decode":
        shift_input *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_input
            new_letter = alphabet[new_position]
            last_text += new_letter
        else:
            last_text += char

    print(f"{last_text}") 
should_continue = True    
while should_continue:
    direction = input("enter encode if you want to encode and decode if you want to decode").lower()
    text = input("enter the text").lower()
    shift = int(input("enter the amount of shift"))
    shift = shift % 26
    ceasar(start_text=text,shift_input=shift,direction_input=direction) 
    choice = input("enter yes to encode or decode again and no to stop").lower()
    if choice == "no":
        should_continue = False
        print("Goodbye")
    else:
        pass    




    
