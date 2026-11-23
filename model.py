import pandas as pd
import joblib
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

project_dir = Path(__file__).resolve().parent

# Load Dataset
data = pd.read_csv(project_dir / "static" / "dataset" / "student.csv")

# Features and Target
X = data[[
    "Study_Hours",
    "Attendance",
    "Previous_Marks"
]]

y = data["Final_Marks"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluation
accuracy = r2_score(y_test, predictions)
error = mean_absolute_error(y_test, predictions)

# Save Model
joblib.dump(model, project_dir / "student_model.pkl")
print("AI Model Trained Successfully!")
print("R2 Score:", round(accuracy, 2))
print("Mean Absolute Error:", round(error, 2))
print("Model Saved Successfully!")