import streamlit as st
import urllib.parse

# Configuration
st.set_page_config(page_title="Aly Momar Diallo | Digital Fluid Pro", layout="wide", page_icon="🌊")

# --- 1. STYLE CSS (LISSAGE ET DESIGN CANVA) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');

    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stToolbar"] {visibility: hidden !important;}
    .stDeployButton {display:none;}

    .stApp {
        background: linear-gradient(135deg, #73A3BF 0%, #FCE1BB 100%);
        background-attachment: fixed;
        transition: background 0.8s cubic-bezier(0.1, 0.7, 1.0, 0.1);
        font-family: 'Poppins', sans-serif;
        color: #1e293b;
    }

    .canva-card {
        background: rgba(255, 255, 255, 0.75);
        backdrop-filter: blur(15px);
        padding: 30px;
        border-radius: 35px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.04);
        text-align: center;
        margin-bottom: 20px;
        border: 1px solid rgba(255, 255, 255, 0.5);
    }

    .hero-img {
        border-radius: 40px;
        box-shadow: 0 20px 50px rgba(115, 163, 191, 0.3);
        width: 100%;
        max-height: 380px;
        object-fit: cover;
    }

    .btn-whatsapp {
        background-color: #25D366;
        color: white !important;
        padding: 20px 35px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 800;
        display: block;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. JAVASCRIPT HYBRIDE (SOURIS PC + GYRO MOBILE) ---
st.components.v1.html("""
    <script>
    const app = window.parent.document.querySelector('.stApp');
    
    // --- MODE PC (SOURIS) ---
    window.parent.addEventListener('mousemove', (e) => {
        let x = e.clientX / window.parent.innerWidth;
        let y = e.clientY / window.parent.innerHeight;
        let angle = (x + y) * 180;
        app.style.background = `linear-gradient(${angle}deg, #73A3BF 0%, #FCE1BB 100%)`;
    });

    // --- MODE MOBILE (GYROSCOPE) ---
    function updateGyro(e) {
        let angle = 135 + (e.beta / 2) + (e.gamma / 2);
        app.style.background = `linear-gradient(${angle}deg, #73A3BF 0%, #FCE1BB 100%)`;
    }

    window.parent.addEventListener('deviceorientation', updateGyro);
    
    // Activation iOS
    window.parent.document.addEventListener('click', function() {
        if (typeof DeviceOrientationEvent.requestPermission === 'function') {
            DeviceOrientationEvent.requestPermission();
        }
    }, {once: true});
    </script>
""", height=0)

# --- 3. CONTENU ---
col_1, col_2 = st.columns([5, 5])

with col_1:
    st.write("<br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 3.2rem; line-height: 1.1;'>Digitalisez avec Élégance 🌊</h1>", unsafe_allow_html=True)
    st.markdown("### Aly Momar Diallo | Expert Solutions QR")
    st.write("Une interface fluide qui réagit à vos mouvements. Le futur de votre commerce commence ici.")
    st.info("✨ **Interactif :** Sur PC, bougez votre souris. Sur Mobile, inclinez l'appareil.")

with col_2:
    st.markdown("""<img src="https://images.unsplash.com/photo-1595079676339-1534801ad6cf?q=80&w=1000&auto=format&fit=crop" class="hero-img">""", unsafe_allow_html=True)

st.divider()

# --- 4. OFFRES ---
st.markdown("<h2 style='text-align: center; margin-bottom: 30px;'>Nos Offres Digitales 💳</h2>", unsafe_allow_html=True)
p1, p2, p3, p4 = st.columns(4)

packs = [
    {"n": "Pack FLASH", "p": "3 500 F", "d": "Le QR Code simple", "c": "#73A3BF"},
    {"n": "Pack STARTER", "p": "15 000 F", "d": "Menu (Max 15 art.)", "c": "#5a8ba8"},
    {"n": "Pack BUSINESS", "p": "35 000 F", "d": "Commande WhatsApp", "c": "#4a768e"},
    {"n": "Pack PREMIUM", "p": "Sur Devis", "d": "Luxe & Sur-mesure", "c": "#b08d57"}
]

for i, p in enumerate(packs):
    with (p1 if i==0 else p2 if i==1 else p3 if i==2 else p4):
        st.markdown(f"""
        <div class="canva-card">
            <div style="background:{p['c']}; color:white; padding:5px 15px; border-radius:20px; font-size:0.7rem; font-weight:bold; display:inline-block; margin-bottom:15px;">{p['n']}</div>
            <h2 style="margin:0; color:#1e293b;">{p['p']}</h2>
            <p style="font-size:0.85rem; color:#636e72; margin-top:10px;">{p['d']}</p>
        </div>
        """, unsafe_allow_html=True)

# --- 5. CONTACT ---
st.write("<br>", unsafe_allow_html=True)
c_left, c_right = st.columns(2)

with c_left:
    st.markdown("""
    <div style="background: white; padding: 40px; border-radius: 35px; border: 1px solid #f1f1f1;">
        <h3 style="margin-top:0; color:#73A3BF;">Parlons de votre projet 📧</h3>
        <form action="https://formsubmit.co/alymomardiallo75@gmail.com" method="POST">
            <input type="text" name="commerce" placeholder="Nom de l'établissement" required style="width:100%; padding:15px; margin-bottom:15px; border-radius:15px; border:1px solid #eee;">
            <input type="text" name="contact" placeholder="Numéro WhatsApp" required style="width:100%; padding:15px; margin-bottom:15px; border-radius:15px; border:1px solid #eee;">
            <button type="submit" style="width:100%; background: #73A3BF; color: white; border: none; padding: 188px; border-radius: 15px; font-weight: bold; cursor: pointer; padding:18px;">DÉMARRER</button>
        </form>
    </div>
    """, unsafe_allow_html=True)

with c_right:
    whatsapp_msg = urllib.parse.quote("Bonjour Aly ! Je souhaite une démonstration pour mon commerce.")
    whatsapp_url = f"https://wa.me/221776938761?text={whatsapp_msg}"
    st.markdown(f"""
        <div style="text-align: center; padding: 40px;">
            <p style="font-size:1.2rem; font-weight:600;">Une question urgente ?</p>
            <a href="{whatsapp_url}" class="btn-whatsapp" target="_blank">
                💬 WHATSAPP DIRECT
            </a>
            <p style="font-size:0.85rem; opacity:0.7; margin-top:15px;">Réponse rapide garantie.</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: #777; font-size: 0.75rem; margin-top:60px;'>© 2026 | ALY MOMAR DIALLO | DAKAR, SÉNÉGAL 🇸🇳</p>", unsafe_allow_html=True)
