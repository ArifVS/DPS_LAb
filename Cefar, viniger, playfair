def encrypt(te,s):
  result = ""
  # traverse text
  for i in range(len(text)):
    char = text[i]
    # Encrypt uppercase characters
    if (char.isupper()):
      result += chr((ord(char) + s-65) % 26 + 65)
    # Encrypt lowercase characters
    else:
      result += chr((ord(char) + s - 97) % 26 + 97)
  return result
#check the above function
text = "WELCoMe"
s = 4
print("Text   : " + text)
print("Shift  : " + str(s))
print("Cipher : " + encrypt(text,s))

-------------------------------------------------------------------------------------------------

def vigenere_encrypt(text, key):
    result = ""
    key = key * (len(text) // len(key) + 1)  # Extend key
    for i in range(len(text)):
        if text[i].isalpha():
            shift = ord(key[i].lower()) - ord('a')
            if text[i].isupper():
                result += chr((ord(text[i]) + shift - ord('A')) % 26 + ord('A'))
            else:
                result += chr((ord(text[i]) + shift - ord('a')) % 26 + ord('a'))
        else:
            result += text[i]
    return result

def vigenere_decrypt(text, key):
    result = ""
    key = key * (len(text) // len(key) + 1)  # Extend key
    for i in range(len(text)):
        if text[i].isalpha():
            shift = ord(key[i].lower()) - ord('a')
            if text[i].isupper():
                result += chr((ord(text[i]) - shift - ord('A') + 26) % 26 + ord('A'))
            else:
                result += chr((ord(text[i]) - shift - ord('a') + 26) % 26 + ord('a'))
        else:
            result += text[i]
    return result

# Example usage
text = "Hello, World!"
key = "KEY"
encrypted = vigenere_encrypt(text, key)
print(f"Encrypted: {encrypted}")
decrypted = vigenere_decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")

-------------------------------------------------------------------------------------------------

def make_matrix(key):
    key = key.upper().replace('J', 'I')
    matrix = []
    seen = set()
    
    # Add key letters
    for char in key:
        if char.isalpha() and char not in seen:
            matrix.append(char)
            seen.add(char)
    
    # Add remaining alphabet
    for char in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if char not in seen:
            matrix.append(char)
            seen.add(char)
    
    # Convert to 5x5 matrix
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def playfair(text, key, encrypt=True):
    matrix = make_matrix(key)
    text = text.upper().replace('J', 'I')
    
    # Prepare digraphs
    digraphs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'
        if a == b:  # Same letters, insert X
            digraphs.append(a + 'X')
            i += 1
        else:
            digraphs.append(a + b)
            i += 2
    
    result = []
    for a, b in digraphs:
        # Find positions
        r1, c1, r2, c2 = None, None, None, None
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == a:
                    r1, c1 = i, j
                if matrix[i][j] == b:
                    r2, c2 = i, j
        
        # Apply rules
        shift = 1 if encrypt else -1
        if r1 == r2:  # Same row
            c1 = (c1 + shift) % 5
            c2 = (c2 + shift) % 5
        elif c1 == c2:  # Same column
            r1 = (r1 + shift) % 5
            r2 = (r2 + shift) % 5
        else:  # Rectangle
            c1, c2 = c2, c1
        
        result.append(matrix[r1][c1] + matrix[r2][c2])
    
    return ''.join(result)

# Example usage
if __name__ == "__main__":
    key = "ICLOUDEMS"
    plaintext = "vardhaman"
    
    encrypted = playfair(plaintext, key, encrypt=True)
    print(f"Encrypted: {encrypted}")
    
    decrypted = playfair(encrypted, key, encrypt=False)
    print(f"Decrypted: {decrypted}")

