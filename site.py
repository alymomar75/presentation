import streamlit as st
import urllib.parse

# 1. Configuration de base (Pas de titre d'onglet pour gagner du temps)
st.set_page_config(layout="wide")

# 2. Variable de contact
whatsapp_url = f"https://wa.me/221776938761?text={urllib.parse.quote('Infos QR Code')}"

# --- 3. CSS ULTRA-SIMPLIFIÉ ---
st.markdown(f"""
    <style>
    /* Supprimer tout ce qui pèse */
    #MainMenu, footer, header, .stDeployButton {{ display:none !important; }}
    
    .stApp {{
        background: #73A3BF; /* Couleur unie pour la montre */
        font-family: -apple-system, system-ui, sans-serif;
    }}

    /* Cartes sans effets de flou (trop lourd pour la SE) */
    .watch-card {{
        background: white;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        color: #1a1a1a;
        text-align: center;
        border: 1px solid #ddd;
    }}

    .btn-qr {{
        background: #25D366;
        color: white !important;
        padding: 15px;
        border-radius: 10px;
        display: block;
        text-decoration: none;
        font-weight: bold;
        text-align: center;
    }}

    /* RÉTABLIR LE LOOK LUXE SUR PC/IPHONE SEULEMENT */
    @media (min-width: 350px) {{
        .stApp {{
            background: linear-gradient(135deg, #73A3BF 0%, #FCE1BB 100%) !important;
        }}
        .watch-card {{
            background: rgba(255, 255, 255, 0.8);
            backdrop-filter: blur(10px);
            border-radius: 25px;
        }}
    }}
    </style>
""", unsafe_allow_html=True)

# --- 4. LE CONTENU (ORDRE CRITIQUE) ---

# Titre Minimaliste
st.markdown("<h2 style='color:white; text-align:center;'>Aly Digital 🇸🇳</h2>", unsafe_allow_html=True)

# On affiche les prix DIRECTEMENT (Pas de colonnes complexes pour la montre)
st.markdown('<div class="watch-card"><b>Pack FLASH</b><br>3 500 F CFA</div>', unsafe_allow_html=True)
st.markdown('<div class="watch-card"><b>Pack STARTER</b><br>15 000 F CFA</div>', unsafe_allow_html=True)
st.markdown('<div class="watch-card"><b>Pack BUSINESS</b><br>35 000 F CFA</div>', unsafe_allow_html=True)

# Bouton d'action (Prioritaire sur Watch)
st.markdown(f'<a href="{whatsapp_url}" class="btn-qr">CONTACT WHATSAPP</a>', unsafe_allow_html=True)

# L'image ne charge QUE sur les grands écrans pour ne pas bloquer la montre
if st.sidebar.hidden: # Astuce technique
    pass
else:
    st.write("---")
    st.markdown('<p style='color:white; text-align:center; font-size:0.7rem;'>Expertise & Modernité</p>', unsafe_allow_html=True)

# --- 5. JS HYBRIDE (Désactivé sur Watch) ---
st.components.v1.html("""
    <script>
    if (window.innerWidth > 350) {
        const app = window.parent.document.querySelector('.stApp');
        window.parent.addEventListener('mousemove', (e) => {
            let x = e.clientX / window.parent.innerWidth;
            app.style.background = `linear-gradient(${x * 360}deg, #73A3BF 0%, #FCE1BB 100%)`;
        });
    }
    </script>
""", height=0)
