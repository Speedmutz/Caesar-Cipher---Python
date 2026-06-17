def myalphabet():

    alphabet = {
        "A":0, "B":1, "C":2, "D":3, "E":4,
        "F":5, "G":6, "H":7, "I":8, "J":9,
        "K":10, "L":11, "M":12, "N":13,
        "O":14, "P":15, "Q":16, "R":17,
        "S":18, "T":19, "U":20, "V":21,
        "W":22, "X":23, "Y":24, "Z":25
    }

    print("Welcome to the encryption, decryption point")
    print("======MENU======")

    Y = int(input("Select which mode you desire and choose the corresponding no. \n a. Encryption ........ 1\n b. Decryption ........ 2\n Place your response here: "))

    if Y == 1:
        encrypt = str(input("Enter the word you want to encrypt: ")).upper()
        shift = int(input("Enter shift value: "))

        encrypted_word = ""

        for letter in encrypt:
            number = alphabet[letter]
            new_number = (number + shift) % 26

            for key, value in alphabet.items():
                if value == new_number:
                    encrypted_word += key

        print("Encrypted word:", encrypted_word)

    elif Y == 2:
        decrypt = str(input("Enter the word you want to decrypt: ")).upper()
        shift = int(input("Enter shift value: "))

        decrypted_word = ""

        for letter in decrypt:
            number = alphabet[letter]
            new_number = (number - shift) % 26

            for key, value in alphabet.items():
                if value == new_number:
                    decrypted_word += key

        print("Decrypted word:", decrypted_word)

    else:
        print("Invalid choice")

myalphabet()