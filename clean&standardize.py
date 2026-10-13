import pandas as pd

# Create a dataset
data = {
    "user": ["Aman", "Riya", "Aman", "Kabir"],
    "text": [
        " AWS is GREAT! ",
        "Good cloud session",
        " AWS is GREAT! ",
        None
    ]
}

# Convert the dataset into a DataFrame
df = pd.DataFrame(data)

# Remove duplicate rows
df = df.drop_duplicates()

# Replace missing values with empty strings
df["text"] = df["text"].fillna("")

# Remove leading and trailing spaces and convert text to lowercase
df["text"] = df["text"].str.strip().str.lower()

# Display the cleaned data
print("Cleaned Data:")
print(df)
