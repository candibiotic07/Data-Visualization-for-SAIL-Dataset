#This python file is used for modelling ISOLATION FOREST algorithm for anomaly detection in HMD Parameters 
                            

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.ensemble import IsolationForest

df=pd.read_csv('ALL_HMD.csv')

df=df.drop(['Unnamed: 0'],axis=1)
# Convert 'time' column to datetime
df['time'] = pd.to_datetime(df['time'])

# df1=df.iloc[:,1:]
# df1=df.columns.difference(['time']) 
df1 = df.select_dtypes(include=[np.number])

# train isolation forest 
outliers_fraction = 0.01
model =  IsolationForest(contamination = outliers_fraction)
model.fit(df1)
# add the anomaly column to the main dataset  
df['anomaly25'] = pd.Series(model.predict(df1))
df['anomaly25'] = df['anomaly25'].map( {1: 0, -1: 1} )
print(df['anomaly25'].value_counts())

a=[]

#append anomalies time stamps into a list
def anomaly_timestamps(anomaly_feature,time_feature):
    z=anomaly_feature.to_numpy()
    indices=np.where(z==1)[0]
    anomaly_time=time_feature[indices]
    return indices,anomaly_time
    
indices,anomaly_time=anomaly_timestamps(df['anomaly25'],df['time'])
anomaly_time_arr=anomaly_time.to_numpy()
anomaly_df = pd.DataFrame({'Index':indices,'Time Stamp':anomaly_time_arr})
anomaly_df.to_csv('anomaly_HMD.csv')






