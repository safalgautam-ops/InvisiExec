def genData(data):
    """Yield 8-bit binary strings for each character in the message."""
    for char in data:
        yield format(ord(char), '08b')

def modBytes(file_bytes, data):
    """
    Generator that yields bytes with message bits hidden in their LSBs.
    Adds 8 zero bits as a delimiter at the end.
    """
    data_bits = ''.join(genData(data)) + '00000000'
    for i, byte in enumerate(file_bytes):
        if i < len(data_bits):
            bit = data_bits[i]
            yield (byte & ~1) | int(bit)
        else:
            yield byte

def encode_file(input_file, output_file, message):
    with open(input_file, 'rb') as f:
        file_bytes = f.read() 
    if len(message) * 8 + 8 > len(file_bytes):
        raise ValueError("File too small to hide the message.")
    modded_bytes = bytearray(modBytes(file_bytes, message))
    with open(output_file, 'wb') as f:
        f.write(modded_bytes)
    print(f"Message hidden in {output_file}")

def decode_file(stego_file):
    with open(stego_file, 'rb') as f:
        file_bytes = f.read()
    bits = (str(byte & 1) for byte in file_bytes)
    chars = []
    while True:
        byte_str = ''.join(next(bits) for _ in range(8))
        if byte_str == '00000000':
            break
        chars.append(chr(int(byte_str, 2)))
    message = ''.join(chars)
    print("Extracted message:", message)
    return message

