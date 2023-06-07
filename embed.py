def convert_to_zero_width(text):
    zero_width_text = ""
    for char in text:
        zero_width_char = ""
        binary_char = bin(ord(char))[2:].zfill(16)
        for bit in binary_char:
            zero_width_char += "\u200C" if bit == "1" else "\u200B"
        zero_width_text += zero_width_char
    return zero_width_text


original_text = "This is a secret message!"
print("Original Text:", original_text)
zero_width_text = convert_to_zero_width(original_text)
with open("modified.txt", "w", encoding="utf-8") as file:
    file.write(zero_width_text)
print("Zero-Width Text saved to 'zero_width_text.txt' file.")
