import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Week 3 - Advanced Data Analysis and Visualization")
print("Libraries imported successfully.")

print("\nStep 2: Creating hypothetical logistics dataset")

np.random.seed(42)

number_of_shipments = 500

logistics_data = pd.DataFrame({
    "Shipment_ID": range(1, number_of_shipments + 1),
    "Delivery_Time_Days": np.random.normal(4.5, 1.2, number_of_shipments),
    "Shipment_Volume_kg": np.random.normal(250, 80, number_of_shipments),
    "Transportation_Cost": np.random.normal(500, 150, number_of_shipments),
    "Distance_km": np.random.normal(450, 150, number_of_shipments),
    "Fuel_Cost": np.random.normal(180, 60, number_of_shipments)
})

logistics_data["Delivery_Time_Days"] = logistics_data["Delivery_Time_Days"].clip(lower=1)
logistics_data["Shipment_Volume_kg"] = logistics_data["Shipment_Volume_kg"].clip(lower=20)
logistics_data["Transportation_Cost"] = logistics_data["Transportation_Cost"].clip(lower=50)
logistics_data["Distance_km"] = logistics_data["Distance_km"].clip(lower=50)
logistics_data["Fuel_Cost"] = logistics_data["Fuel_Cost"].clip(lower=20)

print("Hypothetical logistics dataset created successfully.")
print("Number of shipments:", len(logistics_data))
print("Number of columns:", len(logistics_data.columns))

print("\nFirst 5 shipments:")
print(logistics_data.head())

print("\nStep 3: Inspecting the logistics dataset")

print("\nDataset shape:")
print(logistics_data.shape)

print("\nColumn names:")
print(logistics_data.columns.tolist())

print("\nData types:")
print(logistics_data.dtypes)

print("\nFirst 10 rows:")
print(logistics_data.head(10))

print("\nLast 5 rows:")
print(logistics_data.tail())

print("\nBasic information:")
print(logistics_data.info())

print("\nStep 4: Checking missing values and data quality")

print("\nMissing values in each column:")
print(logistics_data.isnull().sum())

print("\nTotal missing values:")
print(logistics_data.isnull().sum().sum())

print("\nDuplicate rows:")
print(logistics_data.duplicated().sum())

print("\nChecking for negative values:")

numeric_columns = [
    "Delivery_Time_Days",
    "Shipment_Volume_kg",
    "Transportation_Cost",
    "Distance_km",
    "Fuel_Cost"
]

for column in numeric_columns:
    print(column, "minimum value:", logistics_data[column].min())

    print("\nStep 5: Calculating descriptive statistics")

print("\nDescriptive statistics:")
print(logistics_data.describe())

print("\nMean values:")
print(logistics_data[numeric_columns].mean())

print("\nMedian values:")
print(logistics_data[numeric_columns].median())

print("\nStandard deviation:")
print(logistics_data[numeric_columns].std())

print("\nStep 6: Analyzing delivery-time distribution")

delivery_mean = logistics_data["Delivery_Time_Days"].mean()
delivery_median = logistics_data["Delivery_Time_Days"].median()
delivery_min = logistics_data["Delivery_Time_Days"].min()
delivery_max = logistics_data["Delivery_Time_Days"].max()

print("Average delivery time:", round(delivery_mean, 2), "days")
print("Median delivery time:", round(delivery_median, 2), "days")
print("Minimum delivery time:", round(delivery_min, 2), "days")
print("Maximum delivery time:", round(delivery_max, 2), "days")

print("\nDelivery-time percentiles:")
print(logistics_data["Delivery_Time_Days"].quantile([0.25, 0.50, 0.75, 0.90, 0.95]))

print("\nStep 7: Analyzing shipment volume")

volume_mean = logistics_data["Shipment_Volume_kg"].mean()
volume_median = logistics_data["Shipment_Volume_kg"].median()
volume_min = logistics_data["Shipment_Volume_kg"].min()
volume_max = logistics_data["Shipment_Volume_kg"].max()

print("Average shipment volume:", round(volume_mean, 2), "kg")
print("Median shipment volume:", round(volume_median, 2), "kg")
print("Minimum shipment volume:", round(volume_min, 2), "kg")
print("Maximum shipment volume:", round(volume_max, 2), "kg")

print("\nShipment-volume percentiles:")
print(
    logistics_data["Shipment_Volume_kg"].quantile(
        [0.25, 0.50, 0.75, 0.90, 0.95]
    )
)

print("\nStep 8: Analyzing transportation costs")

cost_mean = logistics_data["Transportation_Cost"].mean()
cost_median = logistics_data["Transportation_Cost"].median()
cost_min = logistics_data["Transportation_Cost"].min()
cost_max = logistics_data["Transportation_Cost"].max()

print("Average transportation cost:", round(cost_mean, 2))
print("Median transportation cost:", round(cost_median, 2))
print("Minimum transportation cost:", round(cost_min, 2))
print("Maximum transportation cost:", round(cost_max, 2))

print("\nTransportation-cost percentiles:")
print(
    logistics_data["Transportation_Cost"].quantile(
        [0.25, 0.50, 0.75, 0.90, 0.95]
    )
)

print("\nStep 9: Creating delivery-time visualization")

plt.figure(figsize=(10, 6))

plt.hist(
    logistics_data["Delivery_Time_Days"],
    bins=20,
    edgecolor="black"
)

plt.title("Distribution of Delivery Times")
plt.xlabel("Delivery Time (Days)")
plt.ylabel("Number of Shipments")
plt.grid(axis="y", alpha=0.3)

plt.savefig("delivery_time_distribution.png", dpi=300, bbox_inches="tight")

plt.show()

print("Delivery-time visualization saved successfully.")

print("\nStep 10: Creating shipment-volume visualization")

plt.figure(figsize=(10, 6))

plt.hist(
    logistics_data["Shipment_Volume_kg"],
    bins=20,
    edgecolor="black"
)

plt.title("Distribution of Shipment Volume")
plt.xlabel("Shipment Volume (kg)")
plt.ylabel("Number of Shipments")
plt.grid(axis="y", alpha=0.3)

plt.savefig("shipment_volume_distribution.png", dpi=300, bbox_inches="tight")

plt.show()

print("Shipment-volume visualization saved successfully.")

print("\nStep 11: Creating transportation-cost visualization")

plt.figure(figsize=(10, 6))

plt.hist(
    logistics_data["Transportation_Cost"],
    bins=20,
    edgecolor="black"
)

plt.title("Distribution of Transportation Costs")
plt.xlabel("Transportation Cost")
plt.ylabel("Number of Shipments")
plt.grid(axis="y", alpha=0.3)

plt.savefig("transportation_cost_distribution.png", dpi=300, bbox_inches="tight")

plt.show()

print("Transportation-cost visualization saved successfully.")

print("\nStep 12: Performing correlation analysis")

correlation_columns = [
    "Delivery_Time_Days",
    "Shipment_Volume_kg",
    "Transportation_Cost",
    "Distance_km",
    "Fuel_Cost"
]

correlation_matrix = logistics_data[correlation_columns].corr()

print("\nCorrelation matrix:")
print(correlation_matrix)

correlation_matrix.to_csv("correlation_matrix.csv")

print("\nCorrelation matrix saved successfully.")

print("\nStep 13: Generating analytical logistics insights")

print("\n--- Logistics Insights ---")

average_delivery = logistics_data["Delivery_Time_Days"].mean()
average_volume = logistics_data["Shipment_Volume_kg"].mean()
average_cost = logistics_data["Transportation_Cost"].mean()
average_distance = logistics_data["Distance_km"].mean()
average_fuel = logistics_data["Fuel_Cost"].mean()

print(
    "1. Average delivery time is",
    round(average_delivery, 2),
    "days."
)

print(
    "2. Average shipment volume is",
    round(average_volume, 2),
    "kg."
)

print(
    "3. Average transportation cost is",
    round(average_cost, 2)
)

print(
    "4. Average transportation distance is",
    round(average_distance, 2),
    "km."
)

print(
    "5. Average fuel cost is",
    round(average_fuel, 2)
)

cost_distance_corr = correlation_matrix.loc[
    "Transportation_Cost",
    "Distance_km"
]

cost_fuel_corr = correlation_matrix.loc[
    "Transportation_Cost",
    "Fuel_Cost"
]

cost_volume_corr = correlation_matrix.loc[
    "Transportation_Cost",
    "Shipment_Volume_kg"
]

print(
    "\n6. Correlation between transportation cost and distance:",
    round(cost_distance_corr, 3)
)

print(
    "7. Correlation between transportation cost and fuel cost:",
    round(cost_fuel_corr, 3)
)

print(
    "8. Correlation between transportation cost and shipment volume:",
    round(cost_volume_corr, 3)
)

print("\nInterpretation:")

if cost_distance_corr > 0.5:
    print(
        "- Distance has a strong positive relationship with transportation cost."
    )
else:
    print(
        "- Distance does not show a strong positive relationship with transportation cost."
    )

if cost_fuel_corr > 0.5:
    print(
        "- Fuel cost has a strong positive relationship with transportation cost."
    )
else:
    print(
        "- Fuel cost does not show a strong positive relationship with transportation cost."
    )

if cost_volume_corr > 0.5:
    print(
        "- Shipment volume has a strong positive relationship with transportation cost."
    )
else:
    print(
        "- Shipment volume does not show a strong positive relationship with transportation cost."
    )

print(
    "\nOverall, the analysis can help logistics managers identify "
    "important cost drivers and areas requiring further investigation."
)

print("\nStep 14: Final validation and saving results")

print("\nFinal dataset shape:")
print(logistics_data.shape)

print("\nFinal column names:")
print(logistics_data.columns.tolist())

print("\nFinal missing-value check:")
print(logistics_data.isnull().sum())

print("\nFinal duplicate check:")
print(logistics_data.duplicated().sum())

print("\nFinal dataset preview:")
print(logistics_data.head())

logistics_data.to_csv("logistics_analysis.csv", index=False)

print("\nComplete logistics dataset saved successfully.")
print("Week 3 analysis completed successfully.")
