import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Gestione Lega Fantacalcio", page_icon="⚽", layout="wide"
)

st.title("⚽ Piattaforma Gestione Lega Fantacalcio")
st.markdown(
    "Gestione della lega, rose aggiornate e listone ufficiale della Serie A."
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

# --- 2. LISTONE AGGIORNATO STAGIONE CORRENTE ---
giocatori_data = [
    # Atalanta
    ("Carnesecchi Marco", "P", "Atalanta", 15),
    ("Bellanova Raoul", "D", "Atalanta", 16),
    ("Kolasinac Sead", "D", "Atalanta", 14),
    ("Hien Isak", "D", "Atalanta", 12),
    ("Ederson", "C", "Atalanta", 22),
    ("Samardzic Lazar", "C", "Atalanta", 20),
    ("Retegui Mateo", "A", "Atalanta", 32),
    ("Lookman Ademola", "A", "Atalanta", 35),
    ("De Ketelaere Charles", "A", "Atalanta", 28),
    # Bologna
    ("Skorupski Lukasz", "P", "Bologna", 13),
    ("Posch Stefan", "D", "Bologna", 11),
    ("Miranda Juan", "D", "Bologna", 10),
    ("Ferguson Lewis", "C", "Bologna", 18),
    ("Fabbian Giovanni", "C", "Bologna", 15),
    ("Orsolini Riccardo", "A", "Bologna", 24),
    ("Castro Santiago", "A", "Bologna", 20),
    # Inter
    ("Sommer Yann", "P", "Inter", 16),
    ("Martinez Josep", "P", "Inter", 2),
    ("Bastoni Alessandro", "D", "Inter", 18),
    ("Dimarco Federico", "D", "Inter", 22),
    ("Pavard Benjamin", "D", "Inter", 15),
    ("Barella Nicolò", "C", "Inter", 25),
    ("Çalhanoğlu Hakan", "C", "Inter", 28),
    ("Frattesi Davide", "C", "Inter", 16),
    ("Zielinski Piotr", "C", "Inter", 17),
    ("Martínez Lautaro", "A", "Inter", 40),
    ("Thuram Marcus", "A", "Inter", 32),
    ("Taremi Mehdi", "A", "Inter", 22),
    # Juventus
    ("Di Gregorio Michele", "P", "Juventus", 15),
    ("Bremer Gleison", "D", "Juventus", 17),
    ("Cambiaso Andrea", "D", "Juventus", 16),
    ("Koopmeiners Teun", "C", "Juventus", 26),
    ("Douglas Luiz", "C", "Juventus", 18),
    ("Thuram Khéphren", "C", "Juventus", 14),
    ("Vlahovic Dusan", "A", "Juventus", 35),
    ("Yildiz Kenan", "A", "Juventus", 20),
    ("González Nicolás", "A", "Juventus", 22),
    # Milan
    ("Maignan Mike", "P", "Milan", 16),
    ("Theo Hernández", "D", "Milan", 22),
    ("Tomori Fikayo", "D", "Milan", 13),
    ("Reijnders Tijjani", "C", "Milan", 18),
    ("Fofana Youssouf", "C", "Milan", 15),
    ("Pulisic Christian", "C", "Milan", 25),
    ("Leão Rafael", "A", "Milan", 35),
    ("Morata Álvaro", "A", "Milan", 28),
    ("Abraham Tammy", "A", "Milan", 22),
    # Napoli
    ("Meret Alex", "P", "Napoli", 14),
    ("Di Lorenzo Giovanni", "D", "Napoli", 17),
    ("Buongiorno Alessandro", "D", "Napoli", 16),
    ("McTominay Scott", "C", "Napoli", 24),
    ("Lobotka Stanislav", "C", "Napoli", 15),
    ("Lukaku Romelu", "A", "Napoli", 34),
    ("Kvaratskhelia Khvicha", "A", "Napoli", 36),
    ("Neres David", "A", "Napoli", 22),
    # Roma
    ("Svilar Mile", "P", "Roma", 15),
    ("Mancini Gianluca", "D", "Roma", 13),
    ("Angelino", "D", "Roma", 11),
    ("Pellegrini Lorenzo", "C", "Roma", 17),
    ("Koné Manu", "C", "Roma", 15),
    ("Dybala Paulo", "A", "Roma", 32),
    ("Dovbyk Artem", "A", "Roma", 28),
    ("Soulé Matias", "A", "Roma", 22),
    # Lazio
    ("Provedel Ivan", "P", "Lazio", 15),
    ("Romagnoli Alessio", "D", "Lazio", 13),
    ("Nuno Tavares", "D", "Lazio", 14),
    ("Guendouzi Mattéo", "C", "Lazio", 17),
    ("Zaccagni Mattia", "A", "Lazio", 24),
    ("Dia Boulaye", "A", "Lazio", 25),
    ("Castellanos Taty", "A", "Lazio", 22),
    # Fiorentina
    ("De Gea David", "P", "Fiorentina", 16),
    ("Gosens Robin", "D", "Fiorentina", 17),
    ("Colpani Andrea", "C", "Fiorentina", 18),
    ("Bove Edoardo", "C", "Fiorentina", 14),
    ("Kean Moise", "A", "Fiorentina", 24),
    ("Gudmundsson Albert", "A", "Fiorentina", 26),
    # Como
    ("Audero Emil", "P", "Como", 13),
    ("Sergi Roberto", "C", "Como", 14),
    ("Nico Paz", "A", "Como", 22),
    ("Cutrone Patrick", "A", "Como", 18),
    ("Belotti Andrea", "A", "Como", 15),
    # Torino
    ("Milinković-Savić Vanja", "P", "Torino", 14),
    ("Coco Saul", "D", "Torino", 11),
    ("Ricci Samuele", "C", "Torino", 13),
    ("Vlasic Nikola", "C", "Torino", 16),
    ("Zapata Duvan", "A", "Torino", 30),
    ("Adams Che", "A", "Torino", 18),
]

df_listone = pd.DataFrame(
    giocatori_data, columns=["Giocatore", "Ruolo", "Squadra", "Quotazione"]
)

if scelta == "📋 Listone Serie A":
    st.header(
        f"📋 Listone Ufficiale Giocatori (Totale: {len(df_listone)} giocatori)"
    )
    st.markdown("Cerca e filtra i giocatori per ruolo o squadra.")
