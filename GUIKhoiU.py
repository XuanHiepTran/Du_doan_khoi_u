from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk
import pickle

tk = Tk()
tk.geometry("700x500")
tk.configure(bg="black")
tk.title("Dự đoán ung thư lành tính hay ác tính")


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
helpmenu.add_command(label='About')
with open('log_reg_pickle', 'rb') as f:
    mp= pickle.load(f)

label = Label(tk, text = "DỰ ĐOÁN UNG THƯ VÚ ", font=("Arial", 20,"bold", "italic"),width=40, fg="black",bg="#66CCFF", relief="groove", anchor=CENTER)
label.grid(row = 1, columnspan=3, pady=20, padx=5)
bgImage=ImageTk.PhotoImage(file="ut.jpg")
bgLabel =Label(tk,image=bgImage)
bgLabel.grid(rowspan=8, column=2)

label1 = Label(tk, text = "Clump thickness: ", fg = 'white',bg= 'black', font = ('Arial', 14))
label1.grid(row=2, column= 0, padx=5, pady=5, sticky=W)
tbclum = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
tbclum = ttk.Combobox(tk, values=tbclum, width=10, font = ('Arial', 14))
tbclum.grid(row=2, column=1, padx=5, pady=5)

label2 = Label(tk, text = "Uniformity of Cell Size: ", bg = 'black',fg = 'white', font = ('Arial', 14))
label2.grid(row=3, column= 0, padx=5, pady=5, sticky=W)
tbUSize = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
tbUSize = ttk.Combobox(tk, values=tbUSize, width=10, font = ('Arial', 14))
tbUSize.grid(row=3, column=1, padx=5, pady=5)

label3 = Label(tk, text = "Uniformity of Cell Shape: ", bg = 'black',fg = 'white', font = ('Arial', 14))
label3.grid(row=4, column= 0, padx=5, pady=5, sticky=W)
tbUShape = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
tbUShape = ttk.Combobox(tk, values=tbUShape, width=10, font = ('Arial', 14))
tbUShape.grid(row=4, column=1, padx=5, pady=5)

label4 = Label(tk, text = "Marginal Adhesion: ", bg = 'black', fg = 'white', font = ('Arial', 14))
label4.grid(row=5, column= 0, padx=5, pady=5, sticky=W)
tbMA = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
tbMA = ttk.Combobox(tk, values=tbMA, width=10, font = ('Arial', 14))
tbMA.grid(row=5, column=1, padx=5, pady=5)

label5 = Label(tk, text = "Single Epithelial Cell Size: ", bg = 'black',fg = 'white', font = ('Arial', 14))
label5.grid(row=6, column= 0,padx=5, pady=5, sticky=W)
tbSECS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
tbSECS = ttk.Combobox(tk, values=tbSECS, width=10, font = ('Arial', 14))
tbSECS.grid(row=6, column=1, padx=5, pady=5)

label6 = Label(tk, text = "Bare Nuclei: ", bg = 'black',fg = 'white', font = ('Arial', 14))
label6.grid(row=8, column= 0,padx=5, pady=5, sticky=W)
tbBN = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
tbBN = ttk.Combobox(tk, values=tbBN, width=10, font = ('Arial', 14))
tbBN.grid(row=8, column=1, padx=5, pady=5)

label7 = Label(tk, text = "Bland Chromatin: ", bg = 'black',fg = 'white', font = ('Arial', 14))
label7.grid(row=9, column= 0,padx=5, pady=5, sticky=W)
tbBC = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
tbBC = ttk.Combobox(tk, values=tbBC, width=10, font = ('Arial', 14))
tbBC.grid(row=9, column=1, padx=5, pady=5)

label7 = Label(tk, text = "Normal Nucleoli: ", bg = 'black',fg = 'white', font = ('Arial', 14))
label7.grid(row=10, column= 0,padx=5, pady=5, sticky=W)
tbNN = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
tbNN = ttk.Combobox(tk, values=tbNN, width=10, font = ('Arial', 14))
tbNN.grid(row=10, column=1, padx=5, pady=5)

label7 = Label(tk, text = "Mitoses: ", bg = 'black',fg = 'white', font = ('Arial', 14))
label7.grid(row=11, column= 0,padx=5, pady=5, sticky=W)
tbM = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
tbM = ttk.Combobox(tk, values=tbM, width=10, font = ('Arial', 14))
tbM.grid(row=11, column=1, padx=5, pady=5)
lb = Label(tk, text="Kết quả:",fg = 'black', font = ('Arial', 14),  bg= "yellow").grid(column=2, row=11)

def onClick():
    try:
        tbclum.get()
        tbUSize.get()
        tbUShape.get()
        tbMA.get()
        tbSECS.get()
        tbBN.get()
        tbBC.get()
        tbNN.get()
        tbM.get()
    except Exception as e:
        messagebox.showerror("Thông báo", "Nhập chưa đủ dữ liệu!")
        
    result = mp.predict([[tbclum.get(), tbUSize.get(),tbUShape.get(), tbMA.get(), tbSECS.get(), tbBN.get(), tbBC.get(), tbNN.get(), tbM.get()]])
    if result == 0:
        lb['text'] = 'Lành tính'
        lb['fg'] = 'Green'
    if result == 1:
        lb['text'] = 'Ác tính'
        lb['fg'] = 'red'
def clear():
    tbclum.delete(0, END)
    tbUSize.delete(0, END)
    tbUShape.delete(0, END)
    tbMA.delete(0, END)
    tbSECS.delete(0, END)
    tbBN.delete(0, END)
    tbBC.delete(0, END)
    tbNN.delete(0, END)
    tbM.delete(0, END)
btnClear = Button(tk, text = "Clear", font = ("Arial", 14, "bold"), bg = "gray", fg = "black", command= clear)
btnClear.grid(pady=10, row = 13, column=0)
framePredict= Frame(tk).grid()
btnShow = Button(tk, text = "Result", font = ("Arial", 14, "bold"), bg = "#42f5c5", fg = "black", command=onClick)
btnShow.grid(pady=10, row = 13, column=1)
lb = Label(tk,text = "", font = ('Arial', 18, "bold"),width= 10, height=1,bg= "white")
lb.grid(column=2, row=13)
tk.mainloop()