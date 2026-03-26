# House Price Predictor

A full-stack web application for predicting house prices using machine learning. The project consists of a Next.js frontend and a Python Flask backend with a trained ML model.

## Features

- **Frontend**: Built with Next.js, providing a user-friendly interface for inputting house details and displaying predictions.
- **Backend**: Python Flask API that serves the ML model for price predictions.
- **ML Model**: Trained model using scikit-learn, saved as a joblib file for efficient loading.

## Project Structure

```
.
├── backend/
│   ├── api.py              # Flask API for predictions
│   ├── predict.py          # Prediction logic
│   ├── house_price_predictor.joblib  # Trained ML model
│   └── data.csv            # Dataset used for training
├── house/                  # Next.js frontend application
│   ├── app/
│   │   ├── components/
│   │   │   ├── Header.tsx
│   │   │   └── body.tsx
│   │   ├── globals.css
│   │   ├── layout.tsx
│   │   └── page.tsx
│   ├── package.json
│   └── ...
└── README.md
```

## Prerequisites

- Node.js (for frontend)
- Python 3.8+ (for backend)
- Git

## Installation and Setup

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install Python dependencies:
   ```bash
   pip install flask scikit-learn pandas joblib
   ```

3. Run the backend server:
   ```bash
   python api.py
   ```
   The API will be available at `http://localhost:5000`.

### Frontend Setup

1. Navigate to the house directory:
   ```bash
   cd house
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

3. Run the development server:
   ```bash
   npm run dev
   ```
   The frontend will be available at `http://localhost:3000`.

## Usage

1. Start both the backend and frontend servers as described above.
2. Open your browser and go to `http://localhost:3000`.
3. Enter the house details in the form.
4. Click "Predict" to get the estimated house price.

## API Endpoints

- `POST /predict`: Accepts house features as JSON and returns the predicted price.

Example request:
```json
{
  "feature1": value1,
  "feature2": value2,
  ...
}
```

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Make your changes and commit: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License.