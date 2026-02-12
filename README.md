# Student Performance Prediction

A Django-based machine learning application that predicts student academic performance using a Random Forest regression model.

## Overview

This project combines Django REST Framework with scikit-learn to create an intelligent prediction system for student performance. Users can input various academic and lifestyle factors to receive an estimated performance index score.

## Features

- **Machine Learning Model**: Trained Random Forest Regressor with 200 estimators
- **REST API**: POST endpoint for performance predictions with data validation
- **Web Interface**: HTML template for interactive predictions
- **Data Validation**: Input validation using Django serializers
- **Persistent Model Storage**: Trained model saved as a pickle file for quick loading

## Project Structure

```
student-performance-prediction/
├── student_ml/                    # Django project root
│   ├── performance/              # Main application
│   │   ├── models.py            # StudentPerformance model with validation
│   │   ├── views.py             # API views and home page
│   │   ├── serializers.py       # DRF serializers for validation
│   │   ├── train_model.py       # Model training script
│   │   ├── dataset.csv          # Training dataset
│   │   ├── model.pkl            # Trained model (generated)
│   │   ├── urls.py              # URL routing
│   │   ├── templates/
│   │   │   └── predict.html     # Web interface
│   │   └── migrations/          # Database migrations
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── db.sqlite3
```

## Prerequisites

- Python 3.8+
- Django 3.2+
- djangorestframework
- scikit-learn
- pandas
- joblib
- numpy

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd student-performance-prediction
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Train the model** (if model.pkl doesn't exist)
   ```bash
   python manage.py shell
   ```
   Then run:
   ```python
   from performance.train_model import train
   train()
   ```

5. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

The application will be available at `http://localhost:8000/`

## Usage

### Web Interface

Navigate to `http://localhost:8000/` to access the interactive prediction form. Fill in the student information and submit to get a performance prediction.

### REST API

**Endpoint:** `POST /api/predict/`

**Request body:**
```json
{
  "hours_studied": 7,
  "previous_scores": 85,
  "extracurricular": true,
  "sleep_hours": 8,
  "sample_papers": 5
}
```

**Response:**
```json
{
  "predicted_performance_index": 89.45
}
```

## Data Features

The model uses the following input features:

| Feature | Type | Description |
|---------|------|-------------|
| `hours_studied` | Integer | Total hours spent studying |
| `previous_scores` | Integer | Student's previous test scores |
| `extracurricular` | Boolean | Participation in extracurricular activities |
| `sleep_hours` | Integer | Average hours of sleep per night |
| `sample_papers` | Integer | Number of sample papers solved |

**Validation:** Total hours studied + sleep hours cannot exceed 24 hours per day

**Output:** `performance_index` - Float value representing predicted student performance (typically 0-100)

## Model Details

- **Algorithm**: Random Forest Regressor
- **Number of Estimators**: 200
- **Test Size**: 20% of data
- **Random State**: 42 (for reproducibility)
- **Model File**: `performance/model.pkl`

## Data Validation

The application includes robust validation:
- All input fields are required
- Integer fields are validated for positive values
- The `StudentPerformance` model includes a custom `clean()` method to ensure realistic time constraints
- DRF serializers validate incoming API requests

## API Errors

- **400 Bad Request**: Invalid input data (validation errors detailed in response)
- **500 Server Error**: Model loading or prediction failure

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is provided as-is for educational purposes.

## Author

Created by [Your Name]

---

For questions or issues, please open a GitHub issue.
