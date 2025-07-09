import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('biaya_hidup_model.pkl')  # load model dari file

st.title("Prediksi Biaya Hidup Freelancer di Indonesia")
st.markdown("""
Setelah semua input dimasukkan, pengguna menekan tombol **"Prediksi Biaya Hidup"** dan model akan memproses data tersebut melalui algoritma regresi linear yang sudah dilatih sebelumnya. Model akan mempertimbangkan seluruh variabel, termasuk faktor non-numerik seperti **gaya hidup**, dan menghasilkan estimasi total biaya hidup bulanan.

Dalam kasus ini, model memprediksi bahwa biaya hidup bulanan untuk kondisi tersebut adalah **sekitar Rp 6.171.054**.  
Angka ini merupakan hasil dari perhitungan model berdasarkan hubungan historis antara seluruh variabel terhadap total biaya hidup di dataset yang digunakan untuk pelatihan.

Hasil prediksi ini dapat digunakan sebagai acuan bagi freelancer atau pekerja remote untuk merencanakan kebutuhan finansial mereka di berbagai kota dan gaya hidup yang berbeda.
""")

# Input user
city = st.selectbox("Pilih Kota", ['Jakarta', 'Surabaya', 'Yogyakarta', 'Bali', 'Bandung'])
status = st.radio("Status", ['Single', 'Menikah'])
lifestyle = st.selectbox("Gaya Hidup", ['Minimalis', 'Menengah', 'Mewah'])

rent = st.number_input("Biaya Sewa Tempat (IDR)", value=0)
food = st.number_input("Biaya Makan per Bulan (IDR)", value=0)
transport = st.number_input("Biaya Transportasi (IDR)", value=0)
internet = st.number_input("Biaya Internet (IDR)", value=0)
gym = st.number_input("Biaya Gym (IDR)", value=0)

# Mapping sesuai model
city_mapping = {'Jakarta': 0, 'Bali': 1, 'Bandung': 2, 'Surabaya': 3, 'Yogyakarta': 4}
status_mapping = {'Single': 0, 'Menikah': 1}
lifestyle_mapping = {'Minimalis': 0, 'Menengah': 1, 'Mewah': 2}

input_data = pd.DataFrame([[
    city_mapping[city],
    status_mapping[status],
    lifestyle_mapping[lifestyle],
    rent,
    food,
    transport,
    internet,
    gym
]], columns=['city', 'status', 'lifestyle', 'rent', 'food', 'transport', 'internet', 'gym'])

# Prediksi saat tombol diklik
if st.button("Prediksi Biaya Hidup"):
    pred = model.predict(input_data)[0]
    st.success(f"Estimasi biaya hidup bulanan kamu: Rp {int(pred):,}")
