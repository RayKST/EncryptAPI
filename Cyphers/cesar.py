def cesar (text):
    key = 3
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cypherAlpha = ''

    for l in text.upper():
        index = alphabet.find(l) + key

        if index >= 26:
            index = index - 26

        cypherAlpha += alphabet[index]

    return cypherAlpha