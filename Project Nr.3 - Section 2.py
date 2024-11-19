import pandas as pd

# Step 2: Import the dataset from this address
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv'
euro12 = pd.read_csv(url)

# Step 3: Assign it to a variable called euro12
print("Dataset overview:")
print(euro12.head())

# Step 4: Select only the Goal column
print("\nGoal column:")
print(euro12['Goals'])

# Step 5: How many teams participated in the Euro2012?
print("\nNumber of teams that participated in Euro 2012:")
print(euro12.shape[0])

# Step 6: What is the number of columns in the dataset?
print("\nNumber of columns in the dataset:")
print(euro12.shape[1])

# Step 7: View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
print("\nDiscipline DataFrame:")
print(discipline)

# Step 8: Sort the teams by Red Cards, then to Yellow Cards
sorted_discipline = discipline.sort_values(by=['Red Cards', 'Yellow Cards'], ascending=[False, False])
print("\nTeams sorted by Red Cards and Yellow Cards:")
print(sorted_discipline)

# Step 9: Calculate the mean Yellow Cards given per Team
print("\nMean Yellow Cards per team:")
print(discipline['Yellow Cards'].mean())

# Step 10: Filter teams that scored more than 6 goals
print("\nTeams that scored more than 6 goals:")
print(euro12[euro12['Goals'] > 6])

# Step 11: Select the teams that start with 'G'
print("\nTeams that start with 'G':")
print(euro12[euro12['Team'].str.startswith('G')])

# Step 12: Select the first 7 columns
print("\nFirst 7 columns:")
print(euro12.iloc[:, :7])

# Step 13: Select all columns except the last 3
print("\nAll columns except the last 3:")
print(euro12.iloc[:, :-3])

# Step 14: Present only the Shooting Accuracy from England, Italy and Russia
print("\nShooting Accuracy for England, Italy, and Russia:")
print(euro12.loc[euro12['Team'].isin(['England', 'Italy', 'Russia']), ['Team', 'Shooting Accuracy']])
