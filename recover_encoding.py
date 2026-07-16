import os

files = [
    "content/5-Workshop/5.3-Lab2-Cognito-Auth/1-Create-UserPool/_index.vi.md",
    "content/5-Workshop/5.3-Lab2-Cognito-Auth/2-App-Integration/_index.vi.md",
    "content/5-Workshop/5.3-Lab2-Cognito-Auth/3-Test-Authentication/_index.vi.md",
]

def custom_encode(text):
    res = bytearray()
    for char in text:
        try:
            res.extend(char.encode('cp1252'))
        except UnicodeEncodeError:
            # If it's an undefined character in cp1252, PowerShell likely just kept its byte value
            # as a Unicode code point. For example, U+009D -> 0x9D
            res.append(ord(char))
    return bytes(res)

for path in files:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if content.startswith('\ufeff'):
            content = content[1:]
        
        try:
            original_bytes = custom_encode(content)
            restored = original_bytes.decode('utf-8')
            
            with open(path, 'w', encoding='utf-8', newline='\n') as f:
                f.write(restored)
            print(f"Fixed {path}")
        except Exception as e:
            print(f"Error on {path}: {e}")
