woman = ["Một nhà khoa học", "Một nữ hoàng", "Một tên cướp biển", "Một con thỏ khổng lổ"]
man = ["một sĩ quan cảnh sát", "một nghệ sĩ", "ông của bạn", "một rô bốt sát thủ"]
place = ["trên Sao Diêm Vương", "ở siêu thị", "trong một cái hang tối tăm ma quái đầy dơi."]
sheWore = ["bộ đồ lặn biển", "cánh tiên", "một cái túi giấy"]
heWore = ["đồ vest tím", "đồ hóa trang cá mập", "khăn tắm đi biển."]
womanSays = ["Anh là ai?", "Bao nhiêu hạt đậu thì bằng năm", "Tại sao?"]
manSays = ["Bíp bóp!", "Đừng ăn ếch!", "'Mấy giờ cô sẽ gọi cái này?'"]
consequence = ["hào bình thế giới", "hỗn loạn", "một bàn chân khổng lồ nghiền nát họ?"]
worldSaid = ["'Vô nghĩa vớ vẩn!'", "'Phô mai là nhất.'", "'Tôi đang tan chảy!'"]
import random
while True:
    print(random.choice(woman), "gặp", random.choice(man), random.choice(place))
    print("Cô ấy đang mặc", random.choice(sheWore))
    print("Anh ấy đang mặc", random.choice(heWore))
    print("Cô ấy nới,", random.choice(womanSays))
    print("Anh ấy nói,", random.choice(manSays))
    print("Điều đó dẫn đến", random.choice(consequence))
    print("Thế giới nói,", random.choice(worldSaid))
    print()
    input("Ấn Enter để chơi lại.")
    print()
    break