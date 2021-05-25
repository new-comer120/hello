alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
stringToEncrypt = input("Xin hãy nhập thông điệp cần mã khóa:")
stringToEncrypt = stringToEncrypt.upper()
shiftAmount = int(input("Xin hãy nhập một số từ 1 đến 25 để làm mã khóa."))
encryptedString = ""
for currentCharacter in stringToEncrypt:
    position = alphabet.find(currentCharacter)
    newPosition = position + shiftAmount
    if currentCharacter in alphabet:
        encryptedString = encryptedString + alphabet[newPosition]
    else:
        encryptedString = encryptedString + currentCharacter    
print("Thông điệp mã hóa của bạn là", encryptedString)    