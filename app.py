import csv
import io
from pathlib import Path

import pandas as pd
import joblib
from flask import Flask, Response, render_template, request

app = Flask(__name__)

# Load trained AI model
project_dir = Path(__file__).resolve().parent
model = joblib.load(project_dir / "student_model.pkl")

# Load student dataset
data = pd.read_csv(project_dir / "static" / "dataset" / "student.csv")

# Calculate dashboard statistics
total_students = len(data)

average_marks = round(
    data["Final_Marks"].mean(), 2
)

average_attendance = round(
    data["Attendance"].mean(), 2
)

prediction_history = []


# Home Page
@app.route("/")
@app.route("/home")
def home():

    return render_template(
        "index.html",
        total_students=total_students,
        average_marks=average_marks,
        average_attendance=average_attendance
    )


# Student Performance Prediction
@app.route("/predict", methods=["POST"])
def predict():

    study_hours = float(request.form["study_hours"])

    attendance = float(request.form["attendance"])

    previous_marks = float(request.form["previous_marks"])

    prediction = model.predict(pd.DataFrame([{
        "Study_Hours": study_hours,
        "Attendance": attendance,
        "Previous_Marks": previous_marks
    }]))

    result = round(float(prediction[0]), 2)
    prediction_history.append({
        "Study Hours": study_hours,
        "Attendance": attendance,
        "Previous Marks": previous_marks,
        "Predicted Marks": result
    })

    return render_template(
        "index.html",
        prediction=result,
        total_students=total_students,
        average_marks=average_marks,
        average_attendance=average_attendance
    )


@app.route("/dashboard")
def dashboard():
    history = list(reversed(prediction_history[-10:]))
    predicted_marks = [item["Predicted Marks"] for item in prediction_history]

    return render_template(
        "dashboard.html",
        total_predictions=len(prediction_history),
        average_marks=round(sum(predicted_marks) / len(predicted_marks), 2)
        if predicted_marks else 0,
        highest_marks=max(predicted_marks) if predicted_marks else 0,
        history=history
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/download")
def download():
    output = io.StringIO()
    fieldnames = [
        "Study Hours",
        "Attendance",
        "Previous Marks",
        "Predicted Marks"
    ]
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(prediction_history)

    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={
            "Content-Disposition": "attachment; filename=prediction_history.csv"
        }
    )


# Run Flask Application
if __name__ == "__main__":
    app.run(debug=True)

    