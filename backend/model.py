import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib

# Load dataset
df = pd.read_csv("dataset.csv")

# Show column names
print("Columns in Dataset:")
print(df.columns)

# Show first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Features
X = df.drop("Performance Index", axis=1)

# Target
y = df["Performance Index"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = RandomForestRegressor()

# Train model
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
mae = mean_absolute_error(y_test, predictions)

print("\nMean Absolute Error:", mae)

# Save model
joblib.dump(model, "student_model.pkl")

print("\nModel saved successfully!")






