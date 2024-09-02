import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

hour_df = pd.read_csv("https://raw.githubusercontent.com/MuhammadFauzanL/bikeAnalyst/main/hour_dataa.csv")
day_df = pd.read_csv("https://raw.githubusercontent.com/MuhammadFauzanL/bikeAnalyst/main/day_dataFrame.csv")

hour_df['hour'] = hour_df['hour'].apply(lambda x: f"{x:02d}:00")

total_by_weather_hour = hour_df.groupby(['weather_situation', 'hour'])['count'].sum().reset_index()
total_by_weather = hour_df.groupby('weather_situation')['count'].sum().reset_index()
total_by_hour = hour_df.groupby('hour')['count'].sum().reset_index()

day_df['dteday'] = pd.to_datetime(day_df['dteday'])
day_df['day_type'] = day_df['workingday'].apply(lambda x: 'Hari Kerja' if x == 1 else 'Akhir Pekan')
total_registered = day_df.groupby('day_type')['registered'].sum().reset_index()

st.title('Analisis Penyewaan Sepeda Dicoding')

st.subheader('Total Penyewaan Sepeda Berdasarkan Cuaca dan Jam')
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=total_by_weather_hour, x='hour', y='count', hue='weather_situation', marker='o', ax=ax)
ax.set_title('Total Penyewaan Sepeda Berdasarkan Cuaca dan Jam')
ax.set_xlabel('Jam')
ax.set_ylabel('Jumlah Penyewaan')
st.pyplot(fig)

st.subheader('Total Penyewaan Sepeda Berdasarkan Cuaca')
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=total_by_weather, x='weather_situation', y='count', ax=ax)
ax.set_title('Total Penyewaan Sepeda Berdasarkan Cuaca')
ax.set_xlabel('Situasi Cuaca')
ax.set_ylabel('Jumlah Penyewaan')
st.pyplot(fig)

st.subheader('Total Penyewaan Sepeda Berdasarkan Jam')
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(data=total_by_hour, x='hour', y='count', ax=ax)
ax.set_title('Total Penyewaan Sepeda Berdasarkan Jam')
ax.set_xlabel('Jam')
ax.set_ylabel('Jumlah Penyewaan')
st.pyplot(fig)

st.subheader('Total Penyewaan Sepeda Berdasarkan Hari Kerja dan Akhir Pekan')
st.write(total_registered)

st.subheader('Distribusi Pendaftaran Sepeda Berdasarkan Hari dalam Seminggu')
fig, ax = plt.subplots(figsize=(12, 6))
sns.boxplot(x='weekday', y='registered', data=day_df, palette='coolwarm', ax=ax)
ax.set_title('Distribusi Pendaftaran Sepeda Berdasarkan Hari dalam Seminggu')
ax.set_xlabel('Hari dalam Seminggu (0=Minggu, 6=Sabtu)')
ax.set_ylabel('Jumlah Pendaftaran Sepeda')
st.pyplot(fig)

st.subheader('Total Pendaftaran Sepeda Berdasarkan Hari Kerja dan Akhir Pekan')
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='day_type', y='registered', data=total_registered, ax=ax)
ax.set_title('Total Pendaftaran Sepeda Berdasarkan Hari Kerja dan Akhir Pekan')
ax.set_xlabel('Tipe Hari')
ax.set_ylabel('Total Pendaftaran Sepeda')
st.pyplot(fig)
