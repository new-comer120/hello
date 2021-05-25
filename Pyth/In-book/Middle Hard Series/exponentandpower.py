aliens = 2
password = "ALIENS"
print("Nhanh lên! Người ngoài hành tinh đang xâm chiếm đấy!")
print("Bạn cần bật hệ thông phòng vệ toàn cầu lên ngay!")
print("Hy vọng bạn biết mật khẩu, vì tương lai Trái Đất...")
print()
print("------------------------------------------------------------")
print("     CHÀO MỪNG TỚI HỆ THỐNG PHÒNG VỆ TOÀN CẦU     ")
print("------------------------------------------------------------")
print()
guess = input("Xin hãy điền mật khẩu:").upper()
while guess != password:
    print()
    print("Mật khẩu sai.")
    print()
    aliens = aliens ** 2
    print("Có", aliens, "người ngoài hành tinh xâm nhập Trái Đất. Hãy thử lại!")
    if aliens > 7400000000:
        break
    print()
    print("Gợi ý mật khẩu: thứ đang tấn công chúng ta.(tiếng anh số nhiều)")
    print()
    guess = input("Nhanh nào! Hãy nhập mật khẩu:").upper()
if aliens > 7400000000:
    print("Khôngggggggggg! Người ngoài hành tinh đông hơn hẳn chúng ta. Chúng ta thua rồi!")
else:
    print("Hoan hô! Chúng ta đã chiến thắng, thế giới được cứu rồi!")