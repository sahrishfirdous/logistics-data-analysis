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
## Project Structure
The Week 1 repository contains the main Python code, analysis outputs, and written report.
Example structure:
Week-1/
- week1.py
- logistics_kpi_results.csv
- Week1_Logistics_Strategic_Planning_Detailed_Report.docx
- README.md
The original Online Retail dataset is not included in the repository because of its file size and dataset distribution considerations.
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
