import pandas as pd

# Load your CSV file into a DataFrame
df = pd.read_csv("Ababo/Specimen_RawData_1.csv")

# Define the value of i
i = 300  # Set your desired value of i

# Find the closest value to i in the first column
closest_value = df.iloc[(df['Time']-i).abs().argsort()[:1]].iloc[0]

# Get the relevant values from the other columns
relevant_values = closest_value[['Load', 'Extension']]

print(relevant_values)
