import pandas as pd

# Read the CSV file with semicolon as delimiter
df = pd.read_csv('definition.csv', sep=';', header=None)

# Extract the relevant columns
df = df[[0, 4]]

# Format the output
output = df.apply(lambda row: f"province = {row[0]} #{row[4]}", axis=1)

# Save the output to a new file
with open('output.txt', 'w') as f:
    f.write('\n'.join(output))

print("Conversion complete. Check the output.txt file.")