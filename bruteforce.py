encrypted_text = "Khoor Zruog"

print("--- BRUTE FORCE ДЛЯ ШИФРУ ЦЕЗАРЯ ---\n")

for key in range(1, 26):

    decrypted_text = ""

    for char in encrypted_text:

        if char.isalpha():

            shift = key

            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))

            decrypted_text += decrypted_char

        else:
            decrypted_text += char

    print(f"Ключ {key}: {decrypted_text}")