import streamlit as st
import random

# Configurazione Pagina
st.set_page_config(page_title="Tuscan Meal Planner & SvuotaFrigo", page_icon="🍲", layout="wide")

st.title("🍲 Meal Planner & Schiscetta Smart")
st.caption("Cucina toscana e mediterranea, zero noia, zero appesantimento e spesa pronta!")

# --- DATABASE INGREDIENTI E RICETTE ---
PROTEINE = {
    "Pollo": {"prezzo_al_kg": 9.50, "unita": "g"},
    "Tacchino": {"prezzo_al_kg": 10.50, "unita": "g"},
    "Maiale (Lonza/Arista)": {"prezzo_al_kg": 8.00, "unita": "g"},
    "Manzo (Macinato/Bistecca)": {"prezzo_al_kg": 14.00, "unita": "g"},
    "Ceci": {"prezzo_al_kg": 3.00, "unita": "g"},
    "Fagioli Canellini/Borbotti": {"prezzo_al_kg": 3.00, "unita": "g"},
    "Uova": {"prezzo_unita": 0.35, "unita": "pz"}
}

RICETTE_CENA = [
    {
        "nome": "Bocconcini di pollo al rosmarino, limone e vino bianco con patate in padella",
        "proteina": "Pollo",
        "carbo": "Patate",
        "verdura": "Zucchine",
        "aromi": "Rosmarino, aglio, vino bianco, limone",
        "porzione_prot": 200, "porzione_carbo": 250,
        "preparazione": "Rosola il pollo a cubetti con aglio e rosmarino. Sfuma col vino, aggiungi limone e servi con patate a cubetti saltate in padella."
    },
    {
        "nome": "Straccetti di tacchino con salvia e pomodorini secchi su crema di cannellini",
        "proteina": "Tacchino",
        "carbo": "Pane / Crostini",
        "verdura": "Spinaci saltati",
        "aromi": "Salvia, aglio, olio EVO",
        "porzione_prot": 200, "porzione_carbo": 80,
        "preparazione": "Frulla i cannellini con salvia e un filo d'olio. Rosola il tacchino ad alta temperatura con salvia e unisci alla crema."
    },
    {
        "nome": "Arista di maiale rosolata al finocchietto con carote glasse e finocchi",
        "proteina": "Maiale (Lonza/Arista)",
        "carbo": "Riso Basmati",
        "verdura": "Carote e Finocchi",
        "aromi": "Finocchietto selvatico, vino bianco, pepe",
        "porzione_prot": 200, "porzione_carbo": 80,
        "preparazione": "Cuoci la lonza a fettine sottili in padella antiaderente con finocchietto e vino. Accompagna con carote a rondelle."
    },
    {
        "nome": "Polpette magre di manzo al timo e pomodoro fresco con melanzane",
        "proteina": "Manzo (Macinato/Bistecca)",
        "carbo": "Pasta / Crostini",
        "verdura": "Melanzane / Peperoni",
        "aromi": "Timo, aglio, alloro",
        "porzione_prot": 180, "porzione_carbo": 90,
        "preparazione": "Forma piccole polpette con sale, pepe e timo. Cuocile nel pomodoro fresco a fuoco vivo con foglie d'alloro."
    },
    {
        "nome": "Zuppa franta di ceci e fagioli con salvia, aglio e pasta corta",
        "proteina": "Ceci",
        "carbo": "Pasta",
        "verdura": "Bieta / Cicoria",
        "aromi": "Aglio, salvia, rosmarino, peperoncino",
        "porzione_prot": 150, "porzione_carbo": 80,
        "preparazione": "Soffriggi aglio e salvia, unisci i legumi, schiacciane una parte per fare la crema, allunga con acqua e cuoci la pasta dentro."
    }
]

RICETTE_PRANZO = [
    {
        "nome": "Riso basmati ripassato con straccetti di tacchino, zucchine e scorza di limone",
        "proteina": "Tacchino", "carbo": "Riso Basmati",
        "porzione_prot": 150, "porzione_carbo": 80
    },
    {
        "nome": "Fusilli integrali con crema di ceci, pepe nero e rosmarino croccante",
        "proteina": "Ceci", "carbo": "Pasta",
        "porzione_prot": 120, "porzione_carbo": 80
    },
    {
        "nome": "Insalata tiepida di patate, bocconcini di pollo dorati, origano e pomodorini",
        "proteina": "Pollo", "carbo": "Patate",
        "porzione_prot": 150, "porzione_carbo": 200
    },
    {
        "nome": "Crostini di pane tostato con cannellini all'uccelletto (pomodoro, salvia, aglio) e lonza",
        "proteina": "Fagioli Canellini/Borbotti", "carbo": "Pane / Crostini",
        "porzione_prot": 120, "porzione_carbo": 100
    },
    {
        "nome": "Wrap/Piadina integrale con macinato di manzo speziato al timo, insalata e maionese leggera",
        "proteina": "Manzo (Macinato/Bistecca)", "carbo": "Pane / Crostini",
        "porzione_prot": 130, "porzione_carbo": 100
    }
]

# --- TABS APP ---
tab1, tab2, tab3 = st.tabs(["📅 Menù Settimanale & Spesa", "🧊 Svuota Frigo", "📖 Ricettario Semplice"])

# --- TAB 1: MENU & SPESA ---
with tab1:
    st.header("Generatore di Menù per il Lavoro")
    
    if st.button("🎲 Genera Menù della Settimana (Lunedì - Venerdì)"):
        giorni = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì"]
        menu = []
        
        # Selezione casuale senza ripetizioni consecutive di proteina
        proteine_usate = []
        spesa_totale = {}

        for g in giorni:
            # Scegli ricette garantendo rotazione
            cena_scelta = random.choice([r for r in RICETTE_CENA if r["proteina"] not in proteine_usate[-1:]])
            pranzo_scelto = random.choice([r for r in RICETTE_PRANZO if r["proteina"] != cena_scelta["proteina"]])
            
            proteine_usate.append(cena_scelta["proteina"])
            
            menu.append({
                "Giorno": g,
                "Pranzo (Schiscetta)": pranzo_scelto["nome"],
                "Cena (Fresca 30min)": cena_scelta["nome"],
                "Aromi Cena": cena_scelta["aromi"]
            })
            
            # Calcolo quantitativi per la spesa
            for item in [cena_scelta, pranzo_scelto]:
                prot = item["proteina"]
                q = item["porzione_prot"]
                spesa_totale[prot] = spesa_totale.get(prot, 0) + q

        st.session_state["menu"] = menu
        st.session_state["spesa"] = spesa_totale

    if "menu" in st.session_state:
        st.subheader("📋 Il tuo programma settimanale")
        for item in st.session_state["menu"]:
            with st.expander(f"📌 {item['Giorno']}"):
                st.write(f"**☀️ Pranzo:** {item['Pranzo (Schiscetta)']}")
                st.write(f"**🌙 Cena:** {item['Cena (Fresca 30min)']}")
                st.caption(f"🌿 Aromi da usare la sera: {item['Aromi Cena']}")
        
        st.markdown("---")
        st.subheader("🛒 Lista della Spesa Automatica")
        
        costo_stimato_totale = 0.0
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Ingredienti Proteici da acquistare:**")
            for ing, grammi in st.session_state["spesa"].items():
                if ing in PROTEINE:
                    prezzo_kg = PROTEINE[ing].get("prezzo_al_kg", 0)
                    costo = (grammi / 1000) * prezzo_kg
                    costo_stimato_totale += costo
                    st.write(f"- **{ing}**: {grammi}g (circa €{costo:.2f})")
        
        with col2:
            st.write("**Basi da Dispensa & Verdure:**")
            st.write("- Riso Basmati, Pasta corta, Pane di grano duro")
            st.write("- Zucchine, Carote, Finocchi, Spinaci, Melanzane")
            st.write("- Aromi toscani: Rosmarino fresco, Salvia, Aglio, Timo, Limoni, Vino bianco")
            st.info(f"💰 **Costo stimato proteina fresca:** ~€{costo_stimato_totale:.2f} / settimana")

# --- TAB 2: SVUOTA FRIGO ---
with tab2:
    st.header("🧊 Svuota Frigo Smart")
    st.write("Seleziona gli ingredienti che hai in frigo o dispensa per trovare cosa cucinare stasera:")
    
    ing_selezionati = st.multiselect(
        "Cosa hai a disposizione?",
        ["Pollo", "Tacchino", "Maiale", "Manzo", "Ceci", "Fagioli", "Zucchine", "Patate", "Pasta", "Riso"]
    )
    
    if st.button("🔎 Trova Ricetta"):
        if ing_selezionati:
            st.success(f"Con **{', '.join(ing_selezionati)}** puoi fare:")
            st.markdown("""
            * **Padellata Tuscan-Style:** Rosola la proteina scelta con un trito di aglio e rosmarino. Aggiungi le verdure a cubetti, sfuma con un goccio di vino bianco e servi accompagnato da riso o pane tostato.
            * **Pasta Spadellata Creamy:** Frulla la metà dei legumi con olio, salvia e pepe. Salta la pasta in padella con la crema ottenuta e i pezzetti di carne dorati a parte.
            """)
        else:
            st.warning("Seleziona almeno un ingrediente!")

# --- TAB 3: RICETTARIO ---
with tab3:
    st.header("📖 Consigli di Cottura Veloci")
    st.markdown("""
    * **Il segreto della rosolatura (Reazione di Maillard):** Per non fare la carne 'lessa', asciuga sempre la superficie con carta da cucina prima di metterla nella padella ben calda con olio e rosmarino/salvia.
    * **Schiscetta perfetta al microonde:** Aggiungi sempre un cucchiaio d'acqua o un filo d'olio sulla schiscetta prima di scaldarla e usa la potenza media (600W) per 2 minuti invece del massimo per evitare di seccare la carne.
    """)
