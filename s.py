import streamlit as st
import pandas as pd
import pickle
import boto3
from io import BytesIO

# title
st.title('Uber Fares Prediction')

# AWS S3 Configuration
access_key = "AKIAU6GDYLUVQ2BQ2XW2"
secret_key = "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"
s3_bucket_name = 'uber-fare-prediction-data'
region_name = 'ap-south-1'  # Update with the correct region if needed

# Initialize S3 client
s3_client = boto3.client('s3', 
                         aws_access_key_id=access_key, 
                         aws_secret_access_key=secret_key,
                         region_name=region_name)

def load_s3_file(bucket_name, file_key):
    """Load a file from S3."""
    try:
        obj = s3_client.get_object(Bucket=bucket_name, Key=file_key)
        return pd.read_csv(BytesIO(obj['Body'].read()))
    except Exception as e:
        st.error(f"Error loading file {file_key}: {e}")
        return None

def load_s3_pickle(bucket_name, file_key):
    """Load a pickle file from S3."""
    try:
        obj = s3_client.get_object(Bucket=bucket_name, Key=file_key)
        return pickle.load(BytesIO(obj['Body'].read()))
    except Exception as e:
        st.error(f"Error loading file {file_key}: {e}")
        return None

# Paths to S3 files
data_file_key = 'uber_3/Clean_data.csv'
model_file_key = 'uber_3/model.pkl'
scale_file_key = 'uber_3/scale.pkl'

# Load data from S3
df = load_s3_file(s3_bucket_name, data_file_key)
if df is not None:
    scale = load_s3_pickle(s3_bucket_name, scale_file_key)
    model = load_s3_pickle(s3_bucket_name, model_file_key)
else:
    st.error('Data not loaded properly.')

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
