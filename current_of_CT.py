from math import sqrt
from data_reader import outReader
import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import tensorflow as tf
from keras import Sequential
from keras.layers import LSTM,Dense
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler


reader = outReader()
df_origin = reader.read()
df_result = df_origin.copy()
# print(df_result)

"""yichang to nan"""
df_result.loc[df_result[4] == 1] = [np.nan,np.nan,np.nan,1]
# print(df_result.loc[df_result[4] == 1])

"""nan to mean"""
label = df_result[4]
df_result = df_result.iloc[:,:3]
df_result_re = df_result.fillna(df_result.mean()[:3])
# print(df_result.fillna(df_result.mean()[:3]).loc[df_result['y_pred'] == 1])


values = df_result_re.values
"""ensure all data is float"""
values = values.astype('float32')
"""normalize features"""
scaler = MinMaxScaler(feature_range=(0, 1))
scaled = scaler.fit_transform(values)


current_X = scaled[:-1,:3]
# reshape input to be 3D(samples,timesteps,features)
current_X = current_X.reshape(current_X.shape[0],1,current_X.shape[1])


#download model
model = load_model('cache_data/out/currentlstm.h5')

# plt.figure(figsize=(24,12))
current_predict = model.predict(current_X)
# plt.plot(scaled[:,0], c='b')
# plt.plot([x for x in current_predict], c='r')
# plt.show()

# 归一化反转
from math import sqrt
from numpy import concatenate
from sklearn.metrics import mean_squared_error
# make a prediction
yhat = current_predict
test_X = scaled[:-1,:2]

# invert scaling for forecast
inv_yhat = concatenate((yhat,test_X), axis=1)
inv_yhat = scaler.inverse_transform(inv_yhat)
inv_yhat = inv_yhat[:,0]

inv_yhat = np.insert(inv_yhat,0,values[0,0])

# current8111Ba_hat = pd.DataFrame(inv_yhat)
# current8111Ba_hat.to_excel("cache_data/out/current8111B-A.xlsx")
# print(type(current8111Ba_hat))



"""set label"""
data8111B_A = pd.DataFrame(label)
data8111B_A['A'] = df_origin[1].values
data8111B_A.to_excel("cache_data/out/current8111B-A.xlsx")

# 原数据与标准化预测值对比图
# plt.plot(df_result.iloc[1:, 0].values, c='b')
# # plt.plot(values[:-1,0], c='b')
# # plt.plot([None for _ in df_result.iloc[:450, 0].values] + [x for x in inv_yhat[450:]], c='r')
# plt.plot(inv_yhat[:], c='r')
# plt.show()


# calculate RMSE
rmse = sqrt(mean_squared_error(values[:,0], inv_yhat[:]))
print('RMSE: %.3f' % rmse)



