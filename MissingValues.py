import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    "post": [
        "Good product",
        "Bad service",
        "Good product",
        None
    ],
    "likes": ["10", "5", "10", "3"]
})

# Display DataFrame information
print(df.info())

# Remove duplicate rows
df = df.drop_duplicates()

# Replace missing post values
df["post"] = df["post"].fillna("unknown")

# Convert likes to numeric values
df["likes"] = pd.to_numeric(
    df["likes"],
    errors="coerce"
)

# Replace missing numeric values with 0
df["likes"] = df["likes"].fillna(0)

# Save the processed data to a CSV file
df.to_csv("processed_social_data.csv", index=False)

# Display the processed DataFrame
print(df)

print("Processed file saved.")
