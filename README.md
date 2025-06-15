# 🚛 Freight Delay Prediction using Machine Learning

This project uses a Machine Learning model to predict whether a freight shipment will be **delayed** or **delivered on time**.
It simulates real-world logistics data and provides actionable insights for supply chain optimization.

---

## 📌 Problem Statement

Freight delays cost businesses millions. This project helps supply chain professionals:
- Predict shipment delays based on traffic, weather, vehicle type, and more
- Take proactive actions to avoid missed deliveries
- Improve customer satisfaction and logistics efficiency

---

## 💡 Key Features

- ✅ Simulated logistics dataset with 1000+ shipment records
- ✅ Delay predictions using Random Forest Classifier
- ✅ Feature importance analysis
- ✅ Streamlit web app for real-time predictions
- ✅ Ready for deployment via GitHub & Streamlit Cloud

---

## 🧪 Dataset Columns

| Column Name          | Description                        |
|----------------------|------------------------------------|
| shipment_id          | Unique ID for shipment             |
| origin / destination | Cities involved in transport       |
| distance_km          | Total shipment distance in KM      |
| weight_kg            | Shipment weight                    |
| shipment_date        | Date of shipment                   |
| carrier_name         | Carrier (DHL, FedEx, etc.)         |
| vehicle_type         | Vehicle used for transport         |
| weather_condition    | Weather at shipment time           |
| traffic_condition    | Road traffic level                 |
| delay (target)       | 1 = Delayed, 0 = On-time           |

---

## 🧠 Model Performance

- Model Used: `RandomForestClassifier`
- Accuracy: ~87%
- Evaluation: Confusion Matrix + Classification Report
