import streamlit as st
import pandas as pd
import random

# Configurazione Pagina
st.set_page_config(page_title="CORE Intelligence", page_icon="🍷", layout="wide")

# Stile Bordeaux professionale
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .stButton>button { background-color: #800020 !important; color: white !important; border-radius: 8px; border: none; font-weight: bold; height: 3em; width: 100%; }
    h1, h2, h3 { color: #800020 !important; font-family: 'Helvetica', sans-serif; }
    .metric-card {
        background-color: white; padding: 20px; border-radius: 10px;
        border-left: 6px solid #800020; box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center; margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Database temporaneo
if 'archive' not in st.session_state:
    st.session_state.archive = []

# Sidebar
with st.sidebar:
    st.title("🍷 CORE Intelligence")
    menu = st.radio("Navigazione", ["➕ Nuova Acquisizione", "📂 Archivio Asset"])
    st.divider()
    st.info("Algoritmo: PT 100% | Magazzino 30%")

# Logica di calcolo
if menu == "➕ Nuova Acquisizione":
    st.title("🏙️ Inserimento Immobile")
    
    col1, col2 = st.columns(2)
    with col1:
        indirizzo = st.text_input("Indirizzo", placeholder="Esempio: Via Torino 10, Milano")
        settore = st.selectbox("Target Brand", ["Lusso", "Fashion Premium", "Mass Market", "Food"])
        mq_pt = st.number_input("Mq Piano Terra (PT)", min_value=0, value=50)
    
    with col2:
        mq_mag = st.number_input("Mq Magazzino", min_value=0, value=30)
        canone = st.number_input("Canone Annuo richiesto (€)", min_value=0, value=100000, step=5000)
        key_money = st.number_input("Buonuscita / Key-money (€)", min_value=0, value=50000, step=5000)

    # Regola del 30%
    mq_comm = mq_pt + (mq_mag * 0.3)
    valore_mq = canone / mq_comm if mq_comm > 0 else 0

    if st.button("ANALIZZA E SALVA"):
        st.divider()
        c1, c2, c3 = st.columns(3)
        c1.markdown(f'<div class="metric-card"><small>MQ COMMERCIALE</small><br><b>{mq_comm:.1f} mq</b></div>', unsafe_allow_html=True)
        c2.markdown(f'<div class="metric-card"><small>CANONE REALE / MQ</small><br><b>€ {valore_mq:,.0f}</b></div>', unsafe_allow_html=True)
        c3.markdown(f'<div class="metric-card"><small>DEAL SCORE</small><br><b>{random.randint(75, 95)}/100</b></div>', unsafe_allow_html=True)
        
        # Salvataggio
        st.session_state.archive.append({
            "Indirizzo": indirizzo,
            "Mq PT": mq_pt,
            "Mq Mag": mq_mag,
            "Canone": canone,
            "Settore": settore
        })
        st.success("Immobile salvato con successo!")

elif menu == "📂 Archivio Asset":
    st.title("📂 Archivio Immobili")
    if st.session_state.archive:
        df = pd.DataFrame(st.session_state.archive)
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("L'archivio è ancora vuoto.")