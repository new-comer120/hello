import random

number = random.randint(1,20)
guess = int(input("Tờ đang nghĩ tới một số trong khoảng từ 1 đến 20. Đó là số nào?"))
while guess != number:
    if guess < number:
        print("Số của bạn quá nhỏ...")
    else:
        print("Số của bạn quá lớn...")
    guess = int(input("Xin hãy đoán lại..."))
print("Xin chúc mừng! Bạn đã đoán đúng!")        