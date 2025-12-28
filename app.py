import streamlit as st
import pandas as pd

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="CORE Intelligence", page_icon="🍷", layout="centered")

# --- CSS PROFESSIONALE (Tutte le personalizzazioni incluse) ---
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    h1, h2, h3 { color: #800020 !important; font-weight: bold; }
    
    /* Etichette nere e marcate per visibilità sotto il sole */
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

    .price-tag {
        padding: 12px;
        border-radius: 10px;
        font-weight: bold;
        text-align: center;
        margin: 15px 0;
        font-size: 1.2em;
    }

    .feature-tag {
        background-color: #e9ecef;
        padding: 6px 15px;
        border-radius: 20px;
        font-size: 0.9em;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- DATABASE INTELLIGENCE (Cluster, Brand e Prezzi Medi) ---
BRAND_DB = {
    "Lusso": {"brands": ["Hermès", "Cartier", "Loro Piana"], "avg_rent": 8000, "contacts": "Expansion Manager EMEA"},
    "Fashion Premium": {"brands": ["Stone Island", "Golden Goose", "Ami Paris"], "avg_rent": 3500, "contacts": "Retail Director Italy"},
    "Mass Market": {"brands": ["Uniqlo", "Mango", "Zara Home"], "avg_rent": 1500, "contacts": "Property Manager"},
    "Food": {"brands": ["Starbucks", "Iginio Massari", "Nespresso"], "avg_rent": 2200, "contacts": "Sviluppo Retail / Licensing"}
}

# --- GESTIONE STATO ---
if 'step' not in st.session_state: st.session_state.step = 1
if 'data' not in st.session_state: st.session_state.data = {}

def avanti(): st.session_state.step += 1
def indietro(): st.session_state.step -= 1
def reset(): st.session_state.step = 1

# --- HEADER ---
st.title("🍷 CORE Intelligence")
st.write(f"**Step {st.session_state.step} di 3**")
st.progress(st.session_state.step / 3)

# --- STEP 1: IDENTIFICAZIONE SPAZI & CARATTERISTICHE ---
if st.session_state.step == 1:
    st.subheader("📍 Fase 1: Identificazione e Superfici")
    st.markdown('<div class="step-box">', unsafe_allow_html=True)
    
    st.session_state.data['via'] = st.text_input("Indirizzo Immobile", placeholder="Es: Via Montenapoleone 1, Milano")
    st.session_state.data['target'] = st.selectbox("Cluster Target", list(BRAND_DB.keys()))
    
    # Nuova Caratteristica Canna Fumaria
    st.session_state.data['canna_fumaria'] = st.radio("Canna Fumaria presente?", ["Sì", "No"], horizontal=True)
    
    st.divider()
    
    # Tutte le Caselle Superfici con Placeholder
    col1, col2 = st.columns(2)
    st.session_state.data['mq_pt'] = col1.number_input("Mq Piano Terra (100%)", min_value=0, value=None, placeholder="Inserisci mq PT...")
    st.session_state.data['mq_p1'] = col2.number_input("Mq Piano 1 (50%)", min_value=0, value=None, placeholder="Inserisci mq P1...")
    
    col3, col4 = st.columns(2)
    st.session_state.data['mq_semi'] = col3.number_input("Mq Seminterrato (33%)", min_value=0, value=None, placeholder="Inserisci mq Seminterrato...")
    st.session_state.data['mq_mag'] = col4.number_input("Mq Magazzino (30%)", min_value=0, value=None, placeholder="Inserisci mq Magazzino...")
    
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("Procedi ai Dati Economici ➡️"):
        if st.session_state.data['mq_pt'] is not None:
            avanti()
            st.rerun()
        else:
            st.error("Inserisci almeno la metratura del Piano Terra per procedere.")

# --- STEP 2: ANALISI FINANZIARIA ---
elif st.session_state.step == 2:
    st.subheader("💰 Fase 2: Canone e Buonuscita")
    st.markdown('<div class="step-box">', unsafe_allow_html=True)
    
    st.session_state.data['canone'] = st.number_input("Canone Annuo richiesto (€)", min_value=0, value=None, placeholder="Inserisci Canone (Es: 250000)")
    st.session_state.data['key_money'] = st.number_input("Key Money / Buonuscita (€)", min_value=0, value=None, placeholder="Inserisci Buonuscita (Es: 100000)")
    
    st.info("💡 L'analisi calcolerà automaticamente la sostenibilità rispetto ai negozi circostanti.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    c1.button("⬅️ Indietro", on_click=indietro)
    if c2.button("Genera Report Intelligence 🚀"):
        if st.session_state.data['canone'] is not None:
            avanti()
            st.rerun()
        else:
            st.error("Inserisci il canone annuo per completare l'analisi.")

# --- STEP 3: REPORT FINALE E VALUTAZIONE IMMOBILE ---
elif st.session_state.step == 3:
    st.subheader("🎯 Fase 3: Analisi Risultati & Matchmaking")
    d = st.session_state.data
    
    # Calcolo Superficie Commerciale Pesata
    pt = d['mq_pt'] if d['mq_pt'] else 0
    p1 = (d['mq_p1'] * 0.5) if d['mq_p1'] else 0
    semi = (d['mq_semi'] * 0.33) if d['mq_semi'] else 0
    mag = (d['mq_mag'] * 0.3) if d['mq_mag'] else 0
    mq_totali = pt + p1 + semi + mag
    
    canone = d['canone'] if d['canone'] else 0
    valore_mq = canone / mq_totali if mq_totali > 0 else 0
    
    # LOGICA DI VALUTAZIONE (Confronto con i vicini)
    ref_price = BRAND_DB[d['target']]['avg_rent']
    percent_diff = ((valore_mq - ref_price) / ref_price) * 100
    
    if percent_diff > 15:
        valutazione, colore, desc = "CARO", "#d32f2f", "L'asset è sopra i valori medi dei negozi circostanti."
    elif percent_diff < -15:
        valutazione, colore, desc = "CHEAP", "#2e7d32", "L'asset è molto competitivo rispetto alla zona."
    else:
        valutazione, colore, desc = "IN LINEA", "#ef6c00", "L'asset rispecchia perfettamente i valori di mercato."

    # Box Riepilogo
    st.markdown('<div class="step-box">', unsafe_allow_html=True)
    st.write(f"📍 **{d['via']}**")
    
    cf_tag = "Canna Fumaria: SÌ" if d['canna_fumaria'] == "Sì" else "Canna Fumaria: NO"
    st.markdown(f'<div class="feature-tag">{cf_tag}</div>', unsafe_allow_html=True)
    
    r1, r2 = st.columns(2)
    r1.metric("Mq Commerciali Totali", f"{mq_totali:.1f} mq")
    r2.metric("Canone al Mq", f"€ {valore_mq:,.0f}")
    
    # Valutazione Generale
    st.markdown(f'<div class="price-tag" style="background-color:{colore}; color:white;">VALUTAZIONE: {valutazione}</div>', unsafe_allow_html=True)
    st.write(f"_{desc}_")
    st.markdown('</div>', unsafe_allow_html=True)

    # Sezione Brand
    st.markdown("### 🔍 Brand Intelligence Match")
    st.write(f"Brand con strategia attiva per cluster **{d['target']}**:")
    
    if d['target'] == "Food" and d['canna_fumaria'] == "No":
        st.warning("⚠️ Attenzione: L'assenza di canna fumaria limita i brand Food.")

    for brand in BRAND_DB[d['target']]['brands']:
        st.markdown(f"""
        <div class="brand-card">
            <b style="font-size: 1.2em; color: #800020;">{brand}</b><br>
            <small>👤 Referente: {BRAND_DB[d['target']]['contacts']}</small>
        </div>
        """, unsafe_allow_html=True)

    if st.button("🔄 Nuova Valutazione"):
        reset()
        st.rerun()
