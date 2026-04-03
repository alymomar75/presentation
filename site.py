import streamlit as st
import urllib.parse

# 1. Configuration ultra-légère
st.set_page_config(page_title="Aly Digital", layout="wide")

# 2. CSS Adaptatif (Spécial WatchOS)
st.markdown("""
    <style>
    /* Masquage complet pour gagner de la RAM sur la montre */
    #MainMenu, footer, header, .stDeployButton {display:none !important;}
    
    .stApp {
        background: #73A3BF; /* Couleur fixe par défaut pour la montre */
        font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Cartes simplifiées pour Watch */
    .card {
        background: white;
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 10px;
        color: #1e293b;
        text-align: center;
    }

    /* Bouton WhatsApp géant pour le tactile Watch */
    .btn {
        background: #25D366;
        color: white !important;
        padding: 15px;
        border-radius: 10px;
        display: block;
        text-align: center;
        text-decoration: none;
        font-weight: bold;
    }

    /* SI ÉCRAN LARGE (PC/MOBILE) -> ACTIVER LE FLUIDE */
    @media (min-width: 321px) {
        .stApp {
            background: linear-gradient(135deg, #73A3BF 0%, #FCE1BB 100%);
            transition: background 0.5s ease;
        }
    }
    </style>
""", unsafe_allow_html=True)

# 3. Script de mouvement (Désactivé si l'écran est trop petit pour éviter le bug de charge)
st.components.v1.html("""
    <script>
    if (window.innerWidth > 320) {
        const app = window.parent.document.querySelector('.stApp');
        window.parent.addEventListener('mousemove', (e) => {
            let x = e.clientX / window.parent.innerWidth;
            let angle = x * 180;
            app.style.background = `linear-gradient(${angle}deg, #73A3BF 0%, #FCE1BB 100%)`;
        });
        window.parent.addEventListener('deviceorientation', (e) => {
            let angle = 135 + (e.gamma);
            app.style.background = `linear-gradient(${angle}deg, #73A3BF 0%, #FCE1BB 100%)`;
        });
    }
    </script>
""", height=0)

# 4. CONTENU (Priorité à la lecture rapide)
st.markdown("<h2 style='color:white; text-align:center;'>Aly Digital 🇸🇳</h2>", unsafe_allow_html=True)

# On affiche l'image seulement sur les grands écrans
if st.sidebar.checkbox('Afficher Image', value=True): # Astuce pour cacher sur petit écran
    st.image("https://images.unsplash.com/photo-1595079676339-1534801ad6cf?w=400", use_container_width=True)

st.markdown("<p style='color:white; text-align:center; font-size:0.8rem;'>Menus QR Code & Digitalisation</p>", unsafe_allow_html=True)

# Liste des prix (Verticale pour Watch)
for name, price in [("FLASH", "3 500 F"), ("STARTER", "15 000 F"), ("BUSINESS", "35 000 F")]:
    st.markdown(f"""<div class="card"><b>{name}</b><br>{price}</div>""", unsafe_allow_html=True)

# Contact (Le plus important sur Watch)
whatsapp_url = f"https://wa.me/221776938761?text=" + urllib.parse.quote("Infos démo")
st.markdown(f'<a href="{whatsapp_url}" class="btn">WHATSAPP DIRECT</a>', unsafe_allow_html=True)
