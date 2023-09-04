import pandas as pd
from datetime import datetime, timedelta

# Read the CSV file
df = pd.read_csv('anomaly_HMD.csv')

# Convert the timestamps to datetime objects
df['Time Stamp'] = pd.to_datetime(df['Time Stamp'])

# Create an empty list to store the time intervals
time_intervals = []

# Iterate over the 24 hours of the day
for hour in range(24):
    # Create a mask to select the timestamps within the current hour
    mask = (df['Time Stamp'].dt.hour == hour)
    
    # Select the timestamps within the current hour
    hour_timestamps = df.loc[mask, 'Time Stamp']
    
    # Check if there are any timestamps within the current hour
    if not hour_timestamps.empty:
        # Sort the timestamps in ascending order
        hour_timestamps = hour_timestamps.sort_values()
        
        # Initialize the start and end of the first time interval
        start = hour_timestamps.iloc[0]
        end = start
        
        # Iterate over the remaining timestamps
        for timestamp in hour_timestamps.iloc[1:]:
            # Check if the current timestamp is within 5 minutes of the end of the current time interval
            if (timestamp - end) <= timedelta(minutes=5):
                # Update the end of the current time interval
                end = timestamp
            else:
                # Create a time interval from the start and end of the current time interval
                time_interval = (start, end)
                
                # Add the time interval to the list of time intervals
                time_intervals.append(time_interval)
                
                # Start a new time interval
                start = timestamp
                end = start
        
        # Create a time interval from the start and end of the last time interval
        time_interval = (start, end)
        
        # Add the time interval to the list of time intervals
        time_intervals.append(time_interval)
print(len(time_intervals))
# Print the time intervals
for time_interval in time_intervals:
    print(f'{time_interval[0]} - {time_interval[1]}')