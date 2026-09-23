import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Gestione Lega Fantacalcio", page_icon="⚽", layout="wide"
)

st.title("⚽ Piattaforma Gestione Lega Fantacalcio")
st.markdown(
    "Crea la tua lega, gestisci i partecipanti e consulta il listone ufficiale"
    " completo della Serie A."
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

# --- 2. LISTONE COMPLETO SERIE A (TUTTE LE SQUADRE) ---
giocatori_data = [
    # Atalanta
    ("Carnesecchi Marco", "P", "Atalanta", 15),
    ("Rui Patrício", "P", "Atalanta", 1),
    ("Rossi Francesco", "P", "Atalanta", 1),
    ("Kolasinac Sead", "D", "Atalanta", 14),
    ("Hien Isak", "D", "Atalanta", 12),
    ("Djimsiti Berat", "D", "Atalanta", 10),
    ("Bellanova Raoul", "D", "Atalanta", 16),
    ("Ruggeri Matteo", "D", "Atalanta", 11),
    ("Zappacosta Davide", "D", "Atalanta", 12),
    ("Scalvini Giorgio", "D", "Atalanta", 15),
    ("Ederson", "C", "Atalanta", 22),
    ("De Roon Marten", "C", "Atalanta", 14),
    ("Pasalic Mario", "C", "Atalanta", 18),
    ("Koopmeiners Teun", "C", "Atalanta", 30),
    ("Samardzic Lazar", "C", "Atalanta", 20),
    ("Brescianini Marco", "C", "Atalanta", 12),
    ("Retegui Mateo", "A", "Atalanta", 32),
    ("De Ketelaere Charles", "A", "Atalanta", 28),
    ("Lookman Ademola", "A", "Atalanta", 35),
    ("Zaniolo Nicolò", "A", "Atalanta", 18),
    # Bologna
    ("Skorupski Lukasz", "P", "Bologna", 13),
    ("Ravaglia Federico", "P", "Bologna", 1),
    ("Posch Stefan", "D", "Bologna", 11),
    ("Beukema Sam", "D", "Bologna", 12),
    ("Lucumí Jhon", "D", "Bologna", 10),
    ("Miranda Juan", "D", "Bologna", 10),
    ("De Silvestri Lorenzo", "D", "Bologna", 5),
    ("Freuler Remo", "C", "Bologna", 13),
    ("Aebischer Michel", "C", "Bologna", 9),
    ("Fabbian Giovanni", "C", "Bologna", 15),
    ("Ferguson Lewis", "C", "Bologna", 18),
    ("Urbanski Kacper", "C", "Bologna", 7),
    ("Orsolini Riccardo", "A", "Bologna", 24),
    ("Ndoye Dan", "A", "Bologna", 16),
    ("Castro Santiago", "A", "Bologna", 20),
    ("Dallinga Thijs", "A", "Bologna", 18),
    # Inter
    ("Sommer Yann", "P", "Inter", 16),
    ("Martinez Josep", "P", "Inter", 2),
    ("Di Gennaro Raffaele", "P", "Inter", 1),
    ("Bastoni Alessandro", "D", "Inter", 18),
    ("Pavard Benjamin", "D", "Inter", 15),
    ("Acerbi Francesco", "D", "Inter", 11),
    ("De Vrij Stefan", "D", "Inter", 10),
    ("Bisseck Yann", "D", "Inter", 9),
    ("Dimarco Federico", "D", "Inter", 22),
    ("Dumfries Denzel", "D", "Inter", 17),
    ("Darmian Matteo", "D", "Inter", 10),
    ("Carlos Augusto", "D", "Inter", 11),
    ("Barella Nicolò", "C", "Inter", 25),
    ("Çalhanoğlu Hakan", "C", "Inter", 28),
    ("Mkhitaryan Henrikh", "C", "Inter", 18),
    ("Frattesi Davide", "C", "Inter", 16),
    ("Zielinski Piotr", "C", "Inter", 17),
    ("Asllani Kristjan", "C", "Inter", 7),
    ("Thuram Marcus", "A", "Inter", 32),
    ("Martínez Lautaro", "A", "Inter", 40),
    ("Taremi Mehdi", "A", "Inter", 22),
    ("Arnautovic Marko", "A", "Inter", 12),
    ("Correa Joaquín", "A", "Inter", 5),
    # Juventus
    ("Di Gregorio Michele", "P", "Juventus", 15),
    ("Perin Mattia", "P", "Juventus", 3),
    ("Pinsoglio Carlo", "P", "Juventus", 1),
    ("Bremer Gleison", "D", "Juventus", 17),
    ("Gatti Federico", "D", "Juventus", 12),
    ("Kalulu Pierre", "D", "Juventus", 11),
    ("Danilo", "D", "Juventus", 10),
    ("Cambiaso Andrea", "D", "Juventus", 16),
    ("Cabal Juan", "D", "Juventus", 7),
    ("Savona Nicolò", "D", "Juventus", 8),
    ("Locatelli Manuel", "C", "Juventus", 13),
    ("Thuram Khéphren", "C", "Juventus", 14),
    ("Douglas Luiz", "C", "Juventus", 18),
    ("Koopmeiners Teun", "C", "Juventus", 26),
    ("Fagioli Nicolò", "C", "Juventus", 11),
    ("McKennie Weston", "C", "Juventus", 13),
    ("Yildiz Kenan", "A", "Juventus", 20),
    ("Vlahovic Dusan", "A", "Juventus", 35),
    ("González Nicolás", "A", "Juventus", 22),
    ("Conçeicao Francisco", "A", "Juventus", 18),
    ("Milik Arkadiusz", "A", "Juventus", 12),
    # Milan
    ("Maignan Mike", "P", "Milan", 16),
    ("Sportiello Marco", "P", "Milan", 2),
    ("Torriani Lorenzo", "P", "Milan", 1),
    ("Theo Hernández", "D", "Milan", 22),
    ("Tomori Fikayo", "D", "Milan", 13),
    ("Thiaw Malick", "D", "Milan", 10),
    ("Pavlovic Strahinja", "D", "Milan", 11),
    ("Calabria Davide", "D", "Milan", 8),
    ("Emerson Royal", "D", "Milan", 9),
    ("Gabbia Matteo", "D", "Milan", 10),
    ("Fofana Youssouf", "C", "Milan", 15),
    ("Reijnders Tijjani", "C", "Milan", 18),
    ("Loftus-Cheek Ruben", "C", "Milan", 16),
    ("Bennacer Ismaël", "C", "Milan", 12),
    ("Musah Yunus", "C", "Milan", 8),
    ("Pulisic Christian", "C", "Milan", 25),
    ("Leão Rafael", "A", "Milan", 35),
    ("Morata Álvaro", "A", "Milan", 28),
    ("Abraham Tammy", "A", "Milan", 22),
    ("Okafor Noah", "A", "Milan", 14),
    ("Chukwueze Samuel", "A", "Milan", 12),
    # Napoli
    ("Meret Alex", "P", "Napoli", 14),
    ("Caprile Elia", "P", "Napoli", 4),
    ("Contini Nikita", "P", "Napoli", 1),
    ("Di Lorenzo Giovanni", "D", "Napoli", 17),
    ("Buongiorno Alessandro", "D", "Napoli", 16),
    ("Rrahmani Amir", "D", "Napoli", 12),
    ("Juan Jesus", "D", "Napoli", 7),
    ("Olivera Mathias", "D", "Napoli", 9),
    ("Spinazzola Leonardo", "D", "Napoli", 10),
    ("Mazzocchi Pasquale", "D", "Napoli", 7),
    ("Lobotka Stanislav", "C", "Napoli", 15),
    ("Anguissa Frank", "C", "Napoli", 14),
    ("McTominay Scott", "C", "Napoli", 24),
    ("Gilmour Billy", "C", "Napoli", 10),
    ("Folorunsho Michael", "C", "Napoli", 8),
    ("Verdi Simone", "C", "Napoli", 5),
    ("Kvaratskhelia Khvicha", "A", "Napoli", 36),
    ("Lukaku Romelu", "A", "Napoli", 34),
    ("Politano Matteo", "A", "Napoli", 16),
    ("Neres David", "A", "Napoli", 22),
    ("Raspadori Giacomo", "A", "Napoli", 14),
    ("Simeone Giovanni", "A", "Napoli", 12),
    # Roma
    ("Svilar Mile", "P", "Roma", 15),
    ("Ryan Mathew", "P", "Roma", 1),
    ("Mancini Gianluca", "D", "Roma", 13),
    ("Ndicka Evan", "D", "Roma", 11),
    ("Hummels Mats", "D", "Roma", 10),
    ("Angelino", "D", "Roma", 11),
    ("Celik Zeki", "D", "Roma", 7),
    ("Hermoso Mario", "D", "Roma", 12),
    ("Cristante Bryan", "C", "Roma", 12),
    ("Pellegrini Lorenzo", "C", "Roma", 17),
    ("Paredes Leandro", "C", "Roma", 11),
    ("Koné Manu", "C", "Roma", 15),
    ("Le Fée Enzo", "C", "Roma", 10),
    ("Baldanzi Tommaso", "C", "Roma", 9),
    ("Saelemaekers Alexis", "C", "Roma", 12),
    ("Dybala Paulo", "A", "Roma", 32),
    ("Soulé Matias", "A", "Roma", 22),
    ("Dovbyk Artem", "A", "Roma", 28),
    ("Shomurodov Eldor", "A", "Roma", 6),
]

df_listone = pd.DataFrame(
    giocatori_data, columns=["Giocatore", "Ruolo", "Squadra", "Quotazione"]
)

if scelta == "📋 Listone Serie A":
    st.header(
        f"📋 Listone Ufficiale Giocatori Serie A (Totale: {len(df_listone)}"
        " giocatori)"
    )
    st.markdown("Cerca e filtra i giocatori per ruolo o squadra.")

    col1, col2 = st.columns(2)
    with col1:
        filtro_ruolo = st.selectbox(
            "Filtra per Ruolo", ["Tutti", "P", "D", "C", "A"]
        )
    with col2:
        filtro_squadra = st.selectbox(
            "Filtra per Squadra", ["Tutte"] + sorted(list(df_listone["Squadra"].unique()))
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
        "Seleziona un giocatore dal listone, assegnalo a un partecipante e scala"
        " i crediti."
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
            f"✅ {giocatore_scelto} assegnato a {acquirente} per {prezzo_pagato}"
            " crediti!"
        )
