import streamlit as st
import pandas as pd
import numpy as np

st.write("""
# My Drum Training Diary
""")

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

def load_data():
    google_sheet_link = "https://docs.google.com/spreadsheets/d/1uZ6o5RncwzgZ4pV3hVL4w7qTA7UpKWS1YltcFYGO6I8/gviz/tq?tqx=out:csv"
    SHEET_ID = '1uZ6o5RncwzgZ4pV3hVL4w7qTA7UpKWS1YltcFYGO6I8'
    SHEET_NAME = 'data'
    url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
    #url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv'
    df = pd.read_csv(url)
    return df

data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text("Done!")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


st.dataframe(data)
print(data.head())