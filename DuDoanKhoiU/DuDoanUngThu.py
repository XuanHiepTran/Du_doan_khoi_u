import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import  train_test_split
import pickle

#import data
#link data: https://www.kaggle.com/merishnasuwal/breast-cancer-prediction-dataset
dataset = pd.read_csv('Breast_cancer_data.csv')
dataset.head

null = dataset.isnull().sum()
print("Số giá trị null mỗi feature:")
print(null)

x = dataset.drop('diagnosis', axis = 1)
y = dataset.diagnosis.values

X_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.3)
log_reg = LogisticRegression(solver='lbfgs', max_iter=1000)
log_reg.fit(X_train, y_train)
print("\n\nx_train:\n")
print(X_train)
print("\n\ny_train\n")
print(y_train)

#Hệ số hồi quy
print("\nHệ số hồi quy: ")
print(pd.DataFrame(columns= X_train.columns, data= np.abs(log_reg.coef_)))

#Dự đoán Y
Y_pred = log_reg.predict(x_test)
print("\nGIÁ TRỊ Y DỰ ĐOÁN")
print(Y_pred)

#Y thực tế: y_test
print("\nGIÁ TRỊ Y THỰC TẾ")
print(y_test)

from sklearn.metrics import accuracy_score
#Độ chính xác của mô hình logistic
R_squared_score = accuracy_score(y_test,Y_pred) *100
accuracy = ("{0:.2f}".format(R_squared_score))
print("\nMô hình hồi quy logistic có độ chính xác là " + accuracy + "%")
print("\n")

#Độ chính xác khi dùng mô hình Naive Bayes
from sklearn.naive_bayes import MultinomialNB
clf_knn = MultinomialNB()
clf_knn.fit(X_train,y_train)
y_pred1 = clf_knn.predict(x_test)

R_squared_score = accuracy_score(y_test,y_pred1) *100
accuracy = ("{0:.2f}".format(R_squared_score))
print("\nĐộ chính xác của mô hình Naive Bayes: " + accuracy + "%")

#Độ chính xác khi dùng mô hình cây
from sklearn.tree import DecisionTreeClassifier
clf_dtc = DecisionTreeClassifier(criterion='entropy',random_state=7)
clf_dtc.fit(X_train,y_train)
y_pred3 = clf_dtc.predict(x_test)

R_squared_score = accuracy_score(y_test,y_pred3) *100
accuracy = ("{0:.2f}".format(R_squared_score))
print("\nĐộ chính xác của mô hình cây " + accuracy + "%")

#Mô hình rừng
from sklearn.ensemble import RandomForestClassifier
clf_rfc = RandomForestClassifier(random_state=1)
clf_rfc.fit(X_train, y_train)
y_pred4 = clf_rfc.predict(x_test)

R_squared_score = accuracy_score(y_test,y_pred4) *100
accuracy = ("{0:.2f}".format(R_squared_score))
print("\nĐộ chính xác của mô hình rừng " + accuracy + "%")
print('\n')

#Dự đoán 1 dự liệu cụ thể
pre = log_reg.predict([[17.99,  10.38 , 122.8 , 1001,0.1184]])
if pre ==0:
    print("Khối u đó là khối u ác tính")
if pre == 1:
    print("Khối u đó là khối u lành tính")

print("Tỉ lệ lành tính và ác tính của khối u là: ")
print (log_reg.predict_proba(np.array([[17.99,  10.38 , 122.8 , 1001,0.1184]])))
print("\n")

# Lưu file kết quả
with open('log_reg_pickle', 'wb') as f:
    mp= pickle.dump(log_reg, f)
f.close()
