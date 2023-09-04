import pandas as pd
import matplotlib.pyplot as plt
import os
import re





df = pd.read_csv('concatentaion_HMD_3hours_21_04_32-23_59_32.csv')

# Setting datetime as index
df = df.drop('Unnamed: 0', axis=1)
df["time"] = pd.to_datetime(df["time"])
df = df.set_index('time')


# #plotting all features w.r.t. Time in a single image
# df.plot(subplots=True)
# plt.savefig('24.png')
# plt.show()



# Create a directory to save plots
os.makedirs('plots_HMD_21-24', exist_ok=True)

# COUNT PLOTS
# Loop through each attribute (column) in the DataFrame
for column in df.columns:
    # Sanitize the column name for use in filenames
    sanitized_column = re.sub(r'\W+', '_', column)  # Replace non-alphanumeric characters with underscores
    
    # plt.figure(figsize=(10, 6))  # Adjust figure size if needed
    df[column].value_counts().plot(kind='bar')
    
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.title(f'Count Plot for {column}')
    
    plt.tight_layout()
    plt.savefig(os.path.join('plots_HMD_21-24', f'{sanitized_column}_count_plot.png'))
    # plt.show()
    
    plt.close()



# # TIME SERIES PLOTS
for column in df.columns[1:]:
    sanitized_column = re.sub(r'\W+', '_', column)
    
    plt.plot(df[column])
    plt.title(f'Time Series Plot for {column}')
    
    plt.savefig(os.path.join('plots_HMD_21-24', f'{sanitized_column}_time_series_plot.png'))
    # plt.show()
    
    plt.close()
