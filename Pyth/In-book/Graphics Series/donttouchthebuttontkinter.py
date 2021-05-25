import tkinter
window = tkinter.Tk()
button = tkinter.Button(window, text="Đừng bấm nút này.", width=40)
button.pack(padx=10, pady=10)
clickCount = 0
def onClick(event):
    global clickCount
    clickCount = clickCount + 1
    if clickCount == 1:
        button.configure(text="Thật hả? Đã bảo đùng bấm nút rồi mà!")
    elif clickCount == 2:
        button.configure(text="Hừm! Không nút niếc gì nữa!")
    else:
        button.pack_forget()
button.bind("<ButtonRelease-1>", onClick)    
window.mainloop()