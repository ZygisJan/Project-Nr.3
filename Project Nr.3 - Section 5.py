import pandas as pd

# Step 1: Create the 3 DataFrames based on the following raw data
raw_data_1 = {
    'subject_id': ['1', '2', '3', '4', '5'],
    'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']
}

raw_data_2 = {
    'subject_id': ['4', '5', '6', '7', '8'],
    'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']
}

raw_data_3 = {
    'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
    'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]
}

# Assign each to a variable called data1, data2, data3
data1 = pd.DataFrame(raw_data_1)
data2 = pd.DataFrame(raw_data_2)
data3 = pd.DataFrame(raw_data_3)

# Step 4: Join the two dataframes along rows and assign all_data
all_data = pd.concat([data1, data2], axis=0)
print("\nAll data combined along rows:")
print(all_data)

# Step 5: Join the two dataframes along columns and assign to all_data_col
all_data_col = pd.concat([data1, data2], axis=1)
print("\nAll data combined along columns:")
print(all_data_col)

# Step 6: Print data3
print("\nData3 DataFrame:")
print(data3)

# Step 7: Merge all_data and data3 along the 'subject_id' value
merged_data = pd.merge(all_data, data3, on='subject_id')
print("\nMerged data (all_data and data3) based on subject_id:")
print(merged_data)

# Step 8: Merge only the data that has the same 'subject_id' on both data1 and data2
common_data = pd.merge(data1, data2, on='subject_id', how='inner')
print("\nData with the same 'subject_id' on both data1 and data2:")
print(common_data)

# Step 9: Merge all values in data1 and data2, with matching records from both sides where available
outer_merged_data = pd.merge(data1, data2, on='subject_id', how='outer')
print("\nAll values merged from data1 and data2 with matching records where available:")
print(outer_merged_data)
