import filetype
from stegimg import encode as img_encode, decode as img_decode
from stegfiles import encode_file as file_encode, decode_file as file_decode
from PIL import Image

def main():
    print(":: Steganography ::")
    print("1. Encode")
    print("2. Decode")
    choice = input("Choose (1/2): ").strip()

    filepath = input("Enter file path (with extension): ").strip()
    ext = filepath.rsplit('.', 1)[-1].lower()
    kind = filetype.guess(filepath)

    image_exts = ('png', 'jpeg', 'jpg', 'bmp', 'webp')
    file_exts = ('pdf', 'doc', 'docx', 'txt')

    if (kind and kind.extension in image_exts) or ext in image_exts:
        # Image file
        if choice == '1':
            img_encode(filepath)
        elif choice == '2':
            print(img_decode(filepath))
        else:
            print("Invalid choice.")
    elif ext in file_exts:
        # Document/file
        if choice == '1':
            out_file = input("Enter output file path: ").strip()
            msg = input("Enter message to hide: ")
            file_encode(filepath, out_file, msg)
        elif choice == '2':
            file_decode(filepath)
        else:
            print("Invalid choice.")
    else:
        print("Unsupported file type. Supported: png, jpeg, pdf, doc, docx, txt.")

if __name__ == "__main__":
    main()