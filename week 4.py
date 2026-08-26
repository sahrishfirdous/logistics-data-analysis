import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

print("Week 4 - Predictive Modeling and Optimization")
print("Libraries imported successfully.")

print("\nStep 2: Creating logistics prediction dataset")

np.random.seed(42)

number_of_shipments = 500

week4_data = pd.DataFrame({
    "Shipment_ID": range(1, number_of_shipments + 1),
    "Shipment_Volume_kg": np.random.normal(250, 80, number_of_shipments),
    "Distance_km": np.random.normal(450, 150, number_of_shipments),
    "Transportation_Cost": np.random.normal(500, 150, number_of_shipments),
    "Fuel_Cost": np.random.normal(180, 60, number_of_shipments)
})

week4_data["Shipment_Volume_kg"] = week4_data["Shipment_Volume_kg"].clip(lower=20)
week4_data["Distance_km"] = week4_data["Distance_km"].clip(lower=50)
week4_data["Transportation_Cost"] = week4_data["Transportation_Cost"].clip(lower=50)
week4_data["Fuel_Cost"] = week4_data["Fuel_Cost"].clip(lower=20)

week4_data["Delivery_Time_Days"] = (
    2
    + (week4_data["Distance_km"] / 200)
    + (week4_data["Shipment_Volume_kg"] / 500)
    + (week4_data["Fuel_Cost"] / 500)
    + np.random.normal(0, 0.5, number_of_shipments)
)

week4_data["Delivery_Time_Days"] = week4_data["Delivery_Time_Days"].clip(lower=1)

print("Logistics prediction dataset created successfully.")
print("Number of shipments:", len(week4_data))
print("Number of columns:", len(week4_data.columns))

print("\nFirst 5 shipments:")
print(week4_data.head())

print("\nStep 3: Inspecting the logistics prediction dataset")

print("\nDataset shape:")
print(week4_data.shape)

print("\nColumn names:")
print(week4_data.columns.tolist())

print("\nData types:")
print(week4_data.dtypes)

print("\nFirst 10 rows:")
print(week4_data.head(10))

print("\nMissing values:")
print(week4_data.isnull().sum())

print("\nDuplicate rows:")
print(week4_data.duplicated().sum())

print("\nStep 4: Preparing features and target")

features = [
    "Shipment_Volume_kg",
    "Distance_km",
    "Transportation_Cost",
    "Fuel_Cost"
]

X = week4_data[features]
y = week4_data["Delivery_Time_Days"]

print("\nFeatures used by the models:")
print(features)

print("\nTarget variable:")
print("Delivery_Time_Days")

print("\nFeature dataset shape:")
print(X.shape)

print("\nTarget dataset shape:")
print(y.shape)

print("\nFirst 5 feature rows:")
print(X.head())

print("\nFirst 5 target values:")
print(y.head())

print("\nStep 5: Splitting data into training and testing sets")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining feature data shape:")
print(X_train.shape)

print("\nTesting feature data shape:")
print(X_test.shape)

print("\nTraining target data shape:")
print(y_train.shape)

print("\nTesting target data shape:")
print(y_test.shape)

print("\nData split completed successfully.")

print("\nStep 6: Training the Linear Regression model")

linear_model = LinearRegression()

linear_model.fit(X_train, y_train)

print("Linear Regression model trained successfully.")

print("\nModel coefficients:")
for feature, coefficient in zip(features, linear_model.coef_):
    print(feature, ":", round(coefficient, 4))

print("\nModel intercept:")
print(round(linear_model.intercept_, 4))

print("\nStep 7: Making delivery-time predictions")

linear_predictions = linear_model.predict(X_test)

print("Predictions generated successfully.")

print("\nFirst 10 actual delivery times:")
print(y_test.head(10).values)

print("\nFirst 10 predicted delivery times:")
print(linear_predictions[:10])

prediction_results = pd.DataFrame({
    "Actual_Delivery_Time": y_test.values,
    "Predicted_Delivery_Time": linear_predictions
})

print("\nPrediction results:")
print(prediction_results.head(10))

print("\nStep 8: Evaluating the Linear Regression model")

mae = mean_absolute_error(y_test, linear_predictions)

rmse = np.sqrt(mean_squared_error(y_test, linear_predictions))

r2 = r2_score(y_test, linear_predictions)

print("\nModel Performance:")
print("MAE:", round(mae, 4), "days")
print("RMSE:", round(rmse, 4), "days")
print("R-squared:", round(r2, 4))

print("\nStep 9: Training the Decision Tree model")

decision_tree_model = DecisionTreeRegressor(
    max_depth=5,
    random_state=42
)

decision_tree_model.fit(X_train, y_train)

print("Decision Tree model trained successfully.")

tree_predictions = decision_tree_model.predict(X_test)

print("\nFirst 10 Decision Tree predictions:")
print(tree_predictions[:10])

print("\nStep 10: Comparing predictive models")

tree_mae = mean_absolute_error(y_test, tree_predictions)

tree_rmse = np.sqrt(
    mean_squared_error(y_test, tree_predictions)
)

tree_r2 = r2_score(y_test, tree_predictions)

model_comparison = pd.DataFrame({
    "Model": [
        "Linear Regression",
        "Decision Tree"
    ],
    "MAE": [
        mae,
        tree_mae
    ],
    "RMSE": [
        rmse,
        tree_rmse
    ],
    "R2": [
        r2,
        tree_r2
    ]
})

print("\nModel Performance Comparison:")
print(model_comparison)

model_comparison.to_csv(
    "model_comparison.csv",
    index=False
)

print("\nModel comparison saved successfully.")

print("\nStep 11: Performing 5-fold cross-validation")

linear_cv_scores = cross_val_score(
    linear_model,
    X_train,
    y_train,
    cv=5,
    scoring="neg_mean_absolute_error"
)

tree_cv_scores = cross_val_score(
    decision_tree_model,
    X_train,
    y_train,
    cv=5,
    scoring="neg_mean_absolute_error"
)

linear_cv_mae = -linear_cv_scores.mean()
tree_cv_mae = -tree_cv_scores.mean()

print("\nLinear Regression cross-validation MAE:")
print(round(linear_cv_mae, 4), "days")

print("\nDecision Tree cross-validation MAE:")
print(round(tree_cv_mae, 4), "days")

print("\nCross-validation completed successfully.")

print("\nStep 12: Analyzing feature importance")

feature_importance = pd.DataFrame({
    "Feature": features,
    "Importance": decision_tree_model.feature_importances_
})

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature importance:")
print(feature_importance)

feature_importance.to_csv(
    "feature_importance.csv",
    index=False
)

print("\nFeature importance saved successfully.")

print("\nStep 13: Generating logistics optimization recommendations")

print("\n--- Optimization Recommendations ---")

top_feature = feature_importance.iloc[0]["Feature"]

print("\nMost important predictive factor:")
print(top_feature)

if top_feature == "Distance_km":
    print(
        "Recommendation: Optimize route planning and shipment consolidation "
        "to reduce unnecessary transportation distance."
    )

elif top_feature == "Shipment_Volume_kg":
    print(
        "Recommendation: Improve shipment consolidation and vehicle-capacity "
        "planning to manage shipment volume efficiently."
    )

elif top_feature == "Transportation_Cost":
    print(
        "Recommendation: Compare transportation providers and optimize "
        "cost-effective route and carrier selection."
    )

elif top_feature == "Fuel_Cost":
    print(
        "Recommendation: Improve fuel efficiency through route optimization, "
        "vehicle maintenance, and efficient vehicle utilization."
    )

print(
    "\nGeneral recommendation: Use predictive delivery-time estimates "
    "to identify shipments that may require additional monitoring."
)

print(
    "Optimization recommendations generated successfully."
)

print("\nStep 14: Final validation and saving results")

prediction_results = pd.DataFrame({
    "Shipment_ID": week4_data.loc[X_test.index, "Shipment_ID"].values,
    "Actual_Delivery_Time": y_test.values,
    "Predicted_Delivery_Time": linear_predictions
})

prediction_results.to_csv(
    "week4_predictions.csv",
    index=False
)

week4_data.to_csv(
    "week4_logistics_data.csv",
    index=False
)

print("\nFinal dataset shape:")
print(week4_data.shape)

print("\nPrediction results shape:")
print(prediction_results.shape)

print("\nFinal missing-value check:")
print(week4_data.isnull().sum())

print("\nFinal duplicate check:")
print(week4_data.duplicated().sum())

print("\nFiles created:")
print("- week4_logistics_data.csv")
print("- week4_predictions.csv")
print("- model_comparison.csv")
print("- feature_importance.csv")

print("\nWeek 4 predictive modeling and optimization completed successfully.")