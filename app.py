
import streamlit as st
import pandas as pd

st.set_page_config(page_title="HFC Fantacalcio", page_icon="⚽", layout="centered")

st.title("🏆 HFC Fantacalcio Management System")
st.write("Benvenuto nella web app ufficiale della tua lega!")

# Menu laterale
scelta = st.sidebar.selectbox("Navigazione", ["Classifica & Rose", "Asta & Mercato", "Simulatore Scontro"])

if scelta == "Classifica & Rose":
    st.header("📊 Classifica Ufficiale")
    # Legge i dati salvati su Google Sheets o mostra un'anteprima
    st.info("I dati sono sincronizzati con Google Sheets.")
    
elif scelta == "Asta & Mercato":
    st.header("🔨 Asta Live")
    ruolo = st.selectbox("Seleziona Ruolo", ["Portieri", "Difensori", "Centrocampisti", "Attaccanti"])
    st.write(f"Stai gestendo l'asta per il ruolo: {ruolo}")

elif scelta == "Simulatore Scontro":
    st.header("⚽ Scontro Diretto")
    squadra_1 = st.selectbox("Squadra Casa", ["Leonardo", "Amico 1"])
    squadra_2 = st.selectbox("Squadra Trasferta", ["Amico 2", "Amico 3"])
    if st.button("Simula Partita"):
        st.success("Partita simulata con successo!")
