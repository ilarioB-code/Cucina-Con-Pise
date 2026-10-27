import streamlit as st
import random

# Configurazione Pagina
st.set_page_config(page_title="Tuscan Meal Planner & Spesa Smart", page_icon="🍲", layout="wide")

st.title("🍲 Tuscan Meal Planner & Schiscetta Smart")
st.caption("Cucina toscana e mediterranea, zero noia, zero appesantimento e spesa sotto controllo.")

# --- DATABASE INGREDIENTI E PREZZI (al kg o al pezzo) ---
ANAGRAFICA_SPESA = {
    # Proteine
    "Pollo (Petto/Bocconcini)": {"categoria": "Proteine", "prezzo_unita": 9.50, "unita": "kg"},
    "Tacchino (Straccetti)": {"categoria": "Proteine", "prezzo_unita": 10.50, "unita": "kg"},
    "Maiale (Lonza/Arista)": {"categoria": "Proteine", "prezzo_unita": 8.00, "unita": "kg"},
    "Manzo (Macinato magro)": {"categoria": "Proteine", "prezzo_unita": 14.00, "unita": "kg"},
    "Ceci (barattolo)": {"categoria": "Proteine", "prezzo_unita": 1.50, "unita": "confezione"},
    "Fagioli Cannellini (barattolo)": {"categoria": "Proteine", "prezzo_unita": 1.50, "unita": "confezione"},
    "Uova": {"categoria": "Proteine", "prezzo_unita": 2.50, "unita": "confezione (6pz)"},
    
    # Carboidrati & Dispensa
    "Riso Basmati": {"categoria": "Carboidrati", "prezzo_unita": 3.00, "unita": "kg"},
    "Pasta corta (Fusilli/Penne)": {"categoria": "Carboidrati", "prezzo_unita": 1.80, "unita": "kg"},
    "Pane di grano duro / Crostini": {"categoria": "Carboidrati", "prezzo_unita": 2.50, "unita": "kg"},
    "Patate": {"categoria": "Carboidrati", "prezzo_unita": 1.50, "unita": "kg"},
    "Piadine / Wrap integrali": {"categoria": "Carboidrati", "prezzo_unita": 2.00, "unita": "confezione"},
    
    # Verdure
    "Zucchine": {"categoria": "Verdure", "prezzo_unita": 2.50, "unita": "kg"},
    "Spinaci freschi": {"categoria": "Verdure", "prezzo_unita": 4.00, "unita": "kg"},
    "Carote e Finocchi": {"categoria": "Verdure", "prezzo_unita": 2.20, "unita": "kg"},
    "Melanzane / Peperoni": {"categoria": "Verdure", "prezzo_unita": 2.80, "unita": "kg"},
    "Pomodorini": {"categoria": "Verdure", "prezzo_unita": 3.50, "unita": "kg"}
}

# --- DATABASE RICETTE ---
RICETTE_CENA = [
    {
        "nome": "Bocconcini di pollo al rosmarino, limone e vino bianco con patate",
        "proteina": "Pollo (Petto/Bocconcini)", "carbo": "Patate", "verdura": "Zucchine",
        "tempo": "25 min", "difficoltà": "Facile",
        "passaggi": "1. Taglia le patate a cubetti e cuocile in padella con un filo d'olio e sale (15 min).\n2. Infarina leggermente i bocconcini di pollo e rosolali in un'altra padella con aglio e abbondante rosmarino fresco.\n3. Sfuma con vino bianco e succo di limone.\n4. Unisci tutto e servi ben caldo."
    },
    {
        "nome": "Straccetti di tacchino con salvia e pomodorini su crema di cannellini",
        "proteina": "Tacchino (Straccetti)", "carbo": "Pane di grano duro / Crostini", "verdura": "Spinaci freschi",
        "tempo": "20 min", "difficoltà": "Facile",
        "passaggi": "1. Frulla metà dei cannellini in barattolo con un goccio d'acqua, sale, pepe e un rametto di salvia.\n2. In padella scotta gli spinaci freschi con un filo d'olio (5 min).\n3. Cuoci gli straccetti di tacchino a fiamma viva con foglie di salvia e aglio.\n4. Componi il piatto stendendo la crema di cannellini sotto, il tacchino sopra e accompagna con pane tostato."
    },
    {
        "nome": "Arista di maiale al finocchietto con carote glassate",
        "proteina": "Maiale (Lonza/Arista)", "carbo": "Riso Basmati", "verdura": "Carote e Finocchi",
        "tempo": "20 min", "difficoltà": "Facile",
        "passaggi": "1. Metti a lessare il riso basmati.\n2. Taglia finemente carote e finocchi.\n3. Rosola le fettine sottili di maiale in padella con semi di finocchietto selvatico, sfumando con vino bianco. Unisci le verdure e fai cuocere insieme."
    },
    {
        "nome": "Polpette magre di manzo al timo con pomodorini saltati",
        "proteina": "Manzo (Macinato magro)", "carbo": "Pasta corta (Fusilli/Penne)", "verdura": "Pomodorini",
        "tempo": "30 min", "difficoltà": "Media",
        "passaggi": "1. Impasta il macinato di manzo con sale, pepe e foglioline di timo fresco, formando piccole polpette.\n2. Metti su l'acqua per la pasta.\n3. In padella scotta i pomodorini tagliati a metà, poi unisci le polpette e rosolale bene su tutti i lati.\n4. Scola la pasta al dente e saltala direttamente nella padella con le polpette."
    },
    {
        "nome": "Zuppa espressa di ceci, rosmarino e pasta corta",
        "proteina": "Ceci (barattolo)", "carbo": "Pasta corta (Fusilli/Penne)", "verdura": "Spinaci freschi",
        "tempo": "20 min", "difficoltà": "Facile",
        "passaggi": "1. In una pentola fai un soffritto veloce con aglio, rosmarino tritato e un pizzico di peperoncino.\n2. Aggiungi i ceci scolati e metà acqua.\n3. Schiaccia una parte di ceci con la forchetta per creare una cremina.\n4. Butta la pasta direttamente nella pentola allungando con acqua bollente finché è cotta."
    }
]

RICETTE_PRANZO = [
    {
        "nome": "Riso basmati ripassato con straccetti di tacchino, zucchine e limone",
        "proteina": "Tacchino (Straccetti)", "carbo": "Riso Basmati", "verdura": "Zucchine",
        "tempo": "15 min (Schiscetta da scaldare)",
        "passaggi": "1. Taglia le zucchine a rondelle sottili.\n2. In padella salta gli straccetti di tacchino con le zucchine.\n3. Unisci il riso basmati già cotto, un goccio d'olio e scorza di limone grattugiata.\n4. Metti nella schiscetta (al microonde: 2 minuti a media potenza)."
    },
    {
        "nome": "Pasta fredda/tiepida con crema di ceci, pepe nero e rosmarino",
        "proteina": "Ceci (barattolo)", "carbo": "Pasta corta (Fusilli/Penne)", "verdura": "Spinaci freschi",
        "tempo": "15 min (Schiscetta)",
        "passaggi": "1. Frulla i ceci con un filo d'olio, sale e pepe nero.\n2. Scola la pasta al dente e condiscila con la crema di ceci e foglioline di spinaci freschi.\n3. Perfetta da scaldare al microonde o mangiare tiepida."
    },
    {
        "nome": "Insalata tiepida di patate, bocconcini di pollo dorati e pomodorini",
        "proteina": "Pollo (Petto/Bocconcini)", "carbo": "Patate", "verdura": "Pomodorini",
        "tempo": "20 min (Schiscetta)",
        "passaggi": "1. Taglia e cuoci le patate a cubetti in padella.\n2. Rosola i bocconcini di pollo con origano.\n3. Unisci i pomodorini freschi a metà. Ottima sia calda che tiepida."
    },
    {
        "nome": "Crostini toscani con cannellini all'uccelletto e lonza",
        "proteina": "Fagioli Cannellini (barattolo)", "carbo": "Pane di grano duro / Crostini", "verdura": "Pomodorini",
        "tempo": "15 min (Schiscetta)",
        "passaggi": "1. In padella scalda i fagioli cannellini con un cucchiaio di passata di pomodoro o pomodorini, aglio e salvia.\n2. Taglia la lonza di maiale a listarelle e scottala velocemente.\n3. Componi la schiscetta mettendo i crostini di pane alla base e coprendo con i fagioli e la carne."
    },
    {
        "nome": "Wrap/Piadina arrotolata con macinato di manzo speziato e verdure",
        "proteina": "Manzo (Macinato magro)", "carbo": "Piadine / Wrap integrali", "verdura": "Spinaci freschi",
        "tempo": "15 min (Schiscetta)",
        "passaggi": "1. Rosola il macinato di manzo in padella con timo, sale e pepe.\n2. Scalda la piadina, farciscila con spinaci freschi e il macinato caldo, poi arrotolala.\n3. Tagliala a metà nella schiscetta."
    }
]

# --- GESTIONE PERSISTENZA STATO (SESSION STATE) ---
if "menu_attivo" not in st.session_state:
    st.session_state["menu_attivo"] = None

def genera_nuovo_menu():
    giorni = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì"]
    menu = []
    proteine_usate = []
    
    for g in giorni:
        censioni_disponibili = [r for r in RICETTE_CENA if not proteine_usate or r["proteina"] != proteine_usate[-1]]
        cena_scelta = random.choice(censioni_disponibili)
        proteine_usate.append(cena_scelta["proteina"])
        
        pranzi_disponibili = [r for r in RICETTE_PRANZO if r["proteina"] != cena_scelta["proteina"]]
        pranzo_scelto = random.choice(pranzi_disponibili)
        
        menu.append({
            "Giorno": g,
            "Pranzo": pranzo_scelto,
            "Cena": cena_scelta
        })
    st.session_state["menu_attivo"] = menu
    # Resetta eventuali spunte della spesa precedenti quando si cambia settimana
    keys_da_rimuovere = [k for k in st.session_state.keys() if k.startswith("spesa_")]
    for k in keys_da_rimuovere:
        del st.session_state[k]

# Genera automaticamente un menù iniziale se non esiste
if st.session_state["menu_attivo"] is None:
    genera_nuovo_menu()

# --- TABS APP ---
tab1, tab2, tab3 = st.tabs(["📅 Menù Settimanale & Spesa", "🧊 Svuota Frigo", "📖 Ricettario Semplice"])

# --- TAB 1: MENU & SPESA ---
with tab1:
    st.header("Generatore di Menù per il Lavoro")
    
    # Sezione di controllo per la pianificazione settimanale
    with st.expander("⚙️ Gestione Pianificazione Settimanale (Clicca per rigenerare il menù nel fine settimana)"):
        st.write("Il menù rimane bloccato finché non decidi di pianificare la settimana nuova (es. il venerdì sera o nel weekend).")
        if st.button("🔄 Genera Nuovo Menù per la prossima settimana"):
            genera_nuovo_menu()
            st.rerun()

    if st.session_state["menu_attivo"]:
        st.subheader("📋 Il tuo Programma Settimanale (Lunedì - Venerdì)")
        
        fabbisogno_spesa = {}
        
        for item in st.session_state["menu_attivo"]:
            giorno = item["Giorno"]
            pranzo = item["Pranzo"]
            cena = item["Cena"]
            
            for p_item in [pranzo["proteina"], pranzo["carbo"], pranzo.get("verdura", "Spinaci freschi")]:
                if p_item in ANAGRAFICA_SPESA:
                    fabbisogno_spesa[p_item] = fabbisogno_spesa.get(p_item, 0) + 1
            for c_item in [cena["proteina"], cena["carbo"], cena["verdura"]]:
                if c_item in ANAGRAFICA_SPESA:
                    fabbisogno_spesa[c_item] = fabbisogno_spesa.get(c_item, 0) + 1

            with st.expander(f"📌 {giorno}"):
                c1, c2 = st.columns(2)
                
                with c1:
                    st.markdown(f"**☀️ Pranzo (Schiscetta):** {pranzo['nome']}")
                    with st.expander("🔍 Dettagli & Ricetta Pranzo"):
                        st.write(f"⏱ **Tempo:** {pranzo['tempo']}")
                        st.write(f"🥩 **Proteina:** {pranzo['proteina']} | 🌾 **Carbo:** {pranzo['carbo']}")
                        st.text("Preparazione:\n" + pranzo["passaggi"])
                
                with c2:
                    st.markdown(f"**🌙 Cena (Fresca):** {cena['nome']}")
                    with st.expander("🔍 Dettagli & Ricetta Cena"):
                        st.write(f"⏱ **Tempo:** {cena['tempo']} | 📊 **Difficoltà:** {cena['difficoltà']}")
                        st.write(f"🌿 **Aromi consigliati:** Aglio, rosmarino, salvia, vino bianco, olio EVO")
                        st.text("Preparazione:\n" + cena["passaggi"])

        st.markdown("---")
        st.subheader("🛒 Lista della Spesa Intelligente")
        st.info("💡 Spunta gli ingredienti che **hai già in casa**: il prezzo totale si aggiornerà in tempo reale!")

        totale_effettivo = 0.0
        
        categorie = {"Proteine": [], "Carboidrati": [], "Verdure": []}
        for ing in fabbisogno_spesa.keys():
            cat = ANAGRAFICA_SPESA[ing]["categoria"]
            categorie[cat].append(ing)

        col_s1, col_s2, col_s3 = st.columns(3)
        colonne_cat = [col_s1, col_s2, col_s3]
        
        idx = 0
        for cat, ingredienti in categorie.items():
            with colonne_cat[idx]:
                st.markdown(f"### 📦 {cat}")
                for ing in sorted(ingredienti):
                    info = ANAGRAFICA_SPESA[ing]
                    prezzo_unitario = info["prezzo_unita"]
                    unita_misura = info["unita"]
                    
                    ck_key = f"spesa_{ing}"
                    gia_in_casa = st.checkbox(f"**{ing}** (~€{prezzo_unitario:.2f} / {unita_misura})", key=ck_key)
                    
                    if not gia_in_casa:
                        totale_effettivo += prezzo_unitario
            idx += 1

        st.markdown("---")
        st.metric(label="💰 Costo Totale Stimato della Spesa da Fare", value=f"€ {totale_effettivo:.2f}")

# --- TAB 2: SVUOTA FRIGO ---
with tab2:
    st.header("🧊 Svuota Frigo Smart")
    st.write("Seleziona cosa ti è rimasto in giro tra frigo e dispensa per trovare un'idea al volo:")
    
    tutti_ingredienti = list(ANAGRAFICA_SPESA.keys())
    ing_selezionati = st.multiselect("Seleziona ingredienti disponibili:", tutti_ingredienti)
    
    if st.button("🔎 Genera Piatto Svuota-Frigo"):
        if ing_selezionati:
            st.success(f"Combinazione trovata con: {', '.join(ing_selezionati)}")
            st.markdown("""
            **🍳 Idea Chef Tuscan-Style:**
            * **Padella rapida:** Taglia a cubetti gli ingredienti proteici e le verdure che hai selezionato. Scalda un filo d'olio in padella con uno spicchio d'aglio e un rametto di rosmarino o salvia. Fai saltare a fuoco vivo per 10 minuti, sfuma con un goccio di vino bianco se ce l'hai, e unisci la pasta o il riso lessato a parte. 
            * **Tocco finale:** Un giro d'olio extravergine a crudo e una spolverata di pepe nero.
            """)
        else:
            st.warning("Seleziona almeno un ingrediente per ricevere un'idea!")

# --- TAB 3: RICETTARIO ---
with tab3:
    st.header("📖 Libretto Consigli & Trucchi in Cucina")
    st.markdown("""
    * **🔥 La Reazione di Maillard (La crosticina saporita):** Quando cuoci pollo, tacchino o maiale in padella, ricordati di tamponarli con carta da cucina prima di metterli in padella ben calda. Niente carne lessa o gommosa!
    * **🌿 Aromi Toscani Sempre Pronti:** Tieni sempre a portata di mano rosmarino, salvia e aglio. Cambiano completamente il volto a qualsiasi piatto povero o schiscetta da microonde.
    * **🍱 Gestione della Schiscetta al Microonde:** Quando riscaldi il pranzo in ufficio, aggiungi sempre un cucchiaino d'acqua o un filo d'olio sopra la pasta/riso e scalda a potenza media (circa 600W) per 2 minuti coprendo il contenitore, così non si secca la carne.
    """)
