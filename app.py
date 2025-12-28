import streamlit as st
import pandas as pd

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="CORE Intelligence", page_icon="🍷", layout="centered")

# --- CSS PROFESSIONALE ---
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    h1, h2, h3 { color: #800020 !important; font-weight: bold; }
    
    /* Etichette nere e ben visibili */
    .stWidget label {
        color: #000000 !important;
        font-weight: 800 !important;
        font-size: 1.1rem !important;
    }

    /* Bottoni Bordeaux */
    .stButton>button { 
        background-color: #800020 !important; 
        color: white !important; 
        border-radius: 25px; 
        font-weight: bold; 
        border: none; 
        height: 3.5em;
        width: 100%;
    }

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
    }
    </style>
""", unsafe_allow_html=True)

# --- DATABASE BRAND ---
BRAND_DB = {
    "Lusso": [
        {"nome": "Hermès", "focus": "Flagship High Street", "contatto": "Expansion Manager EMEA"},
        {"nome": "Cartier", "focus": "Boutique di prestigio", "contatto": "Retail Director Italy"},
        {"nome": "Loro Piana", "focus": "Location storiche", "contatto": "Head of Real Estate"}
    ],
    "Fashion Premium": [
        {"nome": "Stone Island", "focus": "Concept store", "contatto": "Global Retail Manager"},
        {"nome": "Golden Goose", "focus": "High visibility", "contatto": "Acquisition Specialist"},
        {"nome": "Ami Paris", "focus": "Quartieri moda", "contatto": "Leasing Manager"}
    ],
    "Mass Market": [
        {"nome": "Uniqlo", "focus": "Superfici >1000mq", "contatto": "Property Manager"},
        {"nome": "Mango", "focus": "High Street", "contatto": "Expansion Dept"},
        {"nome": "Zara Home", "focus": "Centri prime", "contatto": "Inditex Group"}
    ],
    "Food": [
        {"nome": "Starbucks", "focus": "Angoli visibili", "contatto": "Licensing Manager"},
        {"nome": "Iginio Massari", "focus": "Luxury Food", "contatto": "Sviluppo Retail"},
        {"nome": "Nespresso", "focus": "Boutique prestigio", "contatto": "Boutique Expansion"}
    ]
}

if 'step' not in st.session_state: st.session_state.step = 1
if 'data' not in st.session_state: st.session_state.data = {}

def avanti(): st.session_state.step += 1
def indietro(): st.session_state.step -= 1
def reset(): st.session_state.step = 1

st.title("🍷 CORE Intelligence")
st.write(f"**Passaggio {st.session_state.step} di 3**")
st.progress(st.session_state.step / 3)

# --- STEP 1: DATI TECNICI ---
if st.session_state.step == 1:
    st.subheader("📍 Fase 1: Identificazione Spazi")
    st.markdown('<div class="step-box">', unsafe_allow_html=True)
    
    # Suggerimento Indirizzo
    st.session_state.data['via'] = st.text_input("Indirizzo Immobile", placeholder="Es: Via Montenapoleone 1, Milano")
    
    st.session_state.data['target'] = st.selectbox("Seleziona Cluster Target", list(BRAND_DB.keys()))
    
    col_a, col_b = st.columns(2)
    # Suggerimento Metri Quadri PT
    st.session_state.data['mq_pt'] = col_a.number_input("Mq Piano Terra (PT)", min_value=0, value=None, placeholder="Inserisci mq Piano Terra...")
    
    # Suggerimento Metri Quadri Magazzino
    st.session_state.data['mq_mag'] = col_b.number_input("Mq Magazzino", min_value=0, value=None, placeholder="Inserisci mq Magazzino...")
    
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("Procedi ai Dati Economici ➡️"):
        if st.session_state.data['mq_pt'] is not None:
            avanti()
            st.rerun()
        else:
            st.error("Inserisci la metratura del Piano Terra per continuare.")

# --- STEP 2: DATI ECONOMICI ---
elif st.session_state.step == 2:
    st.subheader("💰 Fase 2: Analisi Finanziaria")
    st.markdown('<div class="step-box">', unsafe_allow_html=True)
    
    # Suggerimento Canone
    st.session_state.data['canone'] = st.number_input("Canone Annuo richiesto (€)", min_value=0, value=None, placeholder="Inserisci Canone Annuo (es: 250000)")
    
    # Suggerimento Buonuscita
    st.session_state.data['key_money'] = st.number_input("Key Money / Buonuscita (€)", min_value=0, value=None, placeholder="Inserisci Buonuscita (es: 100000)")
    
    st.info("💡 L'algoritmo calcolerà il valore al mq pesando il magazzino al 30%.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    c1.button("⬅️ Indietro", on_click=indietro)
    if c2.button("Genera Report Finale 🚀"):
        if st.session_state.data['canone'] is not None:
            avanti()
            st.rerun()
        else:
            st.error("Inserisci il canone annuo per generare l'analisi.")

# --- STEP 3: REPORT E MATCHMAKING ---
elif st.session_state.step == 3:
    st.subheader("🎯 Fase 3: Analisi & Matchmaking")
    
    d = st.session_state.data
    mq_pt = d['mq_pt'] if d['mq_pt'] else 0
    mq_mag = d['mq_mag'] if d['mq_mag'] else 0
    canone = d['canone'] if d['canone'] else 0
    
    mq_comm = mq_pt + (mq_mag * 0.3)
    valore_mq = canone / mq_comm if mq_comm > 0 else 0
    
    st.markdown('<div class="step-box">', unsafe_allow_html=True)
    r1, r2 = st.columns(2)
    r1.metric("Superficie Commerciale", f"{mq_comm:.1f} mq")
    r2.metric("Canone al Mq (Pesato)", f"€ {valore_mq:,.0f}")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### 🔍 Brand Matchmaking")
    st.write(f"Asset ideale per i seguenti brand del settore **{d['target']}**:")
    
    matches = BRAND_DB.get(d['target'], [])
    for b in matches:
        st.markdown(f"""
        <div class="brand-card">
            <b style="font-size: 1.2em; color: #800020;">{b['nome']}</b><br>
            <p style="margin: 5px 0;">📍 <b>Strategia:</b> {b['focus']}</p>
            <p style="margin: 0; color: #555;">👤 <b>Referente:</b> {b['contatto']}</p>
        </div>
        """, unsafe_allow_html=True)

    if st.button("🔄 Nuova Analisi"):
        reset()
        st.rerun()
