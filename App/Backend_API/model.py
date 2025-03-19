import pandas as pd
import numpy as np
import seaborn as sns
import pickle

#laoding dataset

df = pd.read_csv("Final_dataset_8_div.csv")

print(df.head())

#Breaking NightTime Data
after_midnight_data= df[df['hour']<7]
till_midnight_data= df[df['hour']>19]

#Dropping NightTime Data

df = df.drop(after_midnight_data.index,axis= 0)

df = df.drop(till_midnight_data.index,axis= 0)

#Defining X and Y

x= df.drop(['year','month','day','hour','wbgt'],axis=1).values
y=df['wbgt'].values

#Splitting Dataset into test and validation set

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
x_train_temp, x_val, y_train_temp, y_val = train_test_split(x_train, y_train , test_size=0.1, random_state=0)
x_val.shape

#Calling Linear Regression

from sklearn.linear_model import LinearRegression
reg= LinearRegression()
reg.fit(x_train_temp,y_train_temp)

#Getting the prediction
y_pred= reg.predict(x_test)

#Making Pickle File of the model
pickle.dump(reg, open("model.pkl", "wb"))


