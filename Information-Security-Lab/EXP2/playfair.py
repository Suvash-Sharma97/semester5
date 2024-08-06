key = 'Kathmandu'
plain_text = 'A quick brown fox jumps over little lazy dog'

def create_grid(key):
    '''Function to create the 5x5 playfair grid'''
    key = key.lower()
    grid = []
    alphabets = list(chr(x) for x in range(97, 123) if x != 'j')

    total_unique_letters = []

    for each_letter in key:
        if each_letter == 'j' or each_letter == 'i':
            if 'i' not in total_unique_letters:
                total_unique_letters.append('i')
        elif each_letter not in total_unique_letters and each_letter != ' ':        
            total_unique_letters.append(each_letter)

    for each_letter in alphabets:
        if each_letter not in total_unique_letters:
            total_unique_letters.append(each_letter)

    counter = 0
    size = 5
    while counter + size <= len(total_unique_letters):
        temp = total_unique_letters[counter:counter + size]
        counter += size
        grid.append(temp)

    return grid

def create_pair(plain_text):
    '''Function to form pairs of two letters in the plain text'''
    pairs = []
    letters = list(x for x in plain_text.lower() if x != ' ')
    i = 0
    
    while i < len(letters):
        if i == len(letters) - 1:  # If there's only one character left
            pairs.append([letters[i], 'x'])
            i += 1
        elif letters[i] != letters[i + 1]:
            pairs.append([letters[i], letters[i + 1]])
            i += 2
        else:
            pairs.append([letters[i], 'x'])
            i += 1

    return pairs

def find_position(letter, grid):
    '''Function to find the position of a letter in the grid'''
    for i in range(5):
        for j in range(5):
            if grid[i][j] == letter:
                return i, j
    return -1, -1

def encrypt(pairs, grid):
    '''Function to encrypt pairs using the Playfair cipher'''
    cipher_text = []

    for pair in pairs:
        r1, c1 = find_position(pair[0], grid)
        r2, c2 = find_position(pair[1], grid)
        
        if r1 == r2:  # Same row
            cipher_text.append(grid[r1][(c1 + 1) % 5])
            cipher_text.append(grid[r2][(c2 + 1) % 5])
        elif c1 == c2:  # Same column
            cipher_text.append(grid[(r1 + 1) % 5][c1])
            cipher_text.append(grid[(r2 + 1) % 5][c2])
        else:  # Rectangle
            cipher_text.append(grid[r1][c2])
            cipher_text.append(grid[r2][c1])

    return ''.join(cipher_text)

def decrypt(cipher_text, grid):
    '''Function to decrypt the cipher text using the Playfair cipher'''
    pairs = [list(cipher_text[i:i+2]) for i in range(0, len(cipher_text), 2)]
    plain_text = []

    for pair in pairs:
        r1, c1 = find_position(pair[0], grid)
        r2, c2 = find_position(pair[1], grid)
        
        if r1 == r2:  # Same row
            plain_text.append(grid[r1][(c1 - 1) % 5])
            plain_text.append(grid[r2][(c2 - 1) % 5])
        elif c1 == c2:  # Same column
            plain_text.append(grid[(r1 - 1) % 5][c1])
            plain_text.append(grid[(r2 - 1) % 5][c2])
        else:  # Rectangle
            plain_text.append(grid[r1][c2])
            plain_text.append(grid[r2][c1])

    return ''.join(plain_text)

def main():
    grid = create_grid(key)
    pairs = create_pair(plain_text)
    cipher_text = encrypt(pairs, grid)

    print("Cipher Text:")
    print(cipher_text)

    decrypted_text = decrypt(cipher_text, grid)
    print("\nDecrypted Text:")
    print(decrypted_text)
    
if __name__ == '__main__':
    main()
