alienDictionary = {"chúng tôi": "vorag", "tới": "thang", "trong": "zon", "hòa bình": "argh", "xin chào": "kodar", "có thể": "znak", "tôi": "az", "mượn": "liftit", "một vài": "zum", "tên lửa": "upgoman", "nhiên lệu": "kakboom", "làm ơn": "selpin", "đừng": "baaaaaaaaaaaaaarn", "bắn": "flabil", "chào mừng": "unkip", "của chúng tôi": "mandig", "mới": "brang", "người ngoài hành tinh": "marangin", "xâm chiếm": "bap"}
vietnamesePhrase = input("Xin hãy điền một từu hoặc một cụm từ tiếng Việt cần dịch: ")
vietnameseWords = vietnamesePhrase.lower().split()
alienWords = []
for word in vietnameseWords:
    if word in alienDictionary:
        alienWords.append(alienDictionary[word])
    else:
        alienWords.append(word)
print("Tiếng ngoài hành tình gọi là", "".join(alienWords))            