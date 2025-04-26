# 🚗 Traffic Volume Prediction using Decision Trees

This project focuses on **predicting vehicle traffic volume** at city junctions using a combination of **feature engineering** and **machine learning models** 
It includes **data preprocessing, feature selection, model training, evaluation, and model saving.**

--

# 📂 Project Structure
- **Train.csv** - Training data with traffic volume at different junctions.

- **Test.csv** - Test data where traffic needs to be predicted.

- **vehicle_model.pkl** - Trained model file saved for future use.

# 🔧 Features & Techniques Used

- **Feature Engineering:**

- Extracting year, month, day, weekday, time, week, quarter from timestamps.

- Converting datetime to UNIX time.

- **Feature Importance:** Using ExtraTreesClassifier to rank features.

- **Modeling:** DecisionTreeClassifier for training and prediction.

- **Evaluation:** Calculated MAE, MSE, and RMSE scores.

- **Model Deployment:** Saved trained model using Joblib.


# 📊 Data Preprocessing

- **DateTime Parsing:** Convert DateTime columns from string to Python datetime objects.

- **Feature Extraction:** Year, Month, Day, Hour, Weekday, Week, Quarter

- **UNIX Timestamp:** DateTime converted to seconds for model training.

# 🧠 Model Training

- **Feature Selection:** ExtraTreesClassifier is used to find the most important features.

- **Model:** DecisionTreeClassifier is trained with the processed features.

- **Evaluation Metrics:**

- MAE (Mean Absolute Error)

- MSE (Mean Squared Error)

- RMSE (Root Mean Squared Error)

Example Output:
```bash
MAE: 8.31
MSE: 134.72
RMSE: 11.61
``

# 📈 Visualizations

- Feature Importance Bar Chart

- Traffic Volume Histogram

- Traffic Trends by Junctions

# 💾 Saving the Model
After training, the Decision Tree Regressor model is saved using Joblib:
```bash
import joblib
joblib.dump(model, "vehicle_model.pkl")
```

# 📦 How the Prediction Works
1.Preprocess the test data with the same transformations as training.

2.Load the trained model (vehicle_model.pkl).

3.Predict the vehicle volume for unseen data.

4.Combine and plot the predictions.

# 🛠 Requirements
- Python 3.8+

- Libraries:
```bash
- pandas

- numpy

- matplotlib

- scikit-learn

- joblib
```

# 📜 Important Notes

- Always ensure that the datetime columns are parsed correctly.

- Make sure that feature engineering steps match exactly between train and test datasets.

- Set the same random seeds (e.g., random_state=42) to reproduce results.

# 🤝 Contributions
- Feel free to fork, improve, and submit pull requests to enhance this project!

# ✨ Acknowledgements
Special thanks to:

- Scikit-learn developers for easy-to-use ML APIs.

- Kaggle and open datasets for real-world traffic data inspiration.
