mport pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Gestione Lega Fantacalcio", page_icon="⚽", layout="wide"
)

st.title("⚽ Piattaforma Gestione Lega Fantacalcio")
st.markdown(
    "Gestione completa della lega, rose e listone ufficiale di tutte le 20"
    " squadre di Serie A."
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

# --- 2. LISTONE COMPLETO TUTTE LE 20 SQUADRE DI SERIE A ---
giocatori_data = [
    # Atalanta
    ("Carnesecchi Marco", "P", "Atalanta", 15),
    ("Rui Patrício", "P", "Atalanta", 1),
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
    ("Freuler Remo", "C", "Bologna", 13),
    ("Aebischer Michel", "C", "Bologna", 9),
    ("Fabbian Giovanni", "C", "Bologna", 15),
    ("Ferguson Lewis", "C", "Bologna", 18),
    ("Urbanski Kacper", "C", "Bologna", 7),
    ("Orsolini Riccardo", "A", "Bologna", 24),
    ("Ndoye Dan", "A", "Bologna", 16),
    ("Castro Santiago", "A", "Bologna", 20),
    ("Dallinga Thijs", "A", "Bologna", 18),
    # Cagliari
    ("Scuffet Simone", "P", "Cagliari", 12),
    ("Sherri Alen", "P", "Cagliari", 1),
    ("Mina Yerry", "D", "Cagliari", 11),
    ("Luperto Sebastiano", "D", "Cagliari", 10),
    ("Zappa Gabriele", "D", "Cagliari", 8),
    ("Augello Tommaso", "D", "Cagliari", 9),
    ("Palomino José Luis", "D", "Cagliari", 7),
    ("Prati Antoine", "C", "Cagliari", 10),
    ("Adopo Michel", "C", "Cagliari", 7),
    ("Deiola Alessandro", "C", "Cagliari", 6),
    ("Makoumbou Antoine", "C", "Cagliari", 8),
    ("Gaetano Gianluca", "C", "Cagliari", 13),
    ("Viola Nicolas", "C", "Cagliari", 9),
    ("Lapadula Gianluca", "A", "Cagliari", 16),
    ("Piccoli Roberto", "A", "Cagliari", 15),
    ("Pavoletti Leonardo", "A", "Cagliari", 10),
    ("Luvumbo Zito", "A", "Cagliari", 14),
    # Como
    ("Audero Emil", "P", "Como", 13),
    ("Reina Pepe", "P", "Como", 1),
    ("Goldaniga Edoardo", "D", "Como", 8),
    ("Kempf Marc-Oliver", "D", "Como", 9),
    ("Moreno Alberto", "D", "Como", 8),
    ("Sala Marco", "D", "Como", 6),
    ("Pezzella Alessio", "D", "Como", 5),
    ("Perrone Máximo", "C", "Como", 11),
    ("Sergi Roberto", "C", "Como", 14),
    ("Baselli Daniele", "C", "Como", 7),
    ("Mazzitelli Luca", "C", "Como", 9),
    ("Strefezza Gabriel", "A", "Como", 16),
    ("Nico Paz", "A", "Como", 22),
    ("Cutrone Patrick", "A", "Como", 18),
    ("Belotti Andrea", "A", "Como", 15),
    ("Alieu Fadera", "A", "Como", 10),
    # Empoli
    ("Vasquez Devis", "P", "Empoli", 12),
    ("Seghetti Jacopo", "P", "Empoli", 1),
    ("Ismajli Ardian", "D", "Empoli", 10),
    ("Viti Mattia", "D", "Empoli", 9),
    ("Goglichidze Saba", "D", "Empoli", 7),
    ("Gyasi Emmanuel", "D", "Empoli", 8),
    ("Pezzella Giuseppe", "D", "Empoli", 8),
    ("Henderson Liam", "C", "Empoli", 7),
    ("Grassi Alberto", "C", "Empoli", 8),
    ("Maleh Youssef", "C", "Empoli", 7),
    ("Fazzini Jacopo", "C", "Empoli", 12),
    ("Anjorin Tino", "C", "Empoli", 8),
    ("Colombo Lorenzo", "A", "Empoli", 15),
    ("Esposito Sebastiano", "A", "Empoli", 16),
    ("Solbakken Ola", "A", "Empoli", 10),
    ("Pellegri Pietro", "A", "Empoli", 9),
    # Fiorentina
    ("De Gea David", "P", "Fiorentina", 16),
    ("Terracciano Pietro", "P", "Fiorentina", 11),
    ("Comiri Lucas", "D", "Fiorentina", 10),
    ("Ranieri Luca", "D", "Fiorentina", 11),
    ("Pongracic Marin", "D", "Fiorentina", 9),
    ("Biraghi Cristiano", "D", "Fiorentina", 12),
    ("Dodo", "D", "Fiorentina", 12),
    ("Gosens Robin", "D", "Fiorentina", 17),
    ("Cataldi Danilo", "C", "Fiorentina", 11),
    ("Bove Edoardo", "C", "Fiorentina", 14),
    ("Mandragora Rolando", "C", "Fiorentina", 10),
    ("Richardson Amir", "C", "Fiorentina", 9),
    ("Colpani Andrea", "C", "Fiorentina", 18),
    ("Adli Yacine", "C", "Fiorentina", 13),
    ("Kean Moise", "A", "Fiorentina", 24),
    ("Gudmundsson Albert", "A", "Fiorentina", 26),
    ("Beltran Lucas", "A", "Fiorentina", 16),
    ("Ikone Jonathan", "A", "Fiorentina", 10),
    # Genoa
    ("Gollini Pierluigi", "P", "Genoa", 13),
    ("Leali Nicola", "P", "Genoa", 2),
    ("Bani Mattia", "D", "Genoa", 10),
    ("Vasquez Johan", "D", "Genoa", 11),
    ("Vogliacco Alessandro", "D", "Genoa", 8),
    ("Sabelli Stefano", "D", "Genoa", 7),
    ("Martin Aaron", "D", "Genoa", 9),
    ("Badelj Milan", "C", "Genoa", 8),
    ("Frendrup Morten", "C", "Genoa", 14),
    ("Malinovskyi Ruslan", "C", "Genoa", 13),
    ("Thorsby Morten", "C", "Genoa", 7),
    ("Miretti Fabio", "C", "Genoa", 15),
    ("Messias Junior", "A", "Genoa", 16),
    ("Pinamonti Andrea", "A", "Genoa", 20),
    ("Vitinha", "A", "Genoa", 14),
    ("Ekuban Caleb", "A", "Genoa", 10),
    # Inter
    ("Sommer Yann", "P", "Inter", 16),
    ("Martinez Josep", "P", "Inter", 2),
    ("Bastoni Alessandro", "D", "Inter", 18),
    ("Pavard Benjamin", "D", "Inter", 15),
    ("Acerbi Francesco", "D", "Inter", 11),
    ("De Vrij Stefan", "D", "Inter", 10),
    ("Dimarco Federico", "D", "Inter", 22),
    ("Dumfries Denzel", "D", "Inter", 17),
    ("Barella Nicolò", "C", "Inter", 25),
    ("Çalhanoğlu Hakan", "C", "Inter", 28),
    ("Mkhitaryan Henrikh", "C", "Inter", 18),
    ("Frattesi Davide", "C", "Inter", 16),
    ("Zielinski Piotr", "C", "Inter", 17),
    ("Thuram Marcus", "A", "Inter", 32),
    ("Martínez Lautaro", "A", "Inter", 40),
    ("Taremi Mehdi", "A", "Inter", 22),
    ("Arnautovic Marko", "A", "Inter", 12),
    # Juventus
    ("Di Gregorio Michele", "P", "Juventus", 15),
    ("Perin Mattia", "P", "Juventus", 3),
    ("Bremer Gleison", "D", "Juventus", 17),
    ("Gatti Federico", "D", "Juventus", 12),
    ("Kalulu Pierre", "D", "Juventus", 11),
    ("Cambiaso Andrea", "D", "Juventus", 16),
    ("Locatelli Manuel", "C", "Juventus", 13),
    ("Thuram Khéphren", "C", "Juventus", 14),
    ("Douglas Luiz", "C", "Juventus", 18),
    ("Koopmeiners Teun", "C", "Juventus", 26),
    ("Yildiz Kenan", "A", "Juventus", 20),
    ("Vlahovic Dusan", "A", "Juventus", 35),
    ("González Nicolás", "A", "Juventus", 22),
    ("Conçeicao Francisco", "A", "Juventus", 18),
    # Lazio
    ("Provedel Ivan", "P", "Lazio", 15),
    ("Mandas Christos", "P", "Lazio", 5),
    ("Gila Mario", "D", "Lazio", 11),
    ("Romagnoli Alessio", "D", "Lazio", 13),
    ("Patric", "D", "Lazio", 8),
    ("Lazzari Manuel", "D", "Lazio", 10),
    ("Marusic Adam", "D", "Lazio", 9),
    ("Nuno Tavares", "D", "Lazio", 14),
    ("Guendouzi Mattéo", "C", "Lazio", 17),
    ("Rovella Nicolò", "C", "Lazio", 12),
    ("Vecino Matias", "C", "Lazio", 11),
    ("Dele-Bashiru Fisayo", "C", "Lazio", 9),
    ("Castrovilli Gaetano", "C", "Lazio", 10),
    ("Zaccagni Mattia", "A", "Lazio", 24),
    ("Isaksen Gustav", "A", "Lazio", 13),
    ("Pedro", "A", "Lazio", 11),
    ("Castellanos Taty", "A", "Lazio", 22),
    ("Dia Boulaye", "A", "Lazio", 25),
    # Lecce
    ("Falcone Wladimiro", "P", "Lecce", 13),
    (" Früchtl Christian", "P", "Lecce", 1),
    ("Baschirotto Federico", "D", "Lecce", 11),
    ("Gaspar Kialonda", "D", "Lecce", 10),
    ("Gallo Antonino", "D", "Lecce", 9),
    ("Guilbert Frédéric", "D", "Lecce", 8),
    ("Ramadani Ylber", "C", "Lecce", 10),
    ("Coulibaly Lassana", "C", "Lecce", 8),
    ("Rafia Hamza", "C", "Lecce", 7),
    ("Berisha Medon", "C", "Lecce", 6),
    ("Morente Tete", "A", "Lecce", 11),
    ("Banda Lameck", "A", "Lecce", 12),
    ("Krstovic Nikola", "A", "Lecce", 18),
    ("Pierotti Santiago", "A", "Lecce", 8),
    ("Rebić Ante", "A", "Lecce", 14),
    # Milan
    ("Maignan Mike", "P", "Milan", 16),
    ("Sportiello Marco", "P", "Milan", 2),
    ("Theo Hernández", "D", "Milan", 22),
    ("Tomori Fikayo", "D", "Milan", 13),
    ("Thiaw Malick", "D", "Milan", 10),
    ("Pavlovic Strahinja", "D", "Milan", 11),
    ("Emerson Royal", "D", "Milan", 9),
    ("Gabbia Matteo", "D", "Milan", 10),
    ("Fofana Youssouf", "C", "Milan", 15),
    ("Reijnders Tijjani", "C", "Milan", 18),
    ("Loftus-Cheek Ruben", "C", "Milan", 16),
    ("Pulisic Christian", "C", "Milan", 25),
    ("Leão Rafael", "A", "Milan", 35),
    ("Morata Álvaro", "A", "Milan", 28),
    ("Abraham Tammy", "A", "Milan", 22),
    ("Okafor Noah", "A", "Milan", 14),
    ("Chukwueze Samuel", "A", "Milan", 12),
    # Monza
    ("Turati Stefano", "P", "Monza", 13),
    ("Pizzignacco Alessandro", "P", "Monza", 2),
    ("Pablo Marí", "D", "Monza", 10),
    ("Izzo Armando", "D", "Monza", 9),
    ("Carboni Andrea", "D", "Monza", 7),
    ("Pereira Pedro", "D", "Monza", 8),
    ("Kyriakopoulos Georgios", "D", "Monza", 9),
    ("Bondo Warren", "C", "Monza", 8),
    ("Pessina Matteo", "C", "Monza", 14),
    ("Akpa Akpro Jean-Daniel", "C", "Monza", 6),
    ("Ciurria Patrick", "C", "Monza", 11),
    ("Maldini Daniel", "C", "Monza", 13),
    ("Caprari Gianluca", "A", "Monza", 12),
    ("Dany Mota", "A", "Monza", 14),
    ("Đurić Milan", "A", "Monza", 15),
    ("Capitani Omari", "A", "Monza", 6),
    # Napoli
    ("Meret Alex", "P", "Napoli", 14),
    ("Caprile Elia", "P", "Napoli", 4),
    ("Di Lorenzo Giovanni", "D", "Napoli", 17),
    ("Buongiorno Alessandro", "D", "Napoli", 16),
    ("Rrahmani Amir", "D", "Napoli", 12),
    ("Olivera Mathias", "D", "Napoli", 9),
    ("Spinazzola Leonardo", "D", "Napoli", 10),
    ("Lobotka Stanislav", "C", "Napoli", 15),
    ("Anguissa Frank", "C", "Napoli", 14),
    ("McTominay Scott", "C", "Napoli", 24),
    ("Gilmour Billy", "C", "Napoli", 10),
    ("Kvaratskhelia Khvicha", "A", "Napoli", 36),
    ("Lukaku Romelu", "A", "Napoli", 34),
    ("Politano Matteo", "A", "Napoli", 16),
    ("Neres David", "A", "Napoli", 22),
    ("Raspadori Giacomo", "A", "Napoli", 14),
    # Parma
    ("Suzuki Zion", "P", "Parma", 12),
    ("Chichizola Leandro", "P", "Parma", 2),
    ("Delprato Enrico", "D", "Parma", 10),
    ("Circati Alessandro", "D", "Parma", 9),
    ("Balogh Botond", "D", "Parma", 7),
    ("Valeri Emanuele", "D", "Parma", 8),
    ("Coulibaly Woyo", "D", "Parma", 7),
    ("Bernabé Adrián", "C", "Parma", 15),
    ("Estevez Nahuel", "C", "Parma", 11),
    ("Sohm Simon", "C", "Parma", 8),
    ("Hernani", "C", "Parma", 9),
    ("Man Dennis", "A", "Parma", 22),
    ("Mihaila Valentin", "A", "Parma", 13),
    ("Bonny Ange-Yoan", "A", "Parma", 14),
    ("Charpentier Gabriel", "A", "Parma", 8),
    ("Almqvist Pontus", "A", "Parma", 10),
    # Roma
    ("Svilar Mile", "P", "Roma", 15),
    ("Ryan Mathew", "P", "Roma", 1),
    ("Mancini Gianluca", "D", "Roma", 13),
    ("Ndicka Evan", "D", "Roma", 11),
    ("Hummels Mats", "D", "Roma", 10),
    ("Angelino", "D", "Roma", 11),
    ("Hermoso Mario", "D", "Roma", 12),
    ("Cristante Bryan", "C", "Roma", 12),
    ("Pellegrini Lorenzo", "C", "Roma", 17),
    ("Paredes Leandro", "C", "Roma", 11),
    ("Koné Manu", "C", "Roma", 15),
    ("Saelemaekers Alexis", "C", "Roma", 12),
    ("Dybala Paulo", "A", "Roma", 32),
    ("Soulé Matias", "A", "Roma", 22),
    ("Dovbyk Artem", "A", "Roma", 28),
    # Torino
    ("Milinković-Savić Vanja", "P", "Torino", 14),
    ("Paleari Alberto", "P", "Torino", 2),
    ("Coco Saul", "D", "Torino", 11),
    ("Maripan Guillermo", "D", "Torino", 10),
    ("Masina Adam", "D", "Torino", 8),
    ("Vojvoda Mergim", "D", "Torino", 7),
    ("Lazaro Valentino", "D", "Torino", 9),
    ("Ricci Samuele", "C", "Torino", 13),
    ("Ilic Ivan", "C", "Torino", 12),
    ("Linetty Karol", "C", "Torino", 7),
    ("Vlasic Nikola", "C", "Torino", 16),
    ("Casale Nicolò", "D", "Torino", 9),
    ("Zapata Duvan", "A", "Torino", 30),
    ("Sanabria Antonio", "A", "Torino", 15),
    ("Adams Che", "A", "Torino", 18),
    ("Karamoh Yann", "A", "Torino", 7),
    # Udinese
    ("Okoye Maduka", "P", "Udinese", 13),
    ("Sava Razvan", "P", "Udinese", 2),
    ("Bijol Jaka", "D", "Udinese", 12),
    ("Giannetti Lautaro", "D", "Udinese", 8),
    ("Kabasele Christian", "D", "Udinese", 7),
    ("Kamara Hassane", "D", "Udinese", 8),
    ("Ehizibue Kingsley", "D", "Udinese", 8),
    ("Zemura Jordan", "D", "Udinese", 7),
    ("Lovric Sandi", "C", "Udinese", 11),
    ("Payero Martin", "C", "Udinese", 10),
    ("Karlstrom Jesper", "C", "Udinese", 9),
    ("Atta Jurgen", "C", "Udinese", 8),
    ("Thauvin Florian", "A", "Udinese", 22),
    ("Lucca Lorenzo", "A", "Udinese", 19),
    ("Davis Keinan", "A", "Udinese", 12),
    ("Brenner", "A", "Udinese", 10),
    # Venezia
    ("Stankovic Filip", "P", "Venezia", 11),
    ("Joronen Jesse", "P", "Venezia", 2),
    ("Idzes Jay", "D", "Venezia", 10),
    ("Svoboda Michael", "D", "Venezia", 8),
    ("Candela Antonio", "D", "Venezia", 7),
    ("Haps Ridgeciano", "D", "Venezia", 7),
    ("Zampano Francesco", "D", "Venezia", 7),
    ("Nicolussi Caviglia Hans", "C", "Venezia", 11),
    ("Duncan Alfred", "C", "Venezia", 10),
    ("Busio Gianluca", "C", "Venezia", 9),
    ("Ellertsson Mikael", "C", "Venezia", 8),
    ("Pohjanpalo Joel", "A", "Venezia", 20),
    ("Gytkjaer Christian", "A", "Venezia", 11),
    ("Oristanio Gaetano", "A", "Venezia", 13),
    ("Yeboah John", "A", "Venezia", 10),
    # Verona
    ("Montipò Lorenzo", "P", "Verona", 13),
    ("Perilli Simone", "P", "Verona", 1),
    ("Dawidowicz Pawel", "D", "Verona", 8),
    ("Coppola Diego", "D", "Verona", 9),
    ("Magnani Giangiacomo", "D", "Verona", 7),
    ("Bradaric Domagoj", "D", "Verona", 8),
    ("Tchatchoua Jackson", "D", "Verona", 9),
    ("Belahyane Reda", "C", "Verona", 9),
    ("Duda Ondrej", "C", "Verona", 10),
    ("Serdar Suat", "C", "Verona", 8),
    ("Suslov Tomas", "C", "Verona", 15),
    ("Harroui Abdou", "C", "Verona", 9),
    ("Tengstedt Casper", "A", "Verona", 14),
    ("Mosquera Amin", "A", "Verona", 11),
    ("Livramento Dailon", "A", "Verona", 10),
    ("Sarr Junior", "A", "Verona", 8),
]

df_listone = pd.DataFrame(
    giocatori_data, columns=["Giocatore", "Ruolo", "Squadra", "Quotazione"]
)

if scelta == "📋 Listone Serie A":
    st.header(
        f"📋 Listone Ufficiale Giocatori Serie A (Totale: {len(df_listone)}"
        " giocatori di tutte le 20 squadre)"
    )
    st.markdown(
        "Cerca e filtra i giocatori per ruolo o per qualsiasi squadra della"
        " Serie A."
    )

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
