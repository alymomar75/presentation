import streamlit as st
import urllib.parse

# 1. CONFIGURATION MINIMALE (Vitesse de chargement prioritaire)
st.set_page_config(layout="centered")

# 2. LIEN WHATSAPP
msg = urllib.parse.quote("Bonjour Aly, je souhaite une démo.")
whatsapp_url = f"https://wa.me/221776938761?text={msg}"

# --- 3. CSS HYBRIDE (ADAPTATION WATCH AUTOMATIQUE) ---
st.markdown(f"""
    <style>
    /* Supprimer l'interface Streamlit pour libérer la RAM de la montre */
    #MainMenu, footer, header, .stDeployButton {{ display:none !important; }}
    [data-testid="stToolbar"] {{ visibility: hidden !important; }}
    
    .stApp {{
        background: #73A3BF; /* Couleur fixe pour chargement instantané */
        font-family: -apple-system, system-ui, sans-serif;
        color: white;
    }}

    /* Cartes Ultra-Légères */
    .card {{
        background: white;
        padding: 12px;
        border-radius: 12px;
        margin: 8px 0;
        color: #1a1a1a;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }}

    /* Bouton tactile pour petit écran */
    .btn {{
        background: #25D366;
        color: white !important;
        padding: 15px;
        border-radius: 12px;
        display: block;
        text-decoration: none;
        font-weight: 800;
        text-align: center;
        margin-top: 15px;
    }}

    /* REVENIR AU LOOK LUXE SI L'ÉCRAN EST ASSEZ GRAND (IPHONE/PC) */
    @media (min-width: 310px) {{
        .stApp {{
            background: linear-gradient(135deg, #73A3BF 0%, #FCE1BB 100%) !important;
        }}
        .card {{
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(10px);
            border-radius: 20px;
        }}
    }}
    </style>
""", unsafe_allow_html=True)

# --- 4. LE CONTENU (ZÉRO CALCUL) ---
st.markdown("<h2 style='text-align:center;'>Aly Digital 🇸🇳</h2>", unsafe_allow_html=True)

# Liste des Packs (Vertical pour la Watch)
st.markdown('<div class="card"><b>FLASH</b><br>3 500 F CFA</div>', unsafe_allow_html=True)
st.markdown('<div class="card"><b>STARTER</b><br>15 000 F CFA</div>', unsafe_allow_html=True)
st.markdown('<div class="card"><b>BUSINESS</b><br>35 000 F CFA</div>', unsafe_allow_html=True)

# Bouton d'action direct
st.markdown(f'<a href="{whatsapp_url}" class="btn">CONTACT WHATSAPP</a>', unsafe_allow_html=True)

st.write("---")

# Image optionnelle (Ne chargera que si la montre a la puissance pour)
st.markdown('<p style="text-align:center; font-size:0.7rem;">Digitalisation & Hygiène</p>', unsafe_allow_html=True)

# --- 5. JAVASCRIPT BRIDÉ (Désactivé sur Watch) ---
st.components.v1.html("""
    <script>
    if (window.innerWidth > 310) {
        const app = window.parent.document.querySelector('.stApp');
        window.parent.addEventListener('mousemove', (e) => {
            let x = e.clientX / window.parent.innerWidth;
            app.style.background = `linear-gradient(${x * 360}deg, #73A3BF 0%, #FCE1BB 100%)`;
        });
    }
    </script>
""", height=0)
