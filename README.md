# 🚖 Uber Fare Prediction and Streamlit Web Application

## Project Link : https://uberfarepredictionandappwebapplication-8rrbpyur2hvlrr3huhxoj2.streamlit.app/

## 🌟 Overview

This project aims to develop a machine learning model to predict Uber ride fares based on various features extracted from ride data. Additionally, it includes a Streamlit web application that allows users to input ride details and get fare estimates.

## 🛠️ Skills Acquired

- 🧹 Data Cleaning and Preprocessing
- 🔧 Feature Engineering
- 🔍 Exploratory Data Analysis (EDA)
- 📉 Regression Modeling
- ⚙️ Hyperparameter Tuning
- 📊 Model Evaluation
- 🌍 Geospatial Analysis
- ⏳ Time Series Analysis
- 🌐 Web Application Development with Streamlit
- ☁️ Deployment on Cloud Platforms (AWS)

## 🌍 Domain

Transportation, Data Science, Machine Learning, Web Development

## ❓ Problem Statement

Develop a machine learning model to predict the fare amount for Uber rides based on features from ride data. Create a Streamlit web application that enables users to input ride details and obtain fare estimates.

## 💼 Business Use Cases

- **Ride Fare Estimation:** Provide fare estimates before booking rides. 🚖
- **Dynamic Pricing:** Adjust fare estimates based on time of day, demand, etc. 📈
- **Resource Allocation:** Optimize fleet management by predicting high-demand areas and times. 🚗
- **User Engagement:** Enhance user experience with accurate fare predictions. ⭐

## 🛠️ Approach

1. **Upload Dataset:** Upload the dataset to an S3 bucket. ☁️
2. **Data Retrieval:** Retrieve the data from the S3 bucket. 📂
3. **Data Preprocessing:** Apply preprocessing techniques including handling null values and dtype conversion. 🔧
4. **Cloud Storage:** Push the cleaned data to an RDS server (MySQL) cloud database. 🗄️
5. **Data Retrieval from Cloud:** Retrieve the cleaned data from the cloud server. ☁️
6. **Model Training:** Train the machine learning model and save it. 📊
7. **Application Development:** Create an application for the saved model. 💻
8. **User Interface:** Develop a user interface for input and prediction. 🌐

## 🏆 Results

- **Trained Model:** A regression model capable of accurately predicting Uber ride fares. 📉
- **Web Application:** A functional Streamlit app for getting fare estimates based on ride details. 🌐
- **Evaluation Metrics:** Detailed performance metrics for the regression model. 📊

## 📊 Dataset

- **Source:** Uber ride data (CSV format) 📦
- **Variables:** key, fare_amount, pickup_datetime, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, passenger_count
- **Content:** Contains details of Uber rides, including fare amount, pickup/dropoff locations, ride datetime, and number of passengers.

## 🧹 Preprocessing Steps

- Handle missing values and outliers. 🛠️
- Extract features from pickup_datetime. 🕒
- Calculate trip distances. 📍
- Segment data based on time of day (morning, afternoon, evening, night). 🌅🌞🌆🌙
- Segment data based on passenger count (mini, XUV, premium XUV). 🚗🚙🚐

## 📝 Project Deliverables

- **Source Code:** Python scripts for data preprocessing, model training, and the Streamlit app. 💻
- **Documentation:** A detailed report explaining data analysis, model development, and deployment. 📄
- **Web Application:** Deployed Streamlit app accessible via a URL. 🌐

## 🚀 Getting Started

### Prerequisites

- Python 3.x 🐍
- Required Python libraries (listed in `requirements.txt`) 📋
- AWS account for S3 and RDS ☁️

### Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/SETHU0010/uber-fare-prediction.git
    ```
2. **Navigate to the Project Directory:**
    ```bash
    cd uber-fare-prediction
    ```
3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. **Upload Data to S3:**
   Follow the instructions in `data_upload_instructions.md`. 📥

2. **Run Data Preprocessing and Model Training:**
    ```bash
    python preprocess_and_train.py
    ```

3. **Run the Streamlit Application:**
    ```bash
    streamlit run app.py
    ```

### Deployment

The web application is deployed on AWS. You can access it [here](URL-to-your-deployed-app). 🌐

## 📋 Project Guidelines

- **Coding Standards:** Follow PEP 8 guidelines. 📜
- **Version Control:** Use Git for version control. Commit changes regularly. 🗂️
- **Documentation:** Ensure code is well-commented and provide clear instructions for running scripts and the application. 📝
- **Best Practices:** Validate models with cross-validation, ensure reproducibility, and handle data privacy appropriately. ✅


## 📫 Contact

For any questions or comments, please contact:

- **Email:** sethumadhavanvelu2002@gmail.com 📧
- **Phone:** 9159299878 📞
