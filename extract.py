def extract_from_zero_width(zero_width_text):
    extracted_text = ""
    binary_char = ""
    for char in zero_width_text:
        if char == "\u200C" or char == "\u200B":
            binary_char += "1" if char == "\u200C" else "0"
            if len(binary_char) == 16:
                extracted_text += chr(int(binary_char, 2))
                binary_char = ""
    return extracted_text


with open("modified.txt", "r", encoding="utf-8") as file:
    zero_width_text = file.read()
extracted_text = extract_from_zero_width(zero_width_text)
print("Extracted Text:", extracted_text)
