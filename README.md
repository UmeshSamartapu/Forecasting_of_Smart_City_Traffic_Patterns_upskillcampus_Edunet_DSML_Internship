# Smart City Traffic Forecasting🚦

## Overview

The **Smart City Traffic Forecasting** project aims to predict traffic volume patterns at key city junctions using machine learning. This tool is designed to help city planners and traffic authorities with infrastructure planning and efficient traffic management. The model predicts the expected traffic volume based on various parameters such as the hour of the day, the day of the week, whether it's a weekend, and the month of the year.

👉 **([Click here to try the app](https://forecasting-of-smart-city-traffic.onrender.com/))**

## Features

- Predicts traffic volumes at specific junctions based on time, day, and other parameters.
- Utilizes machine learning models to provide real-time traffic volume predictions.
- User-friendly interface for entering traffic prediction parameters.
- Deployment-ready as a web service for easy integration into smart city applications.

## Tools & Technologies

- **Machine Learning**: Python (scikit-learn, XGBoost, etc.)
- **Backend**: FastAPI (for creating APIs)
- **Frontend**: HTML, CSS, JavaScript (for the user interface)
- **Deployment**: Render (for hosting the API)
- **Version Control**: Git, GitHub
- **Data Science Libraries**: pandas, numpy, seaborn, matplotlib

## Getting Started

Follow the instructions below to set up the project locally.

### 1.Prerequisites

Make sure you have the following installed:

- Python 3.x
- Git
- Node.js (optional, for testing frontend locally)
- Docker (optional, for containerized setup)

### 2.Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/yourusername/smart-city-traffic-forecasting.git
cd smart-city-traffic-forecasting
```
## Backend Setup
### 1.Create a Virtual Environment:

Create and activate a virtual environment to manage dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows
```

### 2.Install Dependencies:

Install the required Python libraries:

```bash
pip install -r requirements.txt
Run the FastAPI Server:
```

Start the FastAPI server locally:

```bash
uvicorn main:app --reload
The API will be accessible at http://127.0.0.1:8000.
```

## 3.Frontend Setup

Description: Predicts the traffic volume based on input parameters.

Parameters:

```bash
Junction (int): The junction number (1–4)

Hour (int): Hour of the day (0–23)

DayOfWeek (int): Day of the week (0–6)

IsWeekend (int): 0 for weekdays, 1 for weekends

Month (int): Month of the year (1–12)
```

Response: A JSON object containing the predicted number of vehicles.

### Example Input:
```bash
{
  "Junction": 1,
  "Hour": 15,
  "DayOfWeek": 3,
  "IsWeekend": 0,
  "Month": 5
}
```

Running in Docker (Optional)
To run the project in a Docker container, follow these steps:

### Build Docker Image:

```bash
docker build -t traffic-forecasting .
Run Docker Container:
```

```bash
docker run -p 8000:8000 traffic-forecasting
The backend will be accessible at http://localhost:8000.
```

## Contributing
We welcome contributions! If you want to help improve the project, follow these steps:

- Fork the repository.

- Clone your fork to your local machine.

- Create a new branch for your feature or bug fix.

- Make your changes and commit them.

- Push your changes to your forked repository.

- Open a pull request.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments
- FastAPI

- scikit-learn

- XGBoost

- Render

Feel free to edit and customize this README to fit any further specific needs of your project!
