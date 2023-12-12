import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='white')

bikeShare = pd.read_csv('https://raw.githubusercontent.com/fauzanhernadi/Bike-Sharing/main/Submission/dashboard/bikeSharing.csv')

def create_season_daily(df):
    season_data = df.groupby('season_daily')['cnt_daily'].mean()
    return season_data


daily_season = create_season_daily(bikeShare)
season_name = ['Spring', 'Summer', 'Fall', 'Winter']

# Hasil analisis data pertama
st.header('Hasil Analisis Data Rental Sepeda')
st.subheader('Pengaruh suhu terhadap jumlah rental sepeda harian')
plt.figure(figsize=(13, 6))
sns.lineplot(x='temp_daily', y='cnt_hourly', data=bikeShare, errorbar=None)
plt.title("Hubungan suhu terhadap jumlah rental sepeda harian")
plt.xlabel("Suhu")
plt.ylabel("Jumlah rental sepeda harian")
st.pyplot(plt)

# Hasil analisis data kedua
st.subheader('Jumlah sewa sepeda harian berdasarkan musim')
plt.figure(figsize=(13, 6))
colors = ["#D3D3D3", "#D3D3D3", "#72BCD4", "#D3D3D3"]
plt.bar(season_name, daily_season, color=colors)  
plt.xlabel('Musim')
plt.ylabel('Rata rata jumlah rental sepeda harian')
plt.title('Tingkat Jumlah Rental Sepeda Harian')
st.pyplot(plt)

st.subheader('Perbandingan jumlah rental sepeda di hari kerja dengan di hari libur')
plt.figure(figsize=(8, 5))
sns.boxplot(x="workingday_daily", y="cnt_daily", data=bikeShare)
plt.title("Jumlah Sewa Sepeda pada hari kerja dengan hari libur")
plt.xlabel("hari kerja")
plt.ylabel("Jumlah Sewa Sepeda Harian")
st.pyplot(plt)