# Encapsula: Steganography Toolkit

Encapsula is a user-friendly toolkit for hiding and extracting secret messages inside images and files.  

---

## ✨ Features

- **Hide messages** in images (PNG, JPEG, WEBP) and common document formats (TXT, PDF, DOCX, PPTX, XLSX, etc.)
- **AES encryption** for secure message protection with a password
- **Extract and decrypt** hidden messages with password verification
- **Modern TUI** built with [Textual](https://github.com/Textualize/textual) for an interactive experience
- **Cross-platform**: works on Linux, Windows, and macOS
- **Easy-to-use** file dialogs for selecting and saving files
- **Error handling** and user feedback throughout the process

---

## 🔒 How it works

- Your message is encrypted using AES and a password.
- The encrypted data is hidden in the least significant bits (LSB) of image pixels or file bytes.
- Only someone with the correct password can extract and decrypt the hidden message.

---

## 🚀 Getting Started

### 1. Clone this repository

```bash
https://github.com/safalgautam-ops/Encapsula
cd Encapsula
```

### 2. Install requirements

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
python TUI.py
```

---

## 🖥️ Usage

- **Encode:**  
  1. Select "Encode" from the main menu.
  2. Upload a cover file (image or supported document).
  3. Enter your secret message and password.
  4. Choose where to save the encoded file.
  5. Click "Done" to hide your message.

- **Decode:**  
  1. Select "Decode" from the main menu.
  2. Upload the stego file.
  3. Enter the password.
  4. Click "Show Now" to reveal the hidden message.

---

## 📂 Supported File Types

- Images: `.png`, `.jpg`, `.jpeg`, `.webp`
- Documents: `.txt`, `.pdf`, `.doc`, `.docx`, `.pptx`, `.xls`, `.xlsx`

---

## 🛠️ Project Structure

```
stego/
├── TUI.py           # Main Textual TUI application
├── main.py          # Backend logic for encoding/decoding
├── stegimg.py       # Image steganography functions
├── stegfiles.py     # File/document steganography functions
├── crypto.py        # AES encryption/decryption helpers
├── requirements.txt # Python dependencies
└── ...
```

---

## 🤝 Contributing

Pull requests and suggestions are welcome!  
Please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the MIT License.

---

**Developed by Safal Gautam**  
*github: [safalgautam-ops](https://github.com/safalgautam-ops)*
