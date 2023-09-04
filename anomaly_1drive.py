import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.covariance import EllipticEnvelope
from sklearn.svm import OneClassSVM
from sklearn.ensemble import IsolationForest

# Load the CSV file
df = pd.read_csv('ALL_1DRIVE.csv')

# Drop unnecessary columns
df = df.drop(['Unnamed: 0', '1D_D_OK(NC contact)', '1D_DCCB_ON', '1D_RUN(NC contact)', '1D_TRIP'], axis=1)

# Convert 'time' column to datetime
df['time'] = pd.to_datetime(df['time'])

# Select only the numerical columns you want to scale
numerical_columns = df.columns.difference(['time'])  # Exclude the 'time' column

# Initialize the StandardScaler
min_max_scaler = preprocessing.StandardScaler()

# Apply StandardScaler to the selected columns
df[numerical_columns] = min_max_scaler.fit_transform(df[numerical_columns])

# Now df contains the scaled values for the selected numerical columns

# Continue with the rest of your code
outliers_fraction = 0.01
model = IsolationForest(contamination=outliers_fraction)
model.fit(df[numerical_columns])

df['anomaly25'] = pd.Series(model.predict(df[numerical_columns]))
df['anomaly25'] = df['anomaly25'].map({1: 0, -1: 1})
print(df['anomaly25'].value_counts())

# Define an empty list
a = []

# Append anomalies time stamps into a list
def anomaly_timestamps(anomaly_feature, time_feature):
    z = anomaly_feature.to_numpy()
    indices = np.where(z == 1)[0]
    anomaly_time = time_feature[indices]
    return indices, anomaly_time

indices, anomaly_time = anomaly_timestamps(df['anomaly25'], df['time'])
anomaly_time_arr = anomaly_time.to_numpy()
anomaly_df = pd.DataFrame({'Index': indices, 'Time Stamp': anomaly_time_arr})
anomaly_df.to_csv('anomaly.csv')
