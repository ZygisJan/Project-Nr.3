import pandas as pd

# Step 1: Import the dataset from this address
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv'
drinks = pd.read_csv(url)

# Converting specified columns to numeric
numeric_columns = ['beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol']
for column in numeric_columns:
    drinks[column] = pd.to_numeric(drinks[column], errors='coerce')

# Step 2: Assign it to a variable called drinks
print("Dataset overview:")
print(drinks.head())

# Step 3: Which continent drinks more beer on average?
beer_avg = drinks.groupby('continent')['beer_servings'].mean().sort_values(ascending=False)
print("\nContinent that drinks more beer on average:")
print(beer_avg)

# Step 4: For each continent print the statistics for wine consumption
wine_stats = drinks.groupby('continent')['wine_servings'].describe()
print("\nStatistics for wine consumption per continent:")
print(wine_stats)

# Step 5: Print the mean alcohol consumption per continent for numeric columns only
mean_alcohol = drinks.groupby('continent')[numeric_columns].mean()
print("\nMean alcohol consumption per continent for numeric columns only:")
print(mean_alcohol)

# Step 6: Print the median alcohol consumption per continent for numeric columns only
median_alcohol = drinks.groupby('continent')[numeric_columns].median()
print("\nMedian alcohol consumption per continent for numeric columns only:")
print(median_alcohol)

# Step 7: Print the mean, min, and max values for spirit consumption
spirit_stats = drinks.groupby('continent')['spirit_servings'].agg(['mean', 'min', 'max'])
print("\nMean, min, and max values for spirit consumption per continent:")
print(spirit_stats)


