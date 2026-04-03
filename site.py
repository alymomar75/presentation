import streamlit as st
import urllib.parse

# 1. CONFIGURATION
st.set_page_config(page_title="Aly Momar Diallo | Portfolio Digital", layout="wide", page_icon="📲")

# 2. LIENS ET URLS
whatsapp_url = f"https://wa.me/221776938761?text={urllib.parse.quote('Bonjour Aly, j\'ai vu votre portfolio !')}"

# Dictionnaire de tes créations
realisations = [
    {"nom": "KFC Sénégal", "url": "https://kfctest.streamlit.app//", "img": "https://images.unsplash.com/photo-1513639776629-7b61b0ac49cb?q=80&w=400"},
    {"nom": "La Brioche Dorée", "url": "https://menuqrcode.streamlit.app//", "img": "https://images.unsplash.com/photo-1509440159596-0249088772ff?q=80&w=400"}
]

# --- 3. STYLE CSS (LUXE & DYNAMIQUE) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap');

    #MainMenu, footer, header, .stDeployButton { display:none !important; }
    [data-testid="stToolbar"] { visibility: hidden !important; }

    .stApp {
        background: linear-gradient(135deg, #73A3BF 0%, #FCE1BB 100%);
        background-attachment: fixed;
        font-family: 'Poppins', sans-serif;
        transition: background 0.8s ease;
        color: #1e293b;
    }

    /* Cartes Glassmorphism */
    .lux-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(12px);
        padding: 30px;
        border-radius: 30px;
        border: 1px solid rgba(255, 255, 255, 0.4);
        text-align: center;
        margin-bottom: 20px;
    }

    /* Cartes Portfolio */
    .port-card {
        background: white;
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        transition: 0.4s;
        text-decoration: none;
        display: block;
        color: #1e293b;
        margin-bottom: 20px;
    }
    .port-card:hover { transform: translateY(-10px); box-shadow: 0 20px 40px rgba(0,0,0,0.2); }
    .port-img { width: 100%; height: 150px; object-fit: cover; }
    .port-info { padding: 15px; font-weight: 600; text-align: center; }

    .btn-wa {
        background: #25D366;
        color: white !important;
        padding: 18px 35px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 700;
        display: inline-block;
        box-shadow: 0 10px 25px rgba(37, 211, 102, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

# --- 4. JS MOUVEMENT ---
st.components.v1.html("""
    <script>
    const app = window.parent.document.querySelector('.stApp');
    window.parent.addEventListener('mousemove', (e) => {
        let x = e.clientX / window.parent.innerWidth;
        app.style.background = `linear-gradient(${x * 360}deg, #73A3BF 0%, #FCE1BB 100%)`;
    });
    window.parent.addEventListener('deviceorientation', (e) => {
        app.style.background = `linear-gradient(${135 + e.gamma}deg, #73A3BF 0%, #FCE1BB 100%)`;
    });
    </script>
""", height=0)

# --- 5. CONTENU ---

# Hero Section
c1, c2 = st.columns([6, 4])
with c1:
    st.write("<br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 3rem;'>L'Expert du Menu Digital à Dakar 🇸🇳</h1>", unsafe_allow_html=True)
    st.write("Déjà adopté par les plus grands. Découvrez mes réalisations et passez au QR Code de luxe.")
    st.markdown(f'<br><a href="{whatsapp_url}" class="btn-wa">DISCUTER DE MON PROJET</a>', unsafe_allow_html=True)
with c2:
    st.image("https://images.unsplash.com/photo-1595079676339-1534801ad6cf?w=600", use_container_width=True)

st.write("---")

# --- SECTION PORTFOLIO ---
st.markdown("<h2 style='text-align: center;'>Nos Réalisations ✨</h2>", unsafe_allow_html=True)
st.write("<p style='text-align: center;'>Cliquez pour visualiser les menus en direct</p>", unsafe_allow_html=True)

pc1, pc2, pc3 = st.columns(3)
for i, site in enumerate(realisations):
    with (pc1 if i==0 else pc2 if i==1 else pc3):
        st.markdown(f"""
            <a href="{site['url']}" target="_blank" class="port-card">
                <img src="{site['img']}" class="port-img">
                <div class="port-info">{site['nom']} <br> <span style="font-size:0.7rem; color:#73A3BF;">Voir le site →</span></div>
            </a>
        """, unsafe_allow_html=True)

st.write("<br><br>", unsafe_allow_html=True)

# --- SECTION TARIFS ---
st.markdown("<h2 style='text-align: center;'>Nos Offres 💳</h2>", unsafe_allow_html=True)
p1, p2, p3, p4 = st.columns(4)

tarifs = [
    {"n": "Pack FLASH", "p": "3 500 F", "d": "Le QR Code simple", "c": "#73A3BF"},
    {"n": "Pack STARTER", "p": "15 000 F", "d": "Menu (Max 15 art.)", "c": "#5a8ba8"},
    {"n": "Pack BUSINESS", "p": "35 000 F", "d": "Commande WhatsApp", "c": "#4a768e"},
    {"n": "Pack PREMIUM", "p": "Sur Devis", "d": "Sur-mesure Complet", "c": "#b08d57"}
]

for i, t in enumerate(tarifs):
    with (p1 if i==0 else p2 if i==1 else p3 if i==2 else p4):
        st.markdown(f"""
        <div class="lux-card">
            <span style="background:{t['c']}; color:white; padding:5px 15px; border-radius:20px; font-size:0.7rem; font-weight:bold;">{t['n']}</span>
            <h2 style="margin:15px 0;">{t['p']}</h2>
            <p style="font-size:0.8rem; color:#64748b;">{t['d']}</p>
        </div>
        """, unsafe_allow_html=True)

# --- FOOTER ---
st.write("<br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #777; font-size: 0.75rem;'>© 2026 | ALY MOMAR DIALLO | DAKAR, SÉNÉGAL 🇸🇳</p>", unsafe_allow_html=True)
