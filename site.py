import streamlit as st
import urllib.parse

# Configuration de la page
st.set_page_config(page_title="Aly Momar Diallo | Excellence", layout="wide", page_icon="✨")

# --- STYLE CSS (LUXE & RESPONSIVE WATCH/MOBILE) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;600&display=swap');

    /* Masquage Streamlit */
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stToolbar"] {visibility: hidden !important;}

    /* Fond & Base */
    .stApp {
        background-color: #fcfcfc;
        font-family: 'Inter', sans-serif;
        color: #1a1a1a;
    }

    /* Typographie Adaptative */
    h1 {
        font-family: 'Playfair Display', serif !important;
        color: #1a1a1a !important;
        font-size: clamp(1.8rem, 5vw, 3.5rem) !important;
        text-align: center;
    }
    
    h2, h3 {
        font-family: 'Playfair Display', serif !important;
        color: #b08d57 !important;
        text-align: center;
    }

    /* Cartes de Luxe */
    .lux-card {
        background: white;
        padding: 20px;
        border: 1px solid #eeeeee;
        margin-bottom: 10px;
        text-align: center;
    }

    /* Bouton WhatsApp - TAILLE ADAPTÉE AU DOIGT (WATCH) */
    .btn-lux {
        background-color: #1a1a1a;
        color: #ffffff !important;
        padding: 20px 30px;
        text-decoration: none;
        font-weight: 600;
        display: block;
        width: 100%;
        text-align: center;
        letter-spacing: 1px;
        text-transform: uppercase;
        font-size: 0.9rem;
        margin-top: 10px;
    }

    /* --- OPTIMISATION APPLE WATCH & PETITS ÉCRANS --- */
    @media (max-width: 300px) {
        .hero-img { display: none; } /* On cache l'image sur la montre */
        h1 { font-size: 1.2rem !important; }
        .lux-card { padding: 10px; }
        .btn-lux { padding: 15px 10px; font-size: 0.7rem; }
        .contact-box { padding: 15px; }
    }

    .hero-img {
        width: 100%;
        border-bottom: 3px solid #b08d57;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- VUE UNIQUE (ORDRE ADAPTÉ POUR LE DÉFILEMENT WATCH) ---

# 1. Image (Cachée sur montre via CSS)
st.markdown("""<img src="https://images.unsplash.com/photo-1595079676339-1534801ad6cf?q=80&w=1000&auto=format&fit=crop" class="hero-img">""", unsafe_allow_html=True)

# 2. Titre & Intro
st.markdown("<h1>L'Excellence Digitale</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#b08d57; font-weight:bold;'>ALY MOMAR DIALLO</p>", unsafe_allow_html=True)

st.write("<p style='text-align:center; font-size:0.9rem;'>Solutions QR Code Premium pour établissements de prestige à Dakar.</p>", unsafe_allow_html=True)

st.divider()

# 3. Les Tarifs (Version défilante verticale pour montre)
st.markdown("<h2>Nos Tarifs</h2>", unsafe_allow_html=True)

packs = [
    {"n": "FLASH", "p": "3 500 F", "d": "QR Code Essentiel"},
    {"n": "STARTER", "p": "15 000 F", "d": "Catalogue Élégant"},
    {"n": "BUSINESS", "p": "35 000 F", "d": "Commande WhatsApp"},
    {"n": "PREMIUM", "p": "SUR DEVIS", "d": "Sur-Mesure Luxe"}
]

for p in packs:
    st.markdown(f"""
    <div class="lux-card">
        <span style="color:#b08d57; font-size:0.7rem; font-weight:bold;">{p['n']}</span>
        <div style="font-size:1.2rem; font-weight:bold;">{p['p']}</div>
        <div style="font-size:0.75rem; color:#888;">{p['d']}</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# 4. Contact Simplifié
st.markdown("<h2>Contact</h2>", unsafe_allow_html=True)

# Lien WhatsApp Direct (Prioritaire sur montre)
whatsapp_msg = urllib.parse.quote("Bonjour Aly, je souhaite une démo.")
whatsapp_url = f"https://wa.me/221776938761?text={whatsapp_msg}"

st.markdown(f"""
    <a href="{whatsapp_url}" class="btn-lux" target="_blank">
        WHATSAPP DIRECT
    </a>
""", unsafe_allow_html=True)

st.write("<br>", unsafe_allow_html=True)

# Formulaire (Plus bas pour les écrans larges)
with st.expander("M'envoyer un Email"):
    st.markdown(f"""
    <div style="background:#f9f9f9; padding:20px;">
        <form action="https://formsubmit.co/alymomardiallo75@gmail.com" method="POST">
            <input type="text" name="name" placeholder="NOM DU COMMERCE" required style="width:100%; border:none; border-bottom:1px solid #ccc; margin-bottom:15px; background:transparent;">
            <input type="text" name="contact" placeholder="TÉLÉPHONE" required style="width:100%; border:none; border-bottom:1px solid #ccc; margin-bottom:15px; background:transparent;">
            <button type="submit" style="width:100%; background:#1a1a1a; color:white; border:none; padding:15px; font-weight:bold;">ENVOYER</button>
        </form>
    </div>
    """, unsafe_allow_html=True)

# 5. Footer Minimal
st.markdown("<p style='text-align: center; color: #999; font-size: 0.6rem; letter-spacing: 1px; margin-top:30px;'>© 2026 ALY MOMAR DIALLO — DAKAR</p>", unsafe_allow_html=True)
