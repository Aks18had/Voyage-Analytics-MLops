# ✈️ Voyage Analytics: Productionization of ML Systems

## 📌 Project Overview

This project focuses on building and productionizing machine learning models in the travel and tourism domain. It demonstrates an end-to-end MLOps pipeline, including model development, deployment, automation, and scalability.

---

## 🎯 Objectives

* Predict flight prices using regression models
* Classify user gender using demographic data
* Recommend hotels based on user preferences
* Deploy models using modern MLOps practices

---

## 📊 Datasets Used

* **Users Dataset** – demographic details (age, company, gender)
* **Flights Dataset** – flight details (distance, type, agency, price)
* **Hotels Dataset** – booking details (place, price, duration)

---

## 🤖 Machine Learning Models

### 🔹 Flight Price Prediction (Regression)

* Models Used:

  * Linear Regression
  * Random Forest (Final Model)
  * XGBoost
* **Best Performance (Random Forest):**

  * R² Score: ~0.99
  * RMSE: ~0.75

---

### 🔹 Gender Classification (Classification)

* Model Used:

  * Random Forest Classifier
* **Performance:**

  * Accuracy: (add your actual accuracy here, e.g., ~85–95%)

---

### 🔹 Hotel Recommendation System

* Approach:

  * Content-based filtering
* Logic:

  * Recommends hotels based on user booking history and preferences

---

## ⚙️ MLOps Stack

| Component      | Purpose              |
| -------------- | -------------------- |
| Flask          | Model API serving    |
| Streamlit      | User interface       |
| MLflow         | Experiment tracking  |
| Docker         | Containerization     |
| Kubernetes     | Deployment & scaling |
| Apache Airflow | Workflow automation  |
| Jenkins        | CI/CD pipeline       |

---

## 🏗️ Project Structure

```
Voyage-Analytics-MLops/
│
├── notebooks/
├── models/
├── api/
├── streamlit_app/
├── docker/
├── airflow/
├── deployment.yml
├── Jenkinsfile
└── README.md
```

---

## 🚀 How to Run Locally

### 1. Clone the Repository

```
git clone https://github.com/yourusername/Voyage-Analytics-MLops
cd Voyage-Analytics-MLops
```

### 2. Install Dependencies

```
pip install streamlit flask joblib numpy scikit-learn
```

### 3. Run Streamlit App

```
cd streamlit_app
streamlit run app.py
```

### 4. Run Flask API

```
cd api
python app.py
```

---

## 🌐 Key Features

* End-to-end ML pipeline
* Real-time prediction using API
* User-friendly dashboard
* Scalable deployment design
* Automated workflow simulation

---

## 📈 Business Impact

* Helps travel platforms estimate flight pricing
* Enables user segmentation through classification
* Improves customer experience via recommendations

---

## 🔮 Future Improvements

* Add real-time model monitoring
* Implement automated retraining pipelines
* Enhance recommendation system using collaborative filtering
* Deploy on cloud platforms (AWS/GCP/Azure)

---

## 👨‍💻 Author

**Akshad Goyanka**
