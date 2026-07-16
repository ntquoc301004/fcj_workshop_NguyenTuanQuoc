def fix_encoding(text):
    try:
        # The text was read as cp1252 and then saved as utf-8.
        # So the current python string (which is read from the utf-8 file)
        # has characters that correspond to the cp1252 decoding of the original utf-8 bytes.
        # We can reverse it by encoding back to cp1252 to get the original bytes,
        # and then decoding as utf-8.
        original_bytes = text.encode('cp1252')
        return original_bytes.decode('utf-8')
    except Exception as e:
        print("Error:", e)
        return text

# Test
s = "Táº¡o User Pool"
print("Original:", s)
print("Fixed:", fix_encoding(s))
