import pickle
import streamlit as st

model = pickle.load(open('estimasi_phone.sav', 'rb'))

st.title('Estimasi Harga Telepon Seluler')

#weight, resoloution, ppi, cpu_core, cpu_freq, internal_mem, ram, RearCam, Front_Cam, battery, thickness
weight = st.number_input('Input Berat (gr)')
resoloution = st.number_input('Input Resolusi')
ppi = st.number_input('Input Pixel Layar')
cpu_core = st.number_input('Input CPU CORE')
cpu_freq = st.number_input('Input Frekuensi CPU (GHz)')
internal_mem = st.number_input('Input Memori Internal (GB)')
ram = st.number_input('Input RAM (GB)')
RearCam = st.number_input('Input Resolusi Kamera Belakang (MP)')
Front_Cam = st.number_input('Input Resolusi Kamera Depan (MP)')
battery = st.number_input('Input Kapasitas Baterai (mAH)')
thickness = st.number_input('Input Ketebalan Telepon Seluler (inch)')


predict = ''

if st.button('Estimasi'):
    predict = model.predict(
        [[weight, resoloution, ppi, cpu_core, cpu_freq, internal_mem, ram, RearCam, Front_Cam, battery, thickness]]
    )
    st.write ('Estimasi Harga Telepon Seluler Rial Iran : ', predict, 'IRR')
    st.write ('Estimasi Harga Telepon Seluler Rupiah : ', predict*0.35, 'IDR')