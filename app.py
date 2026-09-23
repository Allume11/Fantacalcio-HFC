import streamlit as st
import pandas as pd

# Configurazione della pagina
st.set_page_config(
    page_title="HFC Fantacalcio Management",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Stile CSS personalizzato per renderla bella, moderna e accattivante
st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(90deg, #1b4f72 0%, #2980b9 100%);
        color: white;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .main-header h1 {
        margin: 0;
        font-size: 2.2rem;
    }
    .main-header p {
        margin: 5px 0 0 0;
        font-size: 1rem;
        opacity: 0.9;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #f8f9fa;
        border-radius: 8px 8px 0 0;
        padding: 10px 20px;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# Intestazione grafica spettacolare
st.markdown("""
    <div class="main-header">
        <h1>🏆 HFC Fantacalcio Management System</h1>
        <p>Piattaforma Web Ufficiale • Sincronizzata con Google Drive & Google Sheets</p>
    </div>
""", unsafe_allow_html=True)

# Menu a schede (Tab) pulito e ordinato
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📋 Rosa & Formazione", 
    "🔨 Asta & Mercato", 
    "⚽ Scontro Diretto", 
    "🛡️ Modificatore & Stat", 
    "📅 Calendario & Classifica"
])

with tab1:
    st.subheader("📋 Gestione Rosa e Formazione Titolari")
    col1, col2 = st.columns([1, 2])
    with col1:
        utente_sel = st.selectbox("Seleziona Squadra", ["Leonardo", "Squadra 2", "Squadra 3"], key="rosa_ut")
    with col2:
        st.info(f"Stai visualizzando la rosa e i titolari di **{utente_sel}**.")
    
    # Esempio tabella rosa
    df_sample = pd.DataFrame({
        "Ruolo": ["P", "D", "D", "C", "C", "A", "A"],
        "Calciatore": ["Di Gregorio", "Bastoni", "Di Lorenzo", "Barella", "Pulisic", "Lautaro", "Retegui"],
        "Squadra": ["Juve", "Inter", "Napoli", "Inter", "Milan", "Inter", "Atalanta"],
        "FM": [6.5, 6.3, 6.4, 6.8, 7.2, 8.5, 7.9]
    })
    st.dataframe(df_sample, use_container_width=True)

with tab2:
    st.subheader("🔨 Asta Live & Mercato di Riparazione")
    col1, col2, col3 = st.columns(3)
    with col1:
        ruolo_asta = st.selectbox("Ruolo", ["Portieri", "Difensori", "Centrocampisti", "Attaccanti"])
    with col2:
        giocatore_asta = st.selectbox("Giocatore", ["Nome Giocatore 1", "Nome Giocatore 2"])
    with col3:
        offerta = st.number_input("Offerta Crediti (1-500)", min_value=1, max_value=500, value=10)
    
    if st.button("Fai Offerta / Acquista", type="primary"):
        st.success(f"Offerta registrata con successo per {giocatore_asta}!")

with tab3:
    st.subheader("⚽ Simulatore Giornata & Scontro Diretto")
    c1, c2, c3 = st.columns([2, 1, 2])
    with c1:
        squadra_casa = st.selectbox("Squadra Casa", ["Leonardo", "Squadra 2"], key="sc_casa")
    with c2:
        st.markdown("<h3 style='text-align: center;'>VS</h3>", unsafe_allow_html=True)
    with c3:
        squadra_fuori = st.selectbox("Squadra Trasferta", ["Squadra 3", "Squadra 4"], key="sc_fuori")
    
    if st.button("Simula Partita in Diretta", type="primary"):
        col_res1, col_res2 = st.columns(2)
        col_res1.metric(label=squadra_casa, value="74.5", delta="+1.5 vs media")
        col_res2.metric(label=squadra_fuori, value="69.0", delta="-2.0 vs media")
        st.balloons()

with tab4:
    st.subheader("🛡️ Modificatore di Difesa & 📊 Classifica Marcatori")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Calcola Modificatore Difesa"):
            st.info("Calcolo modificatore completato per tutti i fantallenatori.")
    with col2:
        if st.button("Aggiorna Statistiche & Bonus"):
            st.success("Statistiche aggiornate dal file di Google Drive!")

with tab5:
    st.subheader("📅 Calendario Ufficiale & Classifica Generale")
    
    # Classifica finta di esempio ma bellissima da vedere
    df_classifica = pd.DataFrame({
        "Pos": [1, 2, 3, 4],
        "Squadra": ["Leonardo", "Squadra 2", "Squadra 3", "Squadra 4"],
        "Punti": [15, 12, 10, 7],
        "FantaVinti": [5, 4, 3, 2],
        "Totale FantaPunti": [372.5, 360.0, 355.5, 340.0]
    })
    st.dataframe(df_classifica, use_container_width=True)
