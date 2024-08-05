import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sklearn



# title
st.title('🚖 Uber Fare Prediction and Streamlit Web Application 🌐')


# Load data
df = pd.read_csv('Clean_data.csv')
scale = pd.read_pickle('scale.pkl')
model = pd.read_pickle('model.pkl')


def Problem_Statement():
    st.header("📝 Problem Statement")
    st.write("Develop a machine learning model to predict Uber ride fares based on ride data features. Create a Streamlit web application that allows users to input ride details and receive a fare estimate.")

def objective():
    st.header("🎯 Objective")
    st.write("Develop an accurate regression model to predict Uber ride fares and create a Streamlit web app for users to estimate fares, deployed on AWS for scalability.")

def Domain():
    st.header("🌐 Domain")
    st.write("Transportation, Data Science, Machine Learning, Web Development")

def Approach():
    st.header("🔍 Approach")
    st.write("1. **Upload Data**: Upload the dataset to an S3 bucket. ☁️")
    st.write("2. **Data Retrieval**: Pull data from the S3 bucket. 🔄")
    st.write("3. **Preprocessing**: Perform data cleaning and preprocessing (handle null values, type conversion). 🧹")
    st.write("4. **Database Storage**: Push cleaned data to an RDS (MySQL) cloud database. ☁️")
    st.write("5. **Data Retrieval**: Pull cleaned data from the cloud server. 🔄")
    st.write("6. **Model Training**: Train the machine learning model and save it. 🏋️")
    st.write("7. **Application Development**: Create a web application for the saved model. 💻")
    st.write("8. **User Interface**: Develop a UI to input data for model predictions. 🖥️")

def Workflow():
    st.header("🔄 Workflow")
    st.write("""
    1. **Data Upload**: Upload dataset to an S3 bucket. ☁️
    2. **Preprocessing**: Clean and preprocess the data. 🧹
    3. **Model Training**: Train and save the regression model. 🏋️
    4. **Web Application Development**: Build and integrate the Streamlit app. 💻
    5. **Deployment**: Deploy the model and application on AWS. 🚀
    """)

def prerequisites():
    st.header("⚙️ Prerequisites")
    st.write("Before using the application, ensure you have the following prerequisites set up:")
    st.write("1. **Python Skills**: Data preprocessing, machine learning. 🐍")
    st.write("2. **Tools**: Pandas, NumPy, Scikit-learn, Streamlit. 🛠️")
    st.write("3. **AWS Knowledge**: S3, RDS, deployment. ☁️")
    st.write("4. **Data**: Uber ride dataset (CSV format). 📊")

def required_python_libraries():
    st.header("📚 Required Python Libraries")
    st.write("The following Python libraries are required for the project:")
    libraries = ["pandas", "streamlit", "boto3", "pickle5"]
    st.write("`" + ", ".join(libraries) + "`")

def Dataset():
    st.header("📦 Dataset")
    st.write("**Source**: Uber ride data (CSV format) 📊")
    st.write("**Format**: CSV")
    st.write("**Variables**:")
    st.write("- key 🔑")
    st.write("- fare_amount 💵")
    st.write("- pickup_datetime 🕰️")
    st.write("- pickup_longitude 🌍")
    st.write("- pickup_latitude 🌍")
    st.write("- dropoff_longitude 🌍")
    st.write("- dropoff_latitude 🌍")
    st.write("- passenger_count 🚶")

def Features():
    st.header("🔍 Features")
    st.write("Features include pickup and dropoff locations, time of day, fare amount, and passenger count.")

def Skills_Take_Away_From_This_Project():
    st.header("💡 Skills Take Away From This Project")
    st.caption("🔧 Data Cleaning and Preprocessing")
    st.caption("🔍 Feature Engineering")
    st.caption("📊 Exploratory Data Analysis (EDA)")
    st.caption("📈 Regression Modeling")
    st.caption("⚙️ Hyperparameter Tuning")
    st.caption("📉 Model Evaluation")
    st.caption("🌍 Geospatial Analysis")
    st.caption("🕒 Time Series Analysis")
    st.caption("🌐 Web Application Development with Streamlit")
    st.caption("☁️ Deployment on AWS")

def Result():
    st.header("🏆 Results")
    st.write("1. **Trained Model**: A regression model that accurately predicts Uber ride fares. 📈")
    st.write("2. **Web Application**: A Streamlit app that provides fare estimates based on ride details. 🌐")
    st.write("3. **Evaluation Metrics**: Comprehensive performance metrics for the regression model. 📊")

def Conclusion():
    st.header("✅ Conclusion")
    st.write("Developed a predictive model for Uber fares and a Streamlit app for user estimates. 🎯")
    st.write("Deployed on AWS, showcasing skills in data preprocessing, machine learning, and web application development. 🚀")

def about_the_developer():
    st.header("🔍 About the Developer")
    st.subheader("📬 Contact Details")
    st.write("Name : Sethumadhavan V")
    st.write("Email: [sethumadhavanvelu2002@example.com](mailto:sethumadhavanvelu2002@example.com)")
    st.write("Phone: 📞 9159299878")
    st.write("[LinkedIn ID](https://www.linkedin.com/in/sethumadhavan-v-b84890257/)")
    st.write("[GitHub Profile](https://github.com/SETHU0010/Uber_Fare_Prediction_and_Streamlit_Web_Application)")


def main():
    # Main layout with two columns
    col1, col2 = st.columns(2)

    with col1:
        st.header("Navigation")
        options = [
            "Problem Statement", "Objective", "Domain", "Approach", "Workflow", 
            "Prerequisites", "Required Python Libraries", "Dataset", "Features", 
            "Skills Take Away From This Project", "Results", "Conclusion", 
            "About the Developer"
        ]
        choice = st.radio("Go to", options)

    with col2:
        if choice == "Problem Statement":
            Problem_Statement()
        elif choice == "Objective":
            objective()
        elif choice == "Domain":
            Domain()
        elif choice == "Approach":
            Approach()
        elif choice == "Workflow":
            Workflow()
        elif choice == "Prerequisites":
            prerequisites()
        elif choice == "Required Python Libraries":
            required_python_libraries()
        elif choice == "Dataset":
            Dataset()
        elif choice == "Features":
            Features()
        elif choice == "Skills Take Away From This Project":
            Skills_Take_Away_From_This_Project()
        elif choice == "Results":
            Result()
        elif choice == "Conclusion":
            Conclusion()
        elif choice == "About the Developer":
            about_the_developer()

if __name__ == "__main__":
    main()
        
if df is not None and scale is not None and model is not None:
    # Input
    passenger_count = st.number_input('Passenger Count', int(df['passenger_count'].min()), int(df['passenger_count'].max()))
    Distance = st.number_input('Distance in km', float(df['distance(km)'].min()), float(df['distance(km)'].max()))
    Day = st.number_input('Day', int(df['Day'].min()), int(df['Day'].max()))
    year = st.number_input('Year', int(df['year'].min()), int(df['year'].max()))
    month = st.number_input('Month', int(df['month'].min()), int(df['month'].max()))
    hour = st.number_input('Hour', int(df['hour'].min()), int(df['hour'].max()))

    # Prepare new data
    new_data = {'passenger_count': [passenger_count], 'distance(km)': [Distance], 'Day': [Day], 'year': [year], 'month': [month], 'hour': [hour]}
    new_data_df = pd.DataFrame(new_data)

    # Scale new data
    new_data_scaled = scale.transform(new_data_df)
    
    # Predict
    if st.button('Predict'):
        fare_amount = model.predict(new_data_scaled)
        st.markdown(f'# Fare Amount: ${fare_amount.round(2)[0]}')
else:
    st.error('Required files not loaded properly.')
