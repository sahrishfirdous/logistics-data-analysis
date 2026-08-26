# Week 1 – Strategic Planning and Data Exploration in Logistics
## Project Overview
This project is part of a multi-week Logistics Data Analysis project.
Week 1 focuses on the strategic planning and initial data exploration phase of a logistics analytics project.
The project uses the Online Retail dataset to simulate a realistic retail logistics environment where historical
transaction data is analyzed to support inventory management, demand planning, and resource allocation.
The main purpose of this project is to demonstrate how Python and data science techniques can be used to transform raw transaction data into useful logistics information and support better business decision-making.
## Project Objectives
The objectives of Week 1 are to:
- Understand and define a realistic logistics problem.
- Explore and understand the available dataset.
- Clean and prepare the transaction data.
- Identify important logistics Key Performance Indicators (KPIs).
- Analyze historical demand patterns.
- Identify high-demand products.
- Demonstrate demand forecasting using Random Forest Regression.
- Segment products using K-Means clustering.
- Calculate basic inventory planning measures such as safety stock and reorder point.
- Develop an end-to-end roadmap for logistics data analysis.
## Dataset
The project uses the Online Retail dataset.
The dataset contains transaction records with information such as:
- Invoice number
- Product/Stock code
- Product description
- Quantity purchased
- Invoice date
- Unit price
- Customer ID
- Country
The dataset contains 541,909 transaction records and 8 columns.
The dataset is used to represent a simplified retail logistics environment. 
Since actual inventory levels, supplier lead times, warehouse capacity, 
and stockout records are not available, sales quantity is used as a proxy for demand.

## Key Performance Indicators
The project focuses on several important KPIs:
1. Total Revenue
2. Total Units Sold
3. Total Orders
4. Number of Products
5. Number of Customers
6. Average Order Value
7. Forecasting MAE
8. Forecasting RMSE
9. Safety Stock
10. Reorder Point
These KPIs help evaluate demand, sales activity, operational workload, and inventory requirements.
## Data Cleaning
The raw dataset is cleaned using Python before analysis.
The cleaning process includes:
- Converting dates into the correct datetime format.
- Converting quantity and price fields into numeric values.
- Identifying cancelled transactions.
- Removing cancelled transactions from the main sales analysis.
- Removing transactions with invalid or non-positive quantities.
- Removing transactions with invalid or non-positive prices.
- Creating a revenue column.
These steps help prevent incorrect records from affecting the analysis.
## Data Science Methods
Several data science techniques are introduced in this project.
### Exploratory Data Analysis
Historical transactions are grouped by date and product to understand:
- Daily demand
- Monthly demand
- High-demand products
- Revenue patterns
- Order activity
Visualizations are created using Matplotlib.
### Random Forest Regression
Random Forest Regression is used as an example of predictive analytics.
Historical demand features such as:
- Previous-day demand
- Seven-day lag demand
- Fourteen-day lag demand
- Seven-day rolling average
- Day of week
- Month
are used to predict future daily demand.
Model performance is evaluated using:
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
### K-Means Clustering
K-Means clustering is used to group products according to their sales characteristics.
The clustering features include:
- Total units sold
- Total revenue
- Number of orders
- Average units per transaction
This can help logistics managers apply different inventory strategies to different product groups.
### Inventory Planning
Basic inventory calculations are also demonstrated.
Safety stock is estimated using demand variability and an assumed service-level z-score.
The reorder point is calculated using:
**Reorder Point = Average Daily Demand × Lead Time + Safety Stock**
A seven-day lead time is used as an assumption because supplier lead-time information is not available in the dataset.
## Technologies Used
The project is developed using Python.
Main libraries include:
- pandas
- NumPy
- Matplotlib
- scikit-learn
- openpyxl
The project is developed and executed using Visual Studio Code.
## Expected Outcomes
The analysis is expected to provide:
- A better understanding of historical demand.
- Identification of high-demand products.
- Useful logistics KPIs.
- A basic demand forecasting model.
- Product segments based on sales behavior.
- Illustrative safety-stock and reorder-point values.
- A foundation for future logistics optimization.
## Business Impact
The analysis demonstrates how data science can support logistics decision-making.
The results could help a logistics organization:
- Prioritize high-demand products.
- Improve replenishment planning.
- Reduce the risk of stockouts.
- Reduce unnecessary inventory.
- Improve warehouse resource allocation.
- Understand demand variability.
- Support short-term demand forecasting.
## Limitations
The project has several limitations.
The Online Retail dataset does not contain complete logistics information such as:
- Current inventory levels
- Supplier lead times
- Warehouse capacity
- Transportation costs
- Stockout information
- Purchase orders
- Supplier reliability
Therefore, some calculations are illustrative and rely on stated assumptions.
A future version of the project could integrate these additional datasets to create a more advanced logistics optimization system.
## Week 1 Conclusion
Week 1 establishes the foundation for the overall Logistics Data Analysis project.
The project demonstrates the complete initial analytical workflow from data collection and cleaning to exploratory analysis,
KPI calculation, predictive modeling, product clustering, and inventory planning.
The work completed in Week 1 will provide the foundation for the subsequent weeks of the project, where the analysis can be expanded and improved.

Project: Logistics Data Analysis

Week: 1

# Week 2 – Data Collection, Cleaning, and Preprocessing

## Overview

Week 2 focused on preparing the Online Retail dataset for further logistics analysis. The main objective was to identify and resolve common data-quality problems and create a cleaner and more reliable dataset for future analysis and machine-learning applications.

## Objectives

- Load and inspect the dataset.
- Identify missing values.
- Detect and remove duplicate records.
- Identify potential invalid values.
- Detect outliers using the IQR method.
- Handle extreme quantity values.
- Create a Revenue variable.
- Normalize numerical variables.
- Validate the cleaned dataset.
- Save the processed dataset for future analysis.

## Dataset

The project uses the Online Retail dataset containing transaction-level records from a UK-based online retailer.

The original dataset contains information such as:

- Invoice number
- Product code
- Product description
- Quantity
- Invoice date
- Unit price
- Customer ID
- Country

These variables can be used to study demand, product activity, sales value, and geographic patterns relevant to logistics analysis.

## Data Cleaning Process

The following preprocessing steps were completed:

1. Loaded the Excel dataset using Pandas.
2. Inspected the dataset structure.
3. Checked for missing values.
4. Checked for duplicate records.
5. Removed exact duplicate rows.
6. Handled missing values in important fields.
7. Detected quantity outliers using the IQR method.
8. Capped extreme quantity values.
9. Performed a data-quality validation.
10. Created a Revenue variable.
11. Normalized numerical variables using StandardScaler.
12. Saved the cleaned dataset.
13. Created a preprocessing summary.
14. Performed final validation.

## Outlier Detection

The Interquartile Range (IQR) method was used to identify unusually large values in the Quantity column.

The IQR is calculated as:

IQR = Q3 - Q1

Potential outliers were identified using:

Lower Limit = Q1 - 1.5 × IQR

Upper Limit = Q3 + 1.5 × IQR

Extreme quantity values were capped rather than automatically deleted because unusually large transactions may represent legitimate bulk orders.

## Revenue Calculation

A new Revenue variable was created using:

Revenue = Quantity × UnitPrice

This provides a financial measure that can be analyzed alongside physical demand.

## Normalization

The following numerical variables were normalized:

- Quantity
- UnitPrice
- Revenue

The `StandardScaler` technique from Scikit-learn was used to standardize the variables.

This is useful for future machine-learning techniques where variables with different scales can affect the results.

## Tools Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Excel
- Visual Studio Code

## Files

- `week 2.py` – Complete Week 2 preprocessing code.
- `cleaned_logistics_data.csv` – Cleaned and preprocessed dataset.
- `preprocessing_summary.csv` – Summary of the preprocessing results.
- `Week2_Logistics_Data_Cleaning_Preprocessing_Report.docx` – Detailed Week 2 report.

## Outcome

At the end of Week 2, the dataset was cleaned, transformed, normalized, and validated. 
The resulting dataset provides a stronger foundation for future logistics analysis such as demand forecasting, inventory analysis, customer segmentation, and optimization.

# Week 3 - Advanced Data Analysis and Visualization in Logistics

## Overview

Week 3 focused on advanced data analysis and visualization for logistics using Python.
The main objective was to explore a hypothetical logistics dataset, perform exploratory data analysis (EDA),
create meaningful visualizations, identify relationships between logistics variables, and generate practical insights for data-driven decision-making.
A simulated dataset containing 500 shipments was created using Python, NumPy, and Pandas.
The dataset included delivery time, shipment volume, transportation cost, distance, and fuel cost.

## Objectives
The main objectives of Week 3 were:

- Create a hypothetical logistics dataset.
- Inspect and validate the dataset.
- Perform exploratory data analysis.
- Calculate descriptive statistics.
- Analyze delivery-time patterns.
- Analyze shipment-volume patterns.
- Analyze transportation costs.
- Create logistics visualizations.
- Perform correlation analysis.
- Identify potential logistics cost drivers.
- Generate operational insights and recommendations.

## Dataset
The dataset contains 500 simulated shipments with the following variables:


## Tools and Technologies

The following tools and Python libraries were used:

- Python
- Pandas
- NumPy
- Matplotlib
- Visual Studio Code
- CSV files
- 
### 1. Dataset Creation
A hypothetical logistics dataset containing 500 shipments was created using NumPy and Pandas.

### 2. Data Inspection

The dataset was examined using:

- Dataset shape
- Column names
- Data types
- First and last records
- Dataset information

### 3. Data Quality Checking

The following checks were performed:
- Missing values
- Duplicate records
- Negative numerical values
These checks help ensure that the dataset is suitable for analysis.

### 4. Descriptive Statistics

Descriptive statistics were calculated for the numerical variables, including:
- Mean
- Median
- Standard deviation
- Minimum
- Maximum
- Quartiles
These statistics provide an overview of logistics performance and variation.

### 5. Delivery-Time Analysis

Delivery time was analyzed using mean, median, minimum, maximum, and percentiles.
This analysis helps identify typical delivery performance and possible delays or bottlenecks.

### 6. Shipment-Volume Analysis

Shipment volume was analyzed to understand typical shipment sizes and variation.
This information can support:
- Vehicle capacity planning
- Warehouse planning
- Shipment consolidation
- Transportation planning

### 7. Transportation-Cost Analysis

Transportation costs were analyzed using descriptive statistics and percentiles.
This helps identify the normal range of transportation expenses and potentially expensive shipments.

## Visualizations

Three main visualizations were created using Matplotlib.

### Delivery-Time Distribution

A histogram was created to show how delivery times are distributed across shipments.

### Shipment-Volume Distribution

A histogram was created to show the distribution of shipment volumes.

### Transportation-Cost Distribution

A histogram was created to show the distribution of transportation costs.

## Correlation Analysis

A correlation matrix was created to study relationships between:
- Delivery Time
- Shipment Volume
- Transportation Cost
- Distance
- Fuel Cost
- 
Correlation analysis helps identify variables that may be related to transportation costs and operational performance.
The analysis also demonstrates that correlation can identify relationships,
that require further investigation, although correlation alone does not prove causation.

Week 2 demonstrated that data quality is essential for reliable logistics analytics. Missing values, duplicates, invalid values, and extreme observations can affect calculations and decision-making. A structured preprocessing pipeline helps ensure that future analysis is based on more reliable and consistent data.

# Week 3 - Advanced Data Analysis and Visualization in Logistics

## Overview

Week 3 focused on advanced data analysis and visualization for logistics using Python. The main objective was to explore a hypothetical logistics dataset, perform exploratory data analysis (EDA), create meaningful visualizations, identify relationships between logistics variables, and generate practical insights for data-driven decision-making.
A simulated dataset containing 500 shipments was created using Python, NumPy, and Pandas. The dataset included delivery time, shipment volume, transportation cost, distance, and fuel cost.

## Objectives

The main objectives of Week 3 were:

- Create a hypothetical logistics dataset.
- Inspect and validate the dataset.
- Perform exploratory data analysis.
- Calculate descriptive statistics.
- Analyze delivery-time patterns.
- Analyze shipment-volume patterns.
- Analyze transportation costs.
- Create logistics visualizations.
- Perform correlation analysis.
- Identify potential logistics cost drivers.
- Generate operational insights and recommendations.

## Dataset

The dataset contains 500 simulated shipments with the following variables:

## Tools and Technologies
The following tools and Python libraries were used:
- Python
- Pandas
- NumPy
- Matplotlib
- Visual Studio Code
- CSV files

## Analysis Performed

### 1. Dataset Creation

A hypothetical logistics dataset containing 500 shipments was created using NumPy and Pandas.

### 2. Data Inspection

The dataset was examined using:

- Dataset shape
- Column names
- Data types
- First and last records
- Dataset information

### 3. Data Quality Checking

The following checks were performed:

- Missing values
- Duplicate records
- Negative numerical values

These checks help ensure that the dataset is suitable for analysis.

### 4. Descriptive Statistics

Descriptive statistics were calculated for the numerical variables, including:

- Mean
- Median
- Standard deviation
- Minimum
- Maximum
- Quartiles

These statistics provide an overview of logistics performance and variation.

### 5. Delivery-Time Analysis

Delivery time was analyzed using mean, median, minimum, maximum, and percentiles.

This analysis helps identify typical delivery performance and possible delays or bottlenecks.

### 6. Shipment-Volume Analysis

Shipment volume was analyzed to understand typical shipment sizes and variation.

This information can support:

- Vehicle capacity planning
- Warehouse planning
- Shipment consolidation
- Transportation planning

### 7. Transportation-Cost Analysis

Transportation costs were analyzed using descriptive statistics and percentiles.

This helps identify the normal range of transportation expenses and potentially expensive shipments.

## Visualizations

Three main visualizations were created using Matplotlib.

### Delivery-Time Distribution

A histogram was created to show how delivery times are distributed across shipments.

### Shipment-Volume Distribution

A histogram was created to show the distribution of shipment volumes.

### Transportation-Cost Distribution

A histogram was created to show the distribution of transportation costs.


## Correlation Analysis

A correlation matrix was created to study relationships between:

- Delivery Time
- Shipment Volume
- Transportation Cost
- Distance
- Fuel Cost
Correlation analysis helps identify variables that may be related to transportation costs and operational performance.

## Key Insights

The analysis provides a foundation for understanding logistics operations.
Important areas investigated include:
- Delivery-time consistency
- Shipment-volume variation
- Transportation-cost variation
- Distance as a potential cost driver
- Fuel cost as a potential cost driver
- Relationships between shipment characteristics and logistics costs

The analysis also demonstrates that correlation can identify relationships that require further investigation,
although correlation alone does not prove causation.

# Week 4 - Predictive Modeling and Optimization in Logistics Systems

## Overview

Week 4 focused on applying predictive modeling and optimization techniques to logistics operations using Python. The main objective was to build models that predict delivery time, evaluate their performance, identify important factors, and use the results to suggest practical logistics optimization strategies.

A simulated dataset containing 500 shipments was created. The analysis used shipment volume, transportation distance, transportation cost, and fuel cost as predictive features, while delivery time was used as the target variable.

## Objectives

The main objectives of Week 4 were:

- Define a logistics prediction problem.
- Create a simulated logistics dataset.
- Prepare features and the target variable.
- Split data into training and testing sets.
- Build predictive models.
- Evaluate model performance.
- Compare different machine-learning models.
- Perform cross-validation.
- Analyze feature importance.
- Develop logistics optimization recommendations.

## Dataset

The dataset contains 500 simulated shipment records.

| Variable | Description |
|---|---|
| Shipment_ID | Unique identification number for each shipment |
| Shipment_Volume_kg | Shipment volume in kilograms |
| Distance_km | Transportation distance |
| Transportation_Cost | Cost associated with transportation |
| Fuel_Cost | Fuel-related transportation cost |
| Delivery_Time_Days | Delivery time in days and prediction target |

## Prediction Problem

The main prediction problem was:

> **Predict delivery time in days using logistics-related variables.**

The input features used by the models were:

- Shipment Volume
- Distance
- Transportation Cost
- Fuel Cost

The target variable was:

`Delivery_Time_Days`

## Methodology

### 1. Dataset Creation

A hypothetical dataset containing 500 shipments was generated using NumPy and Pandas.

A random seed of `42` was used to make the results reproducible.

### 2. Dataset Inspection

The dataset was checked for:

- Number of rows and columns
- Column names
- Data types
- Missing values
- Duplicate records
- Sample records

The dataset contained 500 rows and 6 columns.

### 3. Feature and Target Preparation

The following variables were selected as features:

```text
Shipment_Volume_kg
Distance_km
Transportation_Cost
Fuel_Cost

