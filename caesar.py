def caesar_encrypt(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        
        else:
            result += char

    return result


message = "Hello World"
shift_key = 3
encrypted_message = caesar_encrypt(message, shift_key)

print(f"Повідомлення: {message}")
print(f"Шифр Цезаря ({shift_key}): {encrypted_message}")