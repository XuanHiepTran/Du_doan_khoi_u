from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk
import pickle

tk = Tk()
tk.geometry("700x500")
tk.configure(bg="black")
tk.title("Dự đoán ung thư lành tính hay ác tính")
def Click():
    tk1 = Tk()
    tk1.geometry("710x500")

    tk1.configure(bg="gray")
    tk1.iconbitmap(r'favicon.ico')
    tk1.title("About")
    label9 = Label(tk1, text="THÔNG TIN VỀ CÁC FEATURE", font = ("Arial", 15, "bold"), bg = "#FFFF66", fg = "black")
    label9.grid( padx=10, pady=10)
    label0 = Label(tk1, text="1. Mean_radius: bán kính của khối u (đơn vị: µm)", font = ("Arial", 15, "bold"), fg = "black")
    label0.grid(sticky=W, padx=10, pady=10)
    label1 = Label(tk1, text="2. Mean_texture: độ lệch chuẩn của các giá trị thang xám", font = ("Arial", 15, "bold"), fg = "black")
    label1.grid(sticky=W, padx=10, pady=10)
    label2 = Label(tk1, text="3. Mean_perimeter: Chu vi của khối u (đơn vị: µm)", font = ("Arial", 15, "bold"), fg = "black")
    label2.grid(sticky=W, padx=10, pady=10)
    label3 = Label(tk1, text="4. Mean_area: Diện tích của khối u (đơn vị: 〖µm〗^2)", font = ("Arial", 15, "bold"), fg = "black")
    label3.grid(sticky=W, padx=10, pady=10)
    label4 = Label(tk1, text="5. Mean_smoothness:Tỉ lệ thay đổi về bán kính của khối u", font = ("Arial", 15, "bold"), fg = "black")
    label4.grid(sticky=W, padx=10, pady=10)

menu = Menu(tk, activebackground='gray')
tk.config(menu=menu)
filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Home')
filemenu.add_separator()
filemenu.add_command(label='New')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=tk.quit)
helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About', command=Click)
with open('log_reg_pickle', 'rb') as f:
    mp= pickle.load(f)

label = Label(tk, text = "DỰ ĐOÁN UNG THƯ VÚ ", font=("Arial", 20,"bold", "italic"),width=40, fg="black",bg="#66CCFF", relief="groove", anchor=CENTER)
label.grid(row = 1, columnspan=3, pady=20, padx=5)
bgImage=ImageTk.PhotoImage(file="ut.jpg")
bgLabel =Label(tk,image=bgImage)
bgLabel.grid(rowspan=8, column=2)

label1 = Label(tk, text = "Mean_radius: ", fg = 'white',bg= 'black', font = ('Arial', 14))
label1.grid(row=2, column= 0, padx=5, pady=5, sticky=W)
tbRadius = Entry(tk,width=12, fg='blue', font=('Arial', 14))
tbRadius.grid(row=2, column=1, padx=10, pady=10)

label2 = Label(tk, text = "Mean_texture: ", bg = 'black',fg = 'white', font = ('Arial', 14))
label2.grid(row=3, column= 0, padx=5, pady=5, sticky=W)
tbTexture = Entry(tk,width=12, fg='blue', font=('Arial', 14))
tbTexture.grid(row=3, column=1, padx=10, pady=10)

label3 = Label(tk, text = "Mean_perimeter: ", bg = 'black',fg = 'white', font = ('Arial', 14))
label3.grid(row=4, column= 0, padx=5, pady=5, sticky=W)
tbPerimeter =  Entry(tk,width=12, fg='blue', font=('Arial', 14))
tbPerimeter.grid(row=4, column=1, padx=10, pady=10)

label4 = Label(tk, text = "Mean_area: ", bg = 'black', fg = 'white', font = ('Arial', 14))
label4.grid(row=5, column= 0, padx=5, pady=5, sticky=W)
tbArea = Entry(tk,width=12, fg='blue', font=('Arial', 14))
tbArea.grid(row=5, column=1, padx=10, pady=10)

label5 = Label(tk, text = "Mean_smoothness: ", bg = 'black',fg = 'white', font = ('Arial', 14))
label5.grid(row=6, column= 0,padx=5, pady=5, sticky=W)
tbSmoothness = Entry(tk,width=12, fg='blue', font=('Arial', 14))
tbSmoothness.grid(row=6, column=1, padx=10, pady=10)

def onClick():
    try:
        Radius=float(tbRadius.get())
        Texture = float(tbTexture.get())
        Perimeter = float(tbPerimeter.get())
        Area = float(tbArea.get())
        Smoothness= float(tbSmoothness.get())
    except Exception as e:
        messagebox.showerror("Thông báo", "Nhập chưa đủ dữ liệu!")
        
    result = mp.predict([[Radius, Texture, Perimeter, Area, Smoothness]])
    if result == 0:
        lb['text'] = 'Lành tính'
        lb['fg'] = 'Green'
    if result == 1:
        lb['text'] = 'Ác tính'
        lb['fg'] = 'red'
def clear():
    tbRadius.delete(0, END)
    tbTexture.delete(0, END)
    tbPerimeter.delete(0, END)
    tbArea.delete(0, END)
    tbSmoothness.delete(0, END)
    
btnClear = Button(tk, text = "Clear", font = ("Arial", 14, "bold"), bg = "gray", fg = "black", command= clear)
btnClear.grid(pady=50, row = 13, column=0)
framePredict= Frame(tk).grid()
btnShow = Button(tk, text = "Result", font = ("Arial", 14, "bold"), bg = "#42f5c5", fg = "black", command=onClick)
btnShow.grid(pady=50, row = 13, column=1)
lb = Label(tk,text = "", font = ('Arial', 18, "bold"),width= 10, height=1,bg= "white")
lb.grid(column=2, row=13)
tk.mainloop()