
# # WEEK 1 LOGISTICS DATA ANALYSIS PROJECT
# # Strategic Planning and Data Exploration in Logistics
# # STEP 1: IMPORT LIBRARIES
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_absolute_error, mean_squared_error
# from sklearn.preprocessing import StandardScaler
# from sklearn.cluster import KMeans
# print ("all libraries importes successfully!")
# #load the excel dataset
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_absolute_error, mean_squared_error
# from sklearn.preprocessing import StandardScaler
# from sklearn.cluster import KMeans


# print("all libraries importes successfully!")
# df = pd.read_excel("Online Retail.xlsx")
# print("Dataset loaded successfully!")
# print("Dataset size:")
# print(df.shape)
# print("\nFirst 5 rows:")
# print(df.head())
# #explore the data set
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_absolute_error, mean_squared_error
# from sklearn.preprocessing import StandardScaler
# from sklearn.cluster import KMeans


# df = pd.read_excel("Online Retail.xlsx")

# print("=" * 50)
# print("DATASET EXPLORATION")
# print("=" * 50)

# print("\nDataset size:")
# print(df.shape)

# print("\nColumn names:")
# print(df.columns.tolist())

# print("\nFirst 5 rows:")
# print(df.head())

# print("\nMissing values:")
# print(df.isnull().sum())

# print("\nBasic statistics:")
# print(df.describe())
# #data cleaning
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_absolute_error, mean_squared_error
# from sklearn.preprocessing import StandardScaler
# from sklearn.cluster import KMeans


# df = pd.read_excel("Online Retail.xlsx")

# print("=" * 50)
# print("DATA CLEANING")
# print("=" * 50)

# # Convert InvoiceDate into a proper date/time format
# df["InvoiceDate"] = pd.to_datetime(
#     df["InvoiceDate"],
#     errors="coerce"
# )

# # Make sure Quantity is numeric
# df["Quantity"] = pd.to_numeric(
#     df["Quantity"],
#     errors="coerce"
# )

# # Make sure UnitPrice is numeric
# df["UnitPrice"] = pd.to_numeric(
#     df["UnitPrice"],
#     errors="coerce"
# )

# # Identify cancelled orders
# df["is_cancelled"] = (
#     df["InvoiceNo"]
#     .astype(str)
#     .str.startswith("C")
# )

# print(
#     "\nCancelled transactions:",
#     df["is_cancelled"].sum()
# )

# # Remove cancelled orders
# sales = df[
#     df["is_cancelled"] == False
# ].copy()

# # Remove transactions with zero or negative quantities
# sales = sales[
#     sales["Quantity"] > 0
# ]

# # Remove transactions with zero or negative prices
# sales = sales[
#     sales["UnitPrice"] > 0
# ]

# # Remove rows without a product code
# sales = sales.dropna(
#     subset=["StockCode"]
# )

# # Calculate revenue
# sales["Revenue"] = (
#     sales["Quantity"] *
#     sales["UnitPrice"]
# )

# print("\nOriginal dataset:")
# print(df.shape)

# print("\nClean dataset:")
# print(sales.shape)

# print("\nData cleaning completed successfully!")
# #calculate logistics KPI's
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_absolute_error, mean_squared_error
# from sklearn.preprocessing import StandardScaler
# from sklearn.cluster import KMeans

# # LOAD DATA
# df = pd.read_excel("Online Retail.xlsx")
# # DATA CLEANING
# df["InvoiceDate"] = pd.to_datetime(
#     df["InvoiceDate"],
#     errors="coerce"
# )

# df["Quantity"] = pd.to_numeric(
#     df["Quantity"],
#     errors="coerce"
# )

# df["UnitPrice"] = pd.to_numeric(
#     df["UnitPrice"],
#     errors="coerce"
# )

# # Identify cancelled transactions
# df["is_cancelled"] = (
#     df["InvoiceNo"]
#     .astype(str)
#     .str.startswith("C")
# )

# # Remove cancelled transactions
# sales = df[
#     df["is_cancelled"] == False
# ].copy()

# # Remove invalid quantities
# sales = sales[
#     sales["Quantity"] > 0
# ]

# # Remove invalid prices
# sales = sales[
#     sales["UnitPrice"] > 0
# ]

# # Remove missing product codes
# sales = sales.dropna(
#     subset=["StockCode"]
# )

# # Calculate revenue
# sales["Revenue"] = (
#     sales["Quantity"] *
#     sales["UnitPrice"]
# )
# # STEP 5 — LOGISTICS KPIs

# print("=" * 60)
# print("STEP 5 — LOGISTICS KPI CALCULATION")
# print("=" * 60)

# # KPI 1 — Total Revenue
# total_revenue = sales["Revenue"].sum()


# # KPI 2 — Total Units Sold
# total_units = sales["Quantity"].sum()


# # KPI 3 — Total Orders
# total_orders = sales["InvoiceNo"].nunique()


# # KPI 4 — Number of Products
# number_products = sales["StockCode"].nunique()


# # KPI 5 — Number of Customers
# number_customers = sales["CustomerID"].nunique()


# # KPI 6 — Average Order Value
# average_order_value = (
#     total_revenue / total_orders
# )
# # DISPLAY RESULTS

# print("\nLOGISTICS KPI RESULTS")
# print("-" * 60)

# print(
#     f"1. Total Revenue: £{total_revenue:,.2f}"
# )

# print(
#     f"2. Total Units Sold: {total_units:,.0f}"
# )

# print(
#     f"3. Total Orders: {total_orders:,}"
# )

# print(
#     f"4. Number of Products: {number_products:,}"
# )

# print(
#     f"5. Number of Customers: {number_customers:,}"
# )

# print(
#     f"6. Average Order Value: £{average_order_value:,.2f}"
# )

# print("-" * 60)

# print("\nStep 5 completed successfully!")
# #daily demand analysis
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_absolute_error, mean_squared_error
# from sklearn.preprocessing import StandardScaler
# from sklearn.cluster import KMeans
# # LOAD DATA
# df = pd.read_excel("Online Retail.xlsx")
# # DATA CLEANING
# df["InvoiceDate"] = pd.to_datetime(
#     df["InvoiceDate"],
#     errors="coerce"
# )

# df["Quantity"] = pd.to_numeric(
#     df["Quantity"],
#     errors="coerce"
# )

# df["UnitPrice"] = pd.to_numeric(
#     df["UnitPrice"],
#     errors="coerce"
# )

# # Identify cancelled transactions
# df["is_cancelled"] = (
#     df["InvoiceNo"]
#     .astype(str)
#     .str.startswith("C")
# )

# # Remove cancelled transactions
# sales = df[
#     df["is_cancelled"] == False
# ].copy()

# # Remove invalid quantities
# sales = sales[
#     sales["Quantity"] > 0
# ]

# # Remove invalid prices
# sales = sales[
#     sales["UnitPrice"] > 0
# ]

# # Remove missing product codes
# sales = sales.dropna(
#     subset=["StockCode"]
# )

# #DAILY DEMAND ANALYSIS
# print("=" * 60)
# print("STEP 6 — DAILY DEMAND ANALYSIS")
# print("=" * 60)


# # Calculate total units sold each day
# daily_demand = (
#     sales.groupby(
#         sales["InvoiceDate"].dt.date
#     )["Quantity"]
#     .sum()
#     .reset_index()
# )


# # Rename columns
# daily_demand.columns = [
#     "Date",
#     "Units_Sold"
# ]
# # Convert Date back to datetime
# daily_demand["Date"] = pd.to_datetime(
#     daily_demand["Date"]
# )
# # Sort by date
# daily_demand = daily_demand.sort_values(
#     "Date"
# )
# # DISPLAY DAILY DEMAND
# print("\nFirst 10 days of demand:")

# print(
#     daily_demand.head(10)
# )
# print("\nTotal days analyzed:")

# print(
#     len(daily_demand)
# )


# print("\nAverage daily demand:")

# print(
#     f"{daily_demand['Units_Sold'].mean():,.2f} units"
# )
# # CREATE DAILY DEMAND GRAPH
# plt.figure(
#     figsize=(12, 5)
# )

# plt.plot(
#     daily_demand["Date"],
#     daily_demand["Units_Sold"]
# )

# plt.title(
#     "Daily Demand Trend"
# )

# plt.xlabel(
#     "Date"
# )
# plt.ylabel(
#     "Units Sold"
# )
# plt.xticks(
#     rotation=45
# )
# plt.tight_layout()
# plt.show()
# print("\nStep 6 completed successfully!")

# #top 10 products

# import pandas as pd
# import matplotlib.pyplot as plt
# # LOAD DATA
# df = pd.read_excel("Online Retail.xlsx")
# # DATA CLEANING
# df["InvoiceDate"] = pd.to_datetime(
#     df["InvoiceDate"],
#     errors="coerce"
# )

# df["Quantity"] = pd.to_numeric(
#     df["Quantity"],
#     errors="coerce"
# )

# df["UnitPrice"] = pd.to_numeric(
#     df["UnitPrice"],
#     errors="coerce"
# )

# # Identify cancelled transactions
# df["is_cancelled"] = (
#     df["InvoiceNo"]
#     .astype(str)
#     .str.startswith("C")
# )

# # Keep valid sales
# sales = df[
#     (df["is_cancelled"] == False) &
#     (df["Quantity"] > 0) &
#     (df["UnitPrice"] > 0)
# ].copy()
# # STEP 7 — TOP PRODUCTS
# print("=" * 60)
# print("STEP 7 — TOP 10 PRODUCTS BY UNITS SOLD")
# print("=" * 60)


# # Calculate total quantity sold for each product
# top_products = (
#     sales.groupby("StockCode")["Quantity"]
#     .sum()
#     .sort_values(
#         ascending=False
#     )
#     .head(10)
# )


# # Display results
# print("\nTop 10 products by units sold:")

# print(
#     top_products
# )
# # CREATE GRAPH
# plt.figure(
#     figsize=(10, 6)
# )

# top_products.sort_values().plot(
#     kind="barh"
# )

# plt.title(
#     "Top 10 Products by Units Sold"
# )

# plt.xlabel(
#     "Units Sold"
# )

# plt.ylabel(
#     "Product Code"
# )
# plt.tight_layout()
# plt.show()
# print("\nStep 7 completed successfully!")
# #monthly demand

# import pandas as pd
# import matplotlib.pyplot as plt
# # LOAD DATA
# df = pd.read_excel("Online Retail.xlsx")
# # DATA CLEANING
# df["InvoiceDate"] = pd.to_datetime(
#     df["InvoiceDate"],
#     errors="coerce"
# )

# df["Quantity"] = pd.to_numeric(
#     df["Quantity"],
#     errors="coerce"
# )

# df["UnitPrice"] = pd.to_numeric(
#     df["UnitPrice"],
#     errors="coerce"
# )
# # Identify cancelled transactions
# df["is_cancelled"] = (
#     df["InvoiceNo"]
#     .astype(str)
#     .str.startswith("C")
# )
# # Keep valid sales
# sales = df[
#     (df["is_cancelled"] == False) &
#     (df["Quantity"] > 0) &
#     (df["UnitPrice"] > 0)
# ].copy()
# # STEP 8 — MONTHLY DEMAND ANALYSIS
# print("=" * 60)
# print("STEP 8 — MONTHLY DEMAND ANALYSIS")
# print("=" * 60)
# # Calculate total units sold each month
# monthly_demand = (
#     sales.groupby(
#         sales["InvoiceDate"].dt.to_period("M")
#     )["Quantity"]
#     .sum()
# )
# # Display results
# print("\nMonthly demand:")

# print(
#     monthly_demand
# )
# # FIND HIGHEST AND LOWEST DEMAND MONTHS
# highest_month = (
#     monthly_demand.idxmax()
# )
# highest_demand = (
#     monthly_demand.max()
# )

# lowest_month = (
#     monthly_demand.idxmin()
# )
# lowest_demand = (
#     monthly_demand.min()
# )
# print("\nHighest demand month:")

# print(
#     highest_month,
#     f"({highest_demand:,.0f} units)"
# )
# print("\nLowest demand month:")

# print(
#     lowest_month,
#     f"({lowest_demand:,.0f} units)"
# )
# # CREATE MONTHLY DEMAND GRAPH
# plt.figure(
#     figsize=(12, 5)
# )

# monthly_demand.plot()

# plt.title(
#     "Monthly Demand Trend"
# )

# plt.xlabel(
#     "Month"
# )

# plt.ylabel(
#     "Units Sold"
# )
# plt.xticks(
#     rotation=45
# )
# plt.tight_layout()
# plt.show()
# print("\nStep 8 completed successfully!")
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_absolute_error, mean_squared_error

# # LOAD DATA
# df = pd.read_excel("Online Retail.xlsx")

# # DATA CLEANING

# df["InvoiceDate"] = pd.to_datetime(
#     df["InvoiceDate"],
#     errors="coerce"
# )

# df["Quantity"] = pd.to_numeric(
#     df["Quantity"],
#     errors="coerce"
# )

# df["UnitPrice"] = pd.to_numeric(
#     df["UnitPrice"],
#     errors="coerce"
# )


# # Identify cancelled transactions
# df["is_cancelled"] = (
#     df["InvoiceNo"]
#     .astype(str)
#     .str.startswith("C")
# )
# # Keep valid sales
# sales = df[
#     (df["is_cancelled"] == False) &
#     (df["Quantity"] > 0) &
#     (df["UnitPrice"] > 0)
# ].copy()

# # CREATE DAILY DEMAND DATA
# forecast_data = (
#     sales.groupby(
#         sales["InvoiceDate"].dt.date
#     )["Quantity"]
#     .sum()
#     .reset_index()
# )
# forecast_data.columns = [
#     "Date",
#     "Quantity"
# ]
# forecast_data["Date"] = pd.to_datetime(
#     forecast_data["Date"]
# )
# forecast_data = forecast_data.sort_values(
#     "Date"
# )
# # CREATE FORECASTING FEATURES
# # Previous day's demand
# forecast_data["lag_1"] = (
#     forecast_data["Quantity"].shift(1)
# )

# # Demand 7 days earlier
# forecast_data["lag_7"] = (
#     forecast_data["Quantity"].shift(7)
# )

# # Demand 14 days earlier
# forecast_data["lag_14"] = (
#     forecast_data["Quantity"].shift(14)
# )

# # Seven-day moving average
# forecast_data["rolling_7"] = (
#     forecast_data["Quantity"]
#     .shift(1)
#     .rolling(7)
#     .mean()
# )

# # Day of week
# forecast_data["day_of_week"] = (
#     forecast_data["Date"].dt.dayofweek
# )

# # Month
# forecast_data["month"] = (
#     forecast_data["Date"].dt.month
# )
# # Remove rows containing missing values
# forecast_data = forecast_data.dropna()
# # SELECT FEATURES
# features = [
#     "lag_1",
#     "lag_7",
#     "lag_14",
#     "rolling_7",
#     "day_of_week",
#     "month"
# ]


# target = "Quantity"

# # TRAIN
# # Use the first 80% for training
# # and the final 20% for testing

# split_index = int(
#     len(forecast_data) * 0.80
# )
# train = forecast_data.iloc[
#     :split_index
# ]


# test = forecast_data.iloc[
#     split_index:
# ]


# X_train = train[features]

# y_train = train[target]

# X_test = test[features]

# y_test = test[target]


# print("=" * 60)
# print("STEP 9 — DEMAND FORECASTING")
# print("=" * 60)
# print(
#     "\nTraining records:",
#     len(train)
# )
# print(
#     "Testing records:",
#     len(test)
# )
# # TRAIN RANDOM FOREST MODEL
# print("\nTraining Random Forest model...")
# model = RandomForestRegressor(
#     n_estimators=100,
#     random_state=42,
#     n_jobs=-1
# )


# model.fit(
#     X_train,
#     y_train
# )
# print(
#     "Model training completed!"
# )

# # MAKE PREDICTIONS
# predictions = model.predict(
#     X_test
# )
# # MODEL EVALUATION
# mae = mean_absolute_error(
#     y_test,
#     predictions
# )
# rmse = np.sqrt(
#     mean_squared_error(
#         y_test,
#         predictions
#     )
# )
# print("\nMODEL PERFORMANCE")
# print("-" * 60)
# print(
#     f"Mean Absolute Error (MAE): "
#     f"{mae:,.2f}"
# )
# print(
#     f"Root Mean Squared Error (RMSE): "
#     f"{rmse:,.2f}"
# )
# # ACTUAL VS PREDICTED GRAPH
# plt.figure(
#     figsize=(12, 5)
# )
# plt.plot(
#     test["Date"],
#     y_test.values,
#     label="Actual Demand"
# )
# plt.plot(
#     test["Date"],
#     predictions,
#     label="Predicted Demand"
# )
# plt.title(
#     "Actual vs Predicted Daily Demand"
# )
# plt.xlabel(
#     "Date"
# )
# plt.ylabel(
#     "Units Sold"
# )
# plt.legend()
# plt.xticks(
#     rotation=45
# )
# plt.tight_layout()
# plt.show()
# print("\nStep 9 completed successfully!")
#K mean product clustering
# import pandas as pd
# from sklearn.preprocessing import StandardScaler
# from sklearn.cluster import KMeans
# # LOAD DATA
# df = pd.read_excel("Online Retail.xlsx")
# # DATA CLEANING
# df["Quantity"] = pd.to_numeric(
#     df["Quantity"],
#     errors="coerce"
# )
# df["UnitPrice"] = pd.to_numeric(
#     df["UnitPrice"],
#     errors="coerce"
# )
# # Identify cancelled transactions
# df["is_cancelled"] = (
#     df["InvoiceNo"]
#     .astype(str)
#     .str.startswith("C")
# )


# # Keep valid sales
# sales = df[
#     (df["is_cancelled"] == False) &
#     (df["Quantity"] > 0) &
#     (df["UnitPrice"] > 0)
# ].copy()
# # CALCULATE REVENUE
# sales["Revenue"] = (
#     sales["Quantity"] *
#     sales["UnitPrice"]
# )
# # STEP 10 — PRODUCT CLUSTERING
# print("=" * 60)
# print("STEP 10 — K-MEANS PRODUCT CLUSTERING")
# print("=" * 60)


# # Create a profile for each product
# product_profile = (
#     sales.groupby("StockCode")
#     .agg(
#         average_units=(
#             "Quantity",
#             "mean"
#         ),

#         total_units=(
#             "Quantity",
#             "sum"
#         ),

#         total_revenue=(
#             "Revenue",
#             "sum"
#         ),

#         number_of_orders=(
#             "InvoiceNo",
#             "nunique"
#         )
#     )
#     .reset_index()
# )


# print("\nProduct profile:")
# print(
#     product_profile.head(10)
# )
# # SELECT CLUSTERING FEATURES
# features = [
#     "average_units",
#     "total_units",
#     "total_revenue",
#     "number_of_orders"
# ]


# X = product_profile[
#     features
# ]
# # STANDARDIZE THE DATA
# scaler = StandardScaler()

# X_scaled = scaler.fit_transform(
#     X
# )
# # CREATE K-MEANS MODEL
# kmeans = KMeans(
#     n_clusters=4,
#     random_state=42,
#     n_init=10
# )


# # Assign each product to a cluster
# product_profile["Segment"] = (
#     kmeans.fit_predict(
#         X_scaled
#     )
# )
# # DISPLAY PRODUCT SEGMENTS
# print("\nProduct segments:")

# print(
#     product_profile[
#         [
#             "StockCode",
#             "Segment"
#         ]
#     ].head(20)
# )
# # SUMMARIZE THE SEGMENTS
# segment_summary = (
#     product_profile
#     .groupby("Segment")
#     .agg(
#         products=(
#             "StockCode",
#             "count"
#         ),

#         total_units=(
#             "total_units",
#             "sum"
#         ),

#         total_revenue=(
#             "total_revenue",
#             "sum"
#         )
#     )
# )


# print("\nSEGMENT SUMMARY")
# print("-" * 60)

# print(
#     segment_summary
# )
# print("\nStep 10 completed successfully!")
#safety stock and reorder point
# # STEP 11 - SAFETY STOCK AND REORDER POINT

# import pandas as pd
# import numpy as np

# print("STEP 11 - SAFETY STOCK AND REORDER POINT")

# # Load data
# df = pd.read_excel("Online Retail.xlsx")

# # Data cleaning
# df["InvoiceDate"] = pd.to_datetime(
#     df["InvoiceDate"],
#     errors="coerce"
# )

# df["Quantity"] = pd.to_numeric(
#     df["Quantity"],
#     errors="coerce"
# )

# df["UnitPrice"] = pd.to_numeric(
#     df["UnitPrice"],
#     errors="coerce"
# )

# # Identify cancelled transactions
# df["is_cancelled"] = (
#     df["InvoiceNo"]
#     .astype(str)
#     .str.startswith("C")
# )

# # Keep valid sales
# sales = df[
#     (df["is_cancelled"] == False) &
#     (df["Quantity"] > 0) &
#     (df["UnitPrice"] > 0)
# ].copy()

# # Calculate daily demand
# daily_demand = (
#     sales.groupby(
#         sales["InvoiceDate"].dt.date
#     )["Quantity"]
#     .sum()
# )

# # Calculate average daily demand
# average_daily_demand = daily_demand.mean()

# # Calculate demand variability
# demand_std = daily_demand.std()

# # Inventory assumptions
# lead_time_days = 7
# z_score = 1.65

# # Calculate safety stock
# safety_stock = z_score * demand_std

# # Calculate reorder point
# reorder_point = (
#     average_daily_demand * lead_time_days
#     + safety_stock
# )

# # Display results
# print("\nInventory Analysis Results")

# print(
#     f"Average Daily Demand: "
#     f"{average_daily_demand:,.2f} units"
# )

# print(
#     f"Daily Demand Standard Deviation: "
#     f"{demand_std:,.2f} units"
# )

# print(
#     f"Assumed Lead Time: "
#     f"{lead_time_days} days"
# )

# print(
#     f"Service Level Z-Score: "
#     f"{z_score}"
# )

# print(
#     f"Safety Stock: "
#     f"{safety_stock:,.2f} units"
# )

# print(
#     f"Reorder Point: "
#     f"{reorder_point:,.2f} units"
# )

# print(
#     f"\nWhen inventory falls to approximately "
#     f"{reorder_point:,.0f} units, "
#     f"a new order should be considered."
# )

# print("\nStep 11 completed successfully!")

#saving final result
# import pandas as pd

# # Load data
# df = pd.read_excel("Online Retail.xlsx")

# # Data cleaning
# df["InvoiceDate"] = pd.to_datetime(
#     df["InvoiceDate"],
#     errors="coerce"
# )

# df["Quantity"] = pd.to_numeric(
#     df["Quantity"],
#     errors="coerce"
# )

# df["UnitPrice"] = pd.to_numeric(
#     df["UnitPrice"],
#     errors="coerce"
# )

# # Identify cancelled transactions
# df["is_cancelled"] = (
#     df["InvoiceNo"]
#     .astype(str)
#     .str.startswith("C")
# )

# # Keep valid sales
# sales = df[
#     (df["is_cancelled"] == False) &
#     (df["Quantity"] > 0) &
#     (df["UnitPrice"] > 0)
# ].copy()

# # Calculate revenue
# sales["Revenue"] = (
#     sales["Quantity"] *
#     sales["UnitPrice"]
# )

# # Calculate KPIs
# total_revenue = sales["Revenue"].sum()

# total_units = sales["Quantity"].sum()

# total_orders = sales["InvoiceNo"].nunique()

# number_products = sales["StockCode"].nunique()

# number_customers = sales["CustomerID"].nunique()

# average_order_value = (
#     total_revenue / total_orders
# )

# # Create KPI table
# kpis = pd.DataFrame({
#     "KPI": [
#         "Total Revenue",
#         "Total Units Sold",
#         "Total Orders",
#         "Number of Products",
#         "Number of Customers",
#         "Average Order Value"
#     ],
#     "Value": [
#         total_revenue,
#         total_units,
#         total_orders,
#         number_products,
#         number_customers,
#         average_order_value
#     ]
# })

# # Save KPI results
# kpis.to_csv(
#     "logistics_kpi_results.csv",
#     index=False
# )

# # Save cleaned sales data
# sales.to_csv(
#     "cleaned_logistics_data.csv",
#     index=False
# )

# print("\nSTEP 12 - RESULTS SAVED")

# print("\nFiles created:")
# print("logistics_kpi_results.csv")
# print("cleaned_logistics_data.csv")

# print("\nWeek 1 project completed successfully!")