import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
import sklearn
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import  train_test_split
from sklearn import metrics as sq
import statsmodels.formula.api as smf

#import data
#link data: https://www.kaggle.com/shivachandel/kc-house-data
dataset = pd.read_csv('kc_house_data.csv')

dataset.head

x = dataset.drop("price", axis = 1)
y = dataset['price'].to_numpy()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 20)
reg = linear_model.LinearRegression()
reg.fit(x_train, y_train)

#Hệ số hồi quy
print("\nHệ số hồi quy: ")
print(pd.DataFrame({"Tên": x_train.columns, "Hệ số": np.abs(reg.coef_)}))

#Dự đoán y
Y_pred = reg.predict(x_test)
print("\nGIÁ TRỊ Y DỰ ĐOÁN")
print(Y_pred)
 
#Y thực tế: y_test
print("\nGIÁ TRỊ Y THỰC TẾ")
print(y_test)

#Độ chính xác:
R_squared_score = reg.score(x_test, y_test) *100
accuracy = ("{0:.2f}".format(R_squared_score))
print("\nMô hình có độ chính xác là " + accuracy + "%")

#Dự đoán 1 dữ liệu cụ thể
print("\nGiá nhà dự đoán được: ", reg.predict([[3,  1 , 1180 , 5650 , 1]]))

#Tạo form
tk = Tk()
tk.title("Dự đoán giá nhà")
tk.geometry("800x400")
from tkinter import messagebox
def onClick(): 
    try:
        SoPhongNgu= int(tbSoPhongNgu.get())
        Sophongtam = int(tbSoPhongTam.get())
        DTPhongKhach = float(tbDTPhongKhach.get())
        DTTongThe = float(tbDTTongThe.get())
        SoTang= int(tbSoTang.get())
    except Exception as e:
        messagebox.showerror("Thông báo", "Nhập lại!") 
    Label(tk, text=reg.predict([[tbSoPhongNgu.get(), tbSoPhongTam.get(), tbDTPhongKhach.get(), tbDTTongThe.get(), tbSoTang.get()]]), font=("Arial", 12, "bold"), fg= "blue"  ).grid(column=1, row= 9)
    

label = Label(tk, text = "DỰ ĐOÁN GIÁ NHÀ", font=("Arial", 20,"bold"), fg="red")
label.grid(pady=10, column= 1)
label1 = Label(tk, text = "Nhập vào các thông số nhà: ", font=("Arial", 18 ))
label1.grid(row=2, column= 1, padx=5, pady=5)

label2 = Label(tk, text = "Nhập số phòng ngủ: ", fg = 'black', font = ('Arial', 14))
label2.grid(row=3, column= 0, padx=5, pady=5)
tbSoPhongNgu = Entry(tk, fg='blue', font=('Arial', 14))
tbSoPhongNgu.grid(row = 3, column=1)

label2 = Label(tk, text = "Nhập số phòng tắm: ", fg = 'black', font = ('Arial', 14))
label2.grid(row=4, column= 0, padx=5, pady=5)
tbSoPhongTam = Entry(tk, fg='blue', font=('Arial', 14))
tbSoPhongTam.grid(row = 4, column=1)

label2 = Label(tk, text = "Nhập diện tích phòng khách: ", fg = 'black', font = ('Arial', 14))
label2.grid(row=5, column= 0, padx=5, pady=5)
tbDTPhongKhach = Entry(tk, fg='blue', font=('Arial', 14))
tbDTPhongKhach.grid(row = 5, column=1)

label2 = Label(tk, text = "Nhập diện tích tổng thể: ", fg = 'black', font = ('Arial', 14))
label2.grid(row=6, column= 0, padx=5, pady=5)
tbDTTongThe = Entry(tk, fg='blue', font=('Arial', 14))
tbDTTongThe.grid(row = 6, column=1)

label2 = Label(tk, text = "Nhập số tầng: ", fg = 'black', font = ('Arial', 14))
label2.grid(row=7, column= 0, padx=5, pady=5)
tbSoTang = Entry(tk, fg='blue', font=('Arial', 14))
tbSoTang.grid(row = 7, column=1)


framePredict= Frame(tk).grid()
btnShow = Button(tk, text = "Xem giá", font = ("Arial", 14, "bold"), bg = "#42f5c5", fg = "black",command= onClick)
btnShow.grid(pady=10, row = 8, column=1)

tk.mainloop()

#vẽ biểu đồ
model = smf.ols(formula='bathrooms ~ price + bedrooms', data=dataset)
results_formula = model.fit()
results_formula.params

x_surf, y_suft = np.meshgrid(np.linspace(dataset.price.min(), dataset.price.max(), 100),np.linspace(dataset.bedrooms.min(), dataset.bedrooms.max(), 100))
onlyX = pd.DataFrame({'price': x_surf.ravel(), 'bedrooms': y_suft.ravel()})
fittedY=results_formula.predict(exog=onlyX)
fittedY=np.array(fittedY)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(dataset['price'],dataset['bedrooms'],dataset['bathrooms'],c='red', marker='o', alpha=0.5)
ax.plot_surface(x_surf,y_suft,fittedY.reshape(x_surf.shape), color='b', alpha=0.3)
ax.set_xlabel('price')
ax.set_ylabel('bedrooms')
ax.set_zlabel('bathrooms')
ax.set_title('Price by bedrooms and bathrooms')
plt.show()
