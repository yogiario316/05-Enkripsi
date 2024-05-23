from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

keterangan = ["Aplikasi Enkripsi teks ini menggunakan 256-bit", "Yogi Ario :)"]
for i in keterangan:
    print(i)
print("\n")
print("Masukkan teks, angka, atau simbol yang diinginkan")

def aes_encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    padded_text = pad(plaintext.encode('utf-8'), AES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    return iv + encrypted_text

def aes_decrypt(key, encrypted_text):
    iv = encrypted_text[:AES.block_size]
    encrypted_text = encrypted_text[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded_text = cipher.decrypt(encrypted_text)
    decrypted_text = unpad(decrypted_padded_text, AES.block_size)
    return decrypted_text.decode('utf-8')

def main():
    key = get_random_bytes(32)  
    print(f"Generated Key: {key.hex()}")

    while True:
        plaintext = input("Masukkan teks yang ingin dienkripsi: ")
        encrypted_text = aes_encrypt(key, plaintext)
        print(f"Teks terenkripsi: {encrypted_text.hex()}")

        decrypted_text = aes_decrypt(key, encrypted_text)
        print(f"Teks setelah didekripsi: {decrypted_text}")

        choice = input("Tekan 1 untuk memasukkan lagi atau tekan Enter untuk keluar: ")
        if choice != '1':
            break

if __name__ == "__main__":
    main()
