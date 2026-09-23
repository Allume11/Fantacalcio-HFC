import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Gestione Lega Fantacalcio", page_icon="⚽", layout="wide"
)

st.title("⚽ Piattaforma Gestione Lega Fantacalcio")
st.markdown(
    "Crea la tua lega, gestisci i partecipanti e consulta il listone aggiornato."
)

# --- 1. CONFIGURAZIONE DELLA LEGA ---
st.sidebar.header("⚙️ Configurazione Lega")
nome_lega = st.sidebar.text_input("Nome della Lega", "La mia Lega")
budget_iniziale = st.sidebar.number_input(
    "Crediti Iniziali per Squadra", value=500, step=50
)

# Inserimento dei partecipanti reali
partecipanti_input = st.sidebar.text_area(
    "Nomi dei Partecipanti (uno per riga)", "Leonardo\nAmico 1\nAmico 2\nAmico 3"
)
lista_partecipanti = [p.strip() for p in partecipanti_input.split("\n") if p.strip()]

st.sidebar.success(
    f"Lega '{nome_lega}' attiva con {len(lista_partecipanti)} partecipanti!"
)

# Menu di navigazione principale
scelta = st.sidebar.radio(
    "Vai a:",
    ["📋 Listone Serie A", "👥 Rose delle Squadre", "🔨 Gestione Mercato / Asta"],
)

# --- 2. LISTONE AGGIORNATO SERIE A ---
data_listone = {
    "Giocatore": [
        "Lautaro Martinez",
        "Marcus Thuram",
        "Donyell Malen",
        "Hakan Calhanoglu",
        "Christian Pulisic",
        "Scott McTominay",
        "Nico Paz",
        "Kenan Yildiz",
        "Federico Dimarco",
        "Mike Maignan",
        "Mile Svilar",
        "Gleison Bremer",
        "Alessandro Buongiorno",
        "Riccardo Orsolini",
        "Moise Kean",
        "Rasmus Hojlund",
    ],
    "Ruolo": [
        "A",
        "A",
        "A",
        "C",
        "C",
        "C",
        "C",
        "A",
        "D",
        "P",
        "P",
        "D",
        "D",
        "C",
        "A",
        "A",
    ],
    "Squadra": [
        "Inter",
        "Inter",
        "Roma",
        "Inter",
        "Milan",
        "Napoli",
        "Como",
        "Juventus",
        "Inter",
        "Milan",
        "Roma",
        "Juventus",
        "Napoli",
        "Bologna",
        "Fiorentina",
        "Napoli",
    ],
    "Quotazione": [35, 29, 34, 27, 25, 28, 30, 23, 32, 15, 18, 15, 14, 26, 25, 28],
}
df_listone = pd.DataFrame(data_listone)

if scelta == "📋 Listone Serie A":
    st.header("📋 Listone Ufficiale Giocatori Serie A")
    st.markdown("Cerca e filtra i giocatori per ruolo o squadra.")

    col1, col2 = st.columns(2)
    with col1:
        filtro_ruolo = st.selectbox(
            "Filtra per Ruolo", ["Tutti", "P", "D", "C", "A"]
        )
    with col2:
        filtro_squadra = st.selectbox(
            "Filtra per Squadra", ["Tutte"] + list(df_listone["Squadra"].unique())
        )

    df_filtrato = df_listone.copy()
    if filtro_ruolo != "Tutti":
        df_filtrato = df_filtrato[df_filtrato["Ruolo"] == filtro_ruolo]
    if filtro_squadra != "Tutte":
        df_filtrato = df_filtrato[df_filtrato["Squadra"] == filtro_squadra]

    st.dataframe(df_filtrato, use_container_width=True)

# --- 3. ROSE DELLE SQUADRE ---
elif scelta == "👥 Rose delle Squadre":
    st.header("👥 Rose delle Squadre della Lega")
    st.markdown("Visualizza i giocatori acquistati da ciascun partecipante.")

    if "rose" not in st.session_state:
        st.session_state.rose = {
            p: pd.DataFrame(columns=["Giocatore", "Ruolo", "Squadra", "Spesa"])
            for p in lista_partecipanti
        }

    squadra_selezionata = st.selectbox(
        "Seleziona la squadra da visualizzare", lista_partecipanti
    )

    if squadra_selezionata in st.session_state.rose:
        st.subheader(f"Rosa di: {squadra_selezionata}")
        st.dataframe(
            st.session_state.rose[squadra_selezionata], use_container_width=True
        )
    else:
        st.info("Nessun giocatore in rosa per questa squadra.")

# --- 4. GESTIONE MERCATO / ASTA ---
elif scelta == "🔨 Gestione Mercato / Asta":
    st.header("🔨 Assegnazione Giocatori (Asta / Mercato)")
    st.markdown(
        "Seleziona un giocatore dal listone, assegnalo a un partecipante e scala i crediti."
    )

    if "rose" not in st.session_state:
        st.session_state.rose = {
            p: pd.DataFrame(columns=["Giocatore", "Ruolo", "Squadra", "Spesa"])
            for p in lista_partecipanti
        }

    col1, col2, col3 = st.columns(3)

    with col1:
        giocatore_scelto = st.selectbox(
            "Scegli Giocatore", df_listone["Giocatore"].tolist()
        )
    with col2:
        acquirente = st.selectbox("Assegna a Squadra", lista_partecipanti)
    with col3:
        prezzo_pagato = st.number_input("Crediti spesi", min_value=1, value=10)

    if st.button("💾 Conferma Acquisto"):
        info_giocatore = df_listone[
            df_listone["Giocatore"] == giocatore_scelto
        ].iloc[0]

        nuovo_acquisto = pd.DataFrame(
            [
                {
                    "Giocatore": info_giocatore["Giocatore"],
                    "Ruolo": info_giocatore["Ruolo"],
                    "Squadra": info_giocatore["Squadra"],
                    "Spesa": prezzo_pagato,
                }
            ]
        )

        st.session_state.rose[acquirente] = pd.concat(
            [st.session_state.rose[acquirente], nuovo_acquisto], ignore_index=True
        )
        st.success(
            f"✅ {giocatore_scelto} assegnato a {acquirente} per {prezzo_pagato} crediti!"
        )
