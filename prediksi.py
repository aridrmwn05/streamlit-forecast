import pickle
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

model = pickle.load(open('prediksi_sales.sav','rb'))

df = pd.read_csv("totalsales_harian.csv")
df['Date'] = pd.to_datetime(df['Date'], format= '%Y-%m-%d')
df.set_index(['Date'], inplace=True)

st.title('Forecasting Total Sales Harian')
hari = st.slider("Tentukan Hari",1,60, step=1)

pred = model.forecast(hari)
pred = pd.DataFrame(pred, columns=['Total Sales'])

if st.button("Predict"):

    col1, col2 = st.columns([2,3])
    with col1:
        st.dataframe(pred)
    with col2:
        fig, ax = plt.subplots()
        df['Total_Value_Sales'].plot(style='--', color='gray', legend=True, label='data yang diketahui')
        pred['Total_Value_Sales'].plot(color='b', legend=True, label='Prediction')
        st.pyplot(fig)