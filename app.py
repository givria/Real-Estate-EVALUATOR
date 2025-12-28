import streamlit as st
import pandas as pd
import random

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="CORE Intelligence", page_icon="🍷", layout="centered")

# --- CSS PROFESSIONALE (Contrasto elevato e stile Bordeaux) ---
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    
    /* Titoli e sottotitoli */
    h1, h2, h3 { color: #800020 !important; font-weight: bold; }
    
    /* Forza il colore delle etichette (Label) dei campi - RISOLVE IL TUO PROBLEMA */
    .stWidget label {
        color: #1a1a1a !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        margin-bottom: 8px !important;
    }

    /* Stile dei bottoni */
    .stButton>button { 
        background-color: #800020 !important; 
        color: white !important; 
        border-radius: 25px; 
        font-weight: bold; 
        border: none; 
        height: 3.5em;
        width: 100%;
        margin-top: 20px;
    }

    /* Box dei risultati e delle card brand */
    .step-box {
        padding: 25px; 
        border-radius: 15px; 
        border: 1px solid #e0e0e0;
        background-color: #f9f9f9; 
        margin-bottom: 20px;
    }
    .brand-card {
        background: #fff4f6; 
        padding: 20px; 
        border-radius: 12px;
        border-left: 6px solid #800020; 
        margin-bottom: 15px;
        color: #333;
    }
    .metric-title { color: #666; font-size: 0.9em; text-transform: uppercase; }
    .metric-value { color: #800020; font-size: 1.8em; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# --- DATABASE INTELLIGENCE BRAND ---
BRAND_DB = {
    "Lusso": [
        {"nome": "Hermès", "focus": "Flagship High Street", "contatto": "Expansion Manager EMEA"},
        {"nome": "Cartier", "focus": "Corner prestigio / Boutique", "contatto": "Retail Director Italy"},
        {"nome": "Loro Piana", "focus": "Location storiche prime", "contatto": "Head of Real Estate"}
    ],
    "Fashion Premium": [
        {"nome": "Stone Island", "focus": "Concept store innovativi", "contatto": "Global Retail Manager"},
        {"nome": "Golden Goose", "focus": "Vetrine visibili", "contatto": "Acquisition Specialist"},
        {"nome": "Ami Paris", "focus": "Quartieri moda/creativi", "contatto": "Leasing Manager"}
    ],
    "Mass Market": [
        {"nome": "Uniqlo", "focus": "Grandi superfici >1000mq", "contatto": "Property Manager"},
        {"nome": "Mango", "focus": "High Street ad alto traffico", "contatto": "Expansion Dept"},
        {"nome": "Zara Home", "focus": "Retail parks o centri prime", "contatto": "Inditex Group Real Estate"}
    ],
    "Food": [
        {"nome": "Starbucks", "focus": "Angoli visibili / Dehors", "contatto": "Licensing Manager"},
        {"nome": "Iginio Massari", "focus": "Luxury high street", "contatto": "Sviluppo Retail"},
        {"nome": "Nespresso", "focus": "Boutique di prestigio", "contatto": "Boutique Expansion"}
    ]
}

# --- GESTIONE STATO NAVIGAZIONE ---
if 'step' not in st.session_state: st.session_state.step = 1
if 'data' not in st.session_state: st.session_state.data = {}

def avanti(): st.session_state.step += 1
def indietro(): st.session_state.step -= 1
def reset(): st.session_state.step = 1

# --- INTERFACCIA ---
st.title("🍷 CORE Intelligence")
st.write(f"Valutazione Asset | **Passaggio {st.session_state.step} di 3**")
st.progress(st.session_state.step / 3)

# --- STEP 1: DATI TECNICI (TUTTO PULITO) ---
if st.session_state.step == 1:
    st.subheader("📍 Fase 1: Identificazione Asset")
    st.markdown('<div class="step-box">', unsafe_allow_html=True)
    
    # Campi puliti (senza valori pre-inseriti)
    st.session_state.data['via'] = st.text_input("Indirizzo Immobile", placeholder="Es: Via Montenapoleone 1, Milano")
    st.session_state.data['target'] = st.selectbox("Seleziona Cluster Target", list(BRAND_DB.keys()))
    
    col_a, col_b = st.columns(2)
    st.session_state.data['mq_pt'] = col_a.number_input("Mq Piano Terra (PT)", min_value=0, value=0)
    st.session_state.data['mq_mag'] = col_b.number_input("Mq Magazzino", min_value=0, value=0)
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.button("Procedi ai Dati Economici ➡️", on_click=avanti)

# --- STEP 2: DATI ECONOMICI ---
elif st.session_state.step == 2:
    st.subheader("💰 Fase 2: Analisi Finanziaria")
    st.markdown('<div class="step-box">', unsafe_allow_html=True)
    
    st.session_state.data['canone'] = st.number_input("Canone Annuo richiesto (€)", min_value=0, value=0)
    st.session_state.data['key_money'] = st.number_input("Key Money / Buonuscita (€)", min_value=0, value=0)
    
    st.warning("L'algoritmo Bordeaux calcolerà il valore basato sulla superficie omogeneizzata (PT + 30% Magazzino).")
    st.markdown('</div>', unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    c1.button("⬅️ Torna indietro", on_click=indietro)
    c2.button("Genera Report Finale 🚀", on_click=avanti)

# --- STEP 3: REPORT FINALE E MATCHMAKING ---
elif st.session_state.step == 3:
    st.subheader("🎯 Fase 3: Analisi & Matchmaking Brand")
    
    # Calcoli tecnici
    d = st.session_state.data
    mq_comm = d['mq_pt'] + (d['mq_mag'] * 0.3)
    valore_mq = d['canone'] / mq_comm if mq_comm > 0 else 0
    
    # Visualizzazione Risultati Tecnici
    st.markdown('<div class="step-box">', unsafe_allow_html=True)
    r1, r2 = st.columns(2)
    with r1:
        st.markdown(f'<div class="metric-title">Superficie Comm.le</div><div class="metric-value">{mq_comm:.1f} mq</div>', unsafe_allow_html=True)
    with r2:
        st.markdown(f'<div class="metric-title">Valore Canone/Mq</div><div class="metric-value">€ {valore_mq:,.0f}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.divider()
    
    # Sezione Intelligence Brand
    st.markdown("### 🔍 Brand in Scouting (Match suggeriti)")
    st.write(f"In base alla superficie di **{mq_comm:.1f} mq** e al cluster **{d['target']}**, ecco i contatti prioritari:")

    matches = BRAND_DB.get(d['target'], [])
    for b in matches:
        st.markdown(f"""
        <div class="brand-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <b style="font-size: 1.3em; color: #800020;">{b['nome']}</b>
                <span style="background: #800020; color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.8em; font-weight: bold;">MATCH PRIORITARIO</span>
            </div>
            <p style="margin-top: 10px; margin-bottom: 5px;">📍 <b>Requisito:</b> {b['focus']}</p>
            <p style="margin: 0; color: #444;">👤 <b>Referente Scouting:</b> {b['contatto']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()
    if st.button("🔄 Nuova Valutazione"):
        reset()
        st.rerun()
