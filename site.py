import streamlit as st
import urllib.parse

# Configuration de la page
st.set_page_config(page_title="Aly Momar Diallo | Digital Concept", layout="wide", page_icon="✨")

# --- STYLE CSS (STYLE CANVA : JOYEUX & COLORÉ) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');

    /* Fond animé façon dégradé Canva */
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .stApp {
        background: linear-gradient(-45deg, #FF9A8B, #FF6B6B, #4158D0, #C850C0);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        font-family: 'Poppins', sans-serif;
    }

    /* Cartes blanches style "Papier" */
    .card {
        background: white;
        padding: 30px;
        border-radius: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        color: #2D3436;
        text-align: center;
        margin-bottom: 20px;
        transition: 0.3s;
    }
    
    .card:hover {
        transform: scale(1.03);
    }

    /* Titres colorés */
    h1 {
        color: white !important;
        font-size: 3.5rem !important;
        font-weight: 700 !important;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.2);
    }
    
    h2, h3 {
        color: #4834d4 !important;
        font-weight: 700;
    }

    /* Boutons personnalisés */
    .btn-whatsapp {
        background-color: #25D366;
        color: white !important;
        padding: 15px 30px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: bold;
        display: inline-block;
        box-shadow: 0 4px 15px rgba(37, 211, 102, 0.4);
    }

    /* Input style Canva */
    input, textarea {
        border-radius: 15px !important;
        border: 2px solid #f1f2f6 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.write("") # Espacement
st.markdown("<h1 style='text-align: center;'>✨ Digitalisez votre passion</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white; font-size: 1.5rem;'>Par Aly Momar Diallo</p>", unsafe_allow_html=True)

st.write("<br><br>", unsafe_allow_html=True)

# --- SECTION ARGUMENTS (ICÔNES COLORÉES) ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h1 style="font-size: 50px !important;">🧼</h1>
        <h3>100% Hygiénique</h3>
        <p>Plus de menus qui passent de main en main. Un scan, c'est propre et sécurisé pour vos clients.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h1 style="font-size: 50px !important;">🎨</h1>
        <h3>Design Moderne</h3>
        <p>Offrez une image "Premium" à votre commerce. Vos produits méritent une belle vitrine.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h1 style="font-size: 50px !important;">🚀</h1>
        <h3>Zéro Attente</h3>
        <p>Vos clients consultent les prix et dispos dès leur arrivée. Un service fluide et efficace.</p>
    </div>
    """, unsafe_allow_html=True)

# --- SECTION CONTACT ---
st.write("<br><br>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: white !important;'>Prêt pour le futur ? ⚡</h2>", unsafe_allow_html=True)

c_col1, c_col2 = st.columns([1, 1])

with c_col1:
    # Boîte contact blanche
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("M'envoyer un mail 📧")
    contact_form = f"""
    <form action="https://formsubmit.co/alymomardiallo75@gmail.com" method="POST">
        <input type="text" name="commerce" placeholder="Nom de votre boutique" required style="width:100%; padding:10px; margin-bottom:10px;">
        <input type="text" name="phone" placeholder="Votre numéro" required style="width:100%; padding:10px; margin-bottom:10px;">
        <textarea name="message" placeholder="Votre projet..." style="width:100%; padding:10px; margin-bottom:10px;"></textarea>
        <button type="submit" style="width:100%; background:#6c5ce7; color:white; border:none; padding:15px; border-radius:50px; font-weight:bold; cursor:pointer;">ENVOYER MAINTENANT</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with c_col2:
    st.markdown("<div class='card' style='height: 100%; display: flex; flex-direction: column; justify-content: center;'>", unsafe_allow_html=True)
    st.subheader("Direct WhatsApp 📲")
    st.write("Discutez en direct avec Aly pour une démo sur mesure.")
    
    whatsapp_msg = urllib.parse.quote("Bonjour Aly ! Je viens de voir votre site vitrine. J'aimerais digitaliser mon commerce.")
    whatsapp_url = f"https://wa.me/221776938761?text={whatsapp_msg}"
    
    st.markdown(f"""
        <a href="{whatsapp_url}" class="btn-whatsapp">
            ME CONTACTER SUR WHATSAPP
        </a>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>© 2026 | Aly Momar Diallo | Fait avec ❤️ pour le commerce local</p>", unsafe_allow_html=True)
