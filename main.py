from stegimg import encode as img_encode, decode as img_decode
from stegfiles import encode_file as file_encode, decode_file as file_decode
from crypto import encrypt, decrypt, check_password
import base64
from PIL import Image
import os

def check_file_type(filepath):
    """Return 'image' for supported images, 'file' for other supported files, or None if unsupported."""
    if not os.path.isfile(filepath):
        return None
    image_exts = ('.png', '.jpg', '.jpeg', '.bmp', '.webp')
    file_exts = ('.txt', '.pdf', '.docx', '.zip', '.rar')  # Add more as needed
    ext = filepath.lower()
    if ext.endswith(image_exts):
        return "image"
    elif ext.endswith(file_exts):
        return "file"
    else:
        return None

def main():
    print(":: Steganography ::")
    print("1. Encode")
    print("2. Decode")
    choice = input("Choose (1/2): ").strip()
    filepath = input("Enter file path (with extension): ").strip()
    file_type = check_file_type(filepath)

    if not file_type:
        print("Unsupported or missing file. Please provide a supported image or document format.")
        return

    if choice == '1':
        msg = input("Enter message to hide: ")
        password = input("Enter password: ")
        out_file = None
        if file_type == "image":
            out_file = input("Enter output image file path (with extension): ").strip()
        else:
            out_file = input("Enter output file path: ").strip()
        result = encode_stego(filepath, msg, password, out_file=out_file)
        print(result)
    elif choice == '2':
        if file_type == "image":
            extracted = img_decode(filepath)
        else:
            extracted = file_decode(filepath)
        packed = base64.b64decode(extracted.encode('utf-8'))
        while True:
            password = input("Enter password: ")
            if not check_password(packed, password):
                print("Incorrect password. Try again.")
                continue
            try:
                msg = decrypt(packed, password)
                print("Decrypted message:", msg)
                break
            except Exception as e:
                print("Decryption failed:", e)
                break
    else:
        print("Invalid choice.")

def encode_stego(filepath, msg, password, out_file=None):
    """
    Encodes a message into an image or file using steganography.
    Args:
        filepath (str): Path to the cover file (image or document).
        msg (str): The message to hide.
        password (str): The password for encryption.
        out_file (str): Output file path (required).
    Returns:
        str: Success message or error message.
    """
    file_type = check_file_type(filepath)
    if not file_type:
        return "Unsupported or missing file. Please provide a supported image or document format."
    if not out_file:
        return "Output file path required."
    packed = encrypt(msg, password)
    data_to_hide = base64.b64encode(packed).decode('utf-8')
    try:
        if file_type == "image":
            returned_value = img_encode(filepath, data_to_hide, out_file)
            return returned_value
        else:
            file_encode(filepath, out_file, data_to_hide)
            return "Message encrypted and hidden in file."
    except Exception as e:
        return f"Error: {e}"

def decode_stego(filepath, password):
    """
    Decodes a hidden message from an image or file using steganography.
    Args:
        filepath (str): Path to the stego file (image or document).
        password (str): The password for decryption.
    Returns:
        str: Decoded message or error message.
    """
    file_type = check_file_type(filepath)
    if not file_type:
        return "Unsupported or missing file. Please provide a supported image or document format."
    try:
        if file_type == "image":
            extracted = img_decode(filepath)
        else:
            extracted = file_decode(filepath)
        packed = base64.b64decode(extracted.encode('utf-8'))
        if not check_password(packed, password):
            return "Incorrect password."
        try:
            msg = decrypt(packed, password)
            return msg
        except Exception as e:
            return f"Decryption failed"
    except Exception as e:
        return "Decryption failed"

if __name__ == "__main__":
    main()