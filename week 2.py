import pandas as pd
import numpy as np

print("Week 2 - Data Collection, Cleaning and Preprocessing")
print("Libraries loaded successfully.")
print("\nStep 2: Loading and inspecting the dataset")

df = pd.read_excel("Online Retail.xlsx")

print("Dataset loaded successfully.")
print("Number of rows and columns:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())
print("\nStep 3: Checking for missing values")

missing_values = df.isnull().sum()

print("\nMissing values in each column:")
print(missing_values)

print("\nPercentage of missing values:")
missing_percentage = (df.isnull().sum() / len(df)) * 100
print(missing_percentage)
print("\nStep 4: Checking for duplicate records")

duplicate_count = df.duplicated().sum()

print("Number of duplicate rows:", duplicate_count)
print("\nStep 5: Removing duplicate records")

df_clean = df.drop_duplicates().copy()

print("Original number of rows:", len(df))
print("Number of rows after removing duplicates:", len(df_clean))
print("Number of duplicate rows remaining:", df_clean.duplicated().sum())
print("\nStep 6: Handling missing values")

print("Missing values before cleaning:")
print(df_clean.isnull().sum())

df_clean["Description"] = df_clean["Description"].fillna("Unknown Product")

df_clean = df_clean.dropna(subset=["InvoiceDate", "Quantity", "UnitPrice"])

print("\nMissing values after cleaning:")
print(df_clean.isnull().sum())
print("\nStep 7: Checking invalid values and outliers")

print("Minimum Quantity:", df_clean["Quantity"].min())
print("Maximum Quantity:", df_clean["Quantity"].max())

print("Minimum Unit Price:", df_clean["UnitPrice"].min())
print("Maximum Unit Price:", df_clean["UnitPrice"].max())

Q1_quantity = df_clean["Quantity"].quantile(0.25)
Q3_quantity = df_clean["Quantity"].quantile(0.75)
IQR_quantity = Q3_quantity - Q1_quantity

lower_quantity = Q1_quantity - 1.5 * IQR_quantity
upper_quantity = Q3_quantity + 1.5 * IQR_quantity

quantity_outliers = df_clean[
    (df_clean["Quantity"] < lower_quantity) |
    (df_clean["Quantity"] > upper_quantity)
]

print("Number of Quantity outliers:", len(quantity_outliers))
print("\nStep 8: Handling Quantity outliers")

df_clean["Quantity"] = df_clean["Quantity"].clip(
    lower=0,
    upper=upper_quantity
)

print("Quantity outliers have been capped.")
print("New maximum Quantity:", df_clean["Quantity"].max())
print("\nStep 9: Final data quality check")

print("Number of rows:", len(df_clean))
print("Number of columns:", len(df_clean.columns))

print("\nMissing values after cleaning:")
print(df_clean.isnull().sum())

print("\nDuplicate rows after cleaning:")
print(df_clean.duplicated().sum())

print("\nData types:")
print(df_clean.dtypes)

print("\nFirst 5 rows of cleaned data:")
print(df_clean.head())
print("\nStep 10: Creating Revenue and preparing numeric data")

df_clean["Revenue"] = df_clean["Quantity"] * df_clean["UnitPrice"]

print("Revenue column created successfully.")

print("\nRevenue summary:")
print(df_clean["Revenue"].describe())

print("\nSample of Quantity, UnitPrice and Revenue:")
print(df_clean[["Quantity", "UnitPrice", "Revenue"]].head())
print("\nStep 11: Normalizing numerical data")

from sklearn.preprocessing import StandardScaler

features = ["Quantity", "UnitPrice", "Revenue"]

scaler = StandardScaler()

df_clean[["Quantity_scaled", "UnitPrice_scaled", "Revenue_scaled"]] = scaler.fit_transform(
    df_clean[features]
)

print("Normalization completed successfully.")

print("\nOriginal and normalized values:")
print(
    df_clean[
        [
            "Quantity",
            "Quantity_scaled",
            "UnitPrice",
            "UnitPrice_scaled",
            "Revenue",
            "Revenue_scaled"
        ]
    ].head()
)

print("\nStep 12: Saving the cleaned and preprocessed dataset")

df_clean.to_csv("cleaned_logistics_data.csv", index=False)

print("Cleaned dataset saved successfully.")
print("File name: cleaned_logistics_data.csv")

print("\nStep 13: Creating preprocessing summary")

preprocessing_summary = pd.DataFrame({
    "Metric": [
        "Original rows",
        "Cleaned rows",
        "Rows removed",
        "Original columns",
        "Cleaned columns",
        "Duplicate rows remaining"
    ],
    "Value": [
        len(df),
        len(df_clean),
        len(df) - len(df_clean),
        len(df.columns),
        len(df_clean.columns),
        df_clean.duplicated().sum()
    ]
})

preprocessing_summary.to_csv(
    "preprocessing_summary.csv",
    index=False
)

print("Preprocessing summary saved successfully.")
print(preprocessing_summary)

print("\nStep 14: Final validation of the preprocessed dataset")

print("Final number of rows:", len(df_clean))
print("Final number of columns:", len(df_clean.columns))

print("\nRemaining duplicate rows:")
print(df_clean.duplicated().sum())

print("\nRemaining missing values:")
print(df_clean.isnull().sum())

print("\nFinal data preview:")
print(df_clean.head())

print("\nWeek 2 preprocessing completed successfully.")