# Step 1. Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2. Import the dataset from the provided address
url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Titanic_Desaster/train.csv"

# Step 3. Assign it to a variable titanic
titanic = pd.read_csv(url)

# Step 4. Set PassengerId as the index
titanic.set_index('PassengerId', inplace=True)

# Step 5. Create a pie chart presenting the male/female proportion
gender_counts = titanic['Sex'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Proportion of Male/Female Passengers')
plt.show()

# Step 6. Create a scatterplot with the Fare paid and the Age, differ the plot color by gender
plt.figure(figsize=(10, 6))
sns.scatterplot(data=titanic, x='Fare', y='Age', hue='Sex', alpha=0.7)
plt.title('Scatterplot of Fare vs. Age (Colored by Gender)')
plt.xlabel('Fare')
plt.ylabel('Age')
plt.show()

# Step 7. How many people survived?
survived_count = titanic['Survived'].sum()
print(f"Number of people who survived: {survived_count}")

# Step 8. Create a histogram with the Fare paid
plt.figure(figsize=(10, 6))
sns.histplot(titanic['Fare'], bins=30, kde=True)
plt.title('Histogram of Fare Paid')
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.show()

# Step 9. Question: What is the survival rate for each class?
survival_rate_per_class = titanic.groupby('Pclass')['Survived'].mean()
print("\nSurvival rate per class:")
print(survival_rate_per_class)
