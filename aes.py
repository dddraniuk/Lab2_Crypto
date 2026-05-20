from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

message = b"Hello World"

encrypted_message = cipher.encrypt(message)
decrypted_message = cipher.decrypt(encrypted_message)

print("Key:", key)
print("Encrypted:", encrypted_message)
print("Decrypted:", decrypted_message)