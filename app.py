import streamlit as st
import pandas as pd
import random
import time

# --- CONFIGURAZIONE ---
st.set_page_config(page_title="CORE Intelligence", page_icon="🍷", layout="centered")

# --- CSS PROFESSIONALE ---
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    h1, h2, h3 { color: #800020 !important; }
    .stButton>button { 
        background-color: #800020 !important; color: white !important; 
        border-radius: 25px; font-weight: bold; border: none; height: 3.5em;
    }
    .step-box {
        padding: 20px; border-radius: 15px; border: 1px solid #eee;
        background-color: #fcfcfc; margin-bottom: 20px;
    }
    .brand-card {
        background: #fff4f6; padding: 15px; border-radius: 10px;
        border-left: 5px solid #800020; margin-bottom: 15px;
    }
    .metric-value { color: #800020; font-size: 24px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# --- DATABASE INTELLIGENCE BRAND ---
BRAND_DB = {
    "Lusso": [
        {"nome": "Hermès", "focus": "Flagship >150mq", "contatto": "Expansion Manager EMEA"},
        {"nome": "Cartier", "focus": "Corner high-traffic", "contatto": "Retail Director Italy"},
        {"nome": "Loro Piana", "focus": "Location storiche", "contatto": "Head of Real Estate"}
    ],
    "Fashion Premium": [
        {"nome": "Stone Island", "focus": "Industrial chic style", "contatto": "Global Retail Manager"},
        {"nome": "Golden Goose", "focus": "Vetrine visibili", "contatto": "Acquisition Specialist"},
        {"nome": "Ami Paris", "focus": "Quartieri creativi", "contatto": "Leasing Manager"}
    ],
    "Mass Market": [
        {"nome": "Uniqlo", "focus": "Grandi superfici >1000mq", "contatto": "Property Manager"},
        {"nome": "Mango", "focus": "High Street", "contatto": "Expansion Dept"},
        {"nome": "Zara Home", "focus": "Retail parks o center", "contatto": "Inditex Group Real Estate"}
    ],
    "Food": [
        {"nome": "Starbucks", "focus": "Angoli visibili", "contatto": "Licensing Manager"},
        {"nome": "Iginio Massari", "focus": "Luxury high street", "contatto": "Sviluppo Retail"},
        {"nome": "Nespresso", "focus": "Location prestigio", "contatto": "Boutique Expansion"}
    ]
}

# --- STATO DELL'APP ---
if 'step' not in st.session_state: st.session_state.step = 1
if 'data' not in st.session_state: st.session_state.data = {}

def avanti(): st.session_state.step += 1
def reset(): st.session_state.step = 1

# --- HEADER ---
st.title("🍷 CORE Intelligence")
st.write(f"**Step {st.session_state.step} di 3**")
st.progress(st.session_state.step / 3)

# --- STEP 1: DATI TECNICI ---
if st.session_state.step == 1:
    st.subheader("📍 Fase 1: Identificazione Asset")
    with st.container():
        st.markdown('<div class="step-box">', unsafe_allow_html=True)
        st.session_state.data['via'] = st.text_input("Indirizzo Immobile", "Via Montenapoleone, Milano")
        st.session_state.data['target'] = st.selectbox("Cluster Target", list(BRAND_DB.keys()))
        c1, c2 = st.columns(2)
        st.session_state.data['mq_pt'] = c1.number_input("Mq Piano Terra", value=100)
        st.session_state.data['mq_mag'] = c2.number_input("Mq Magazzino", value=50)
        st.markdown('</div>', unsafe_allow_html=True)
        st.button("Procedi ai Dati Economici ➡️", on_click=avanti)

# --- STEP 2: DATI ECONOMICI ---
elif st.session_state.step == 2:
    st.subheader("💰 Fase 2: Analisi Finanziaria")
    with st.container():
        st.markdown('<div class="step-box">', unsafe_allow_html=True)
        st.session_state.data['canone'] = st.number_input("Canone Annuo richiesto (€)", value=200000)
        st.session_state.data['key_money'] = st.number_input("Key Money / Buonuscita (€)", value=150000)
        st.info("L'algoritmo calcolerà il valore al mq basato sulla superficie pesata (PT + 30% Magazzino).")
        st.markdown('</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        col1.button("⬅️ Indietro", on_click=lambda: setattr(st.session_state, 'step', 1))
        col2.button("Genera Matchmaking AI 🚀", on_click=avanti)

# --- STEP 3: ANALISI E BRAND MATCH ---
elif st.session_state.step == 3:
    st.subheader("🎯 Fase 3: Analisi Brand & Matchmaking")
    
    # Calcoli
    d = st.session_state.data
    mq_comm = d['mq_pt'] + (d['mq_mag'] * 0.3)
    valore_mq = d['canone'] / mq_comm
    
    # Report Sintetico
    c1, c2 = st.columns(2)
    c1.metric("Mq Commerciali", f"{mq_comm:.1f} mq")
    c2.metric("Valore al Mq", f"€ {valore_mq:,.0f}")

    st.divider()
    
    st.markdown("### 🏆 Top Brand Match (Da Contattare)")
    st.write(f"In base al cluster **{d['target']}**, ecco i brand con strategie compatibili:")

    matches = BRAND_DB.get(d['target'], [])
    for b in matches:
        with st.container():
            st.markdown(f"""
            <div class="brand-card">
                <div style="display: flex; justify-content: space-between;">
                    <span style="font-size: 1.2em; font-weight: bold; color: #800020;">{b['nome']}</span>
                    <span style="background: #800020; color: white; padding: 2px 10px; border-radius: 10px; font-size: 0.8em;">MATCH 95%</span>
                </div>
                <p style="margin: 5px 0;"><b>Focus:</b> {b['focus']}</p>
                <p style="margin: 0; color: #555;">👤 <b>Contatto Suggerito:</b> {b['contatto']}</p>
            </div>
            """, unsafe_allow_html=True)

    st.divider()
    if st.button("🔄 Nuova Analisi"):
        reset()
        st.rerun()
