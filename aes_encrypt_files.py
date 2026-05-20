import time
from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)

files = [
    "text.txt",
    "pdf.pdf",
    "video.mp4"
]

print("--- ШИФРУВАННЯ РЕАЛЬНИХ ФАЙЛІВ AES ---")
print(f"{'Файл':<15} | {'Час шифрування (сек)':<25}")
print("-" * 50)

for file_name in files:

    with open(file_name, "rb") as file:
        file_data = file.read()

    start_time = time.perf_counter()

    encrypted_data = fernet.encrypt(file_data)

    end_time = time.perf_counter()

    encrypted_file_name = file_name + ".aes"

    with open(encrypted_file_name, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

    execution_time = end_time - start_time

    print(f"{file_name:<15} | {execution_time:<25.6f}")

print("-" * 50)