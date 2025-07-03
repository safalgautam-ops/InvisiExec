from stegimg import encode as img_encode, decode as img_decode
from stegfiles import encode_file as file_encode, decode_file as file_decode
from crypto import encrypt, decrypt
import base64
from PIL import Image

def main():
    print(":: Steganography ::")
    print("1. Encode")
    print("2. Decode")
    choice = input("Choose (1/2): ").strip()
    filepath = input("Enter file path (with extension): ").strip()
    is_image = filepath.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.webp'))

    if choice == '1':
        msg = input("Enter message to hide: ")
        password = input("Enter password: ")
        packed = encrypt(msg, password)
        # Optionally base64-encode for text-based steganography
        data_to_hide = base64.b64encode(packed).decode('utf-8')
        if is_image:
            img_encode(filepath, data_to_hide)
        else:
            out_file = input("Enter output file path: ").strip()
            file_encode(filepath, out_file, data_to_hide)
        print("Message encrypted and hidden.")
    elif choice == '2':
        password = input("Enter password: ")
        if is_image:
            extracted = img_decode(filepath)
        else:
            extracted = file_decode(filepath)
        packed = base64.b64decode(extracted.encode('utf-8'))
        try:
            msg = decrypt(packed, password)
            print("Decrypted message:", msg)
        except Exception as e:
            print("Decryption failed:", e)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()