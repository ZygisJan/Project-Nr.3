import pandas as pd

# Step 1: Import the dataset from this address
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/Wind_Stats/wind.data'
data = pd.read_csv(url, sep=r'\s+')

# Step 2: Assign it to a variable called data and replace the first 3 columns by a proper datetime index
data['Yr'] = data['Yr'].apply(lambda x: x + 1900 if x < 100 else x)  # Pakeisti metus teisingai
data['Yr_Mo_Dy'] = pd.to_datetime(data['Yr'].astype(str) + '-' + data['Mo'].astype(str) + '-' + data['Dy'].astype(str))
data = data.set_index('Yr_Mo_Dy')
data = data.drop(columns=['Yr', 'Mo', 'Dy'])
print("Data overview with datetime index:")
print(data.head())

# Step 3: Compute how many values are missing for each location over the entire record
missing_values = data.isna().sum()
print("\nMissing values for each location:")
print(missing_values)

# Step 4: Compute how many non-missing values there are in total
non_missing_values = data.notna().sum().sum()
print("\nTotal number of non-missing values:")
print(non_missing_values)

# Step 5: Calculate the mean windspeeds of the windspeeds over all the locations and all the times
mean_windspeed = data.mean().mean()
print("\nMean windspeed over all locations and all times:")
print(mean_windspeed)

# Step 6: Create a DataFrame called loc_stats and calculate the min, max, mean, and standard deviation of the windspeeds at each location over all the days
loc_stats = data.describe().T[['mean', 'std', 'min', 'max']]
print("\nStatistics (min, max, mean, std) of the windspeeds at each location:")
print(loc_stats)

# Step 7: Create a DataFrame called day_stats and calculate the min, max, mean, and standard deviation of the windspeeds across all the locations at each day
day_stats = data.aggregate(['min', 'max', 'mean', 'std'], axis=1)
print("\nStatistics (min, max, mean, std) of the windspeeds across all locations at each day:")
print(day_stats.head())

# Step 8: Find the average windspeed in January for each location
january_data = data[data.index.month == 1]
january_avg = january_data.mean()
print("\nAverage windspeed in January for each location:")
print(january_avg)

# Step 9: Downsample the record to a yearly frequency for each location
yearly_data = data.resample('YE').mean()
print("\nYearly frequency data (average windspeed):")
print(yearly_data.head())

# Step 10: Downsample the record to a monthly frequency for each location
monthly_data = data.resample('ME').mean()
print("\nMonthly frequency data (average windspeed):")
print(monthly_data.head())

# Step 11: Downsample the record to a weekly frequency for each location
weekly_data = data.resample('W').mean()
print("\nWeekly frequency data (average windspeed):")
print(weekly_data.head())

# Step 12: Calculate the min, max, mean, and standard deviation of the windspeeds across all locations for each week (assume the first week starts on January 2, 1961) for the first 52 weeks
weekly_stats = data.resample('W').agg(['min', 'max', 'mean', 'std']).iloc[:52]
print("\nWeekly statistics (min, max, mean, std) for the first 52 weeks:")
print(weekly_stats.head())
