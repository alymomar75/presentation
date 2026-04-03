import streamlit as st
import urllib.parse

# --- CONFIGURATION ---
st.set_page_config(page_title="Aly Momar Diallo | Digital Fluid Pro", layout="wide", page_icon="🌊")

# --- 1. STYLE CSS (DESIGN LUXE & CANVA) ---
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

    .port-card {
        background: white;
        border-radius: 25px;
        overflow: hidden;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        transition: 0.4s;
        text-decoration: none;
        display: block;
        color: #1e293b;
        margin-bottom: 20px;
    }
    .port-card:hover { transform: translateY(-10px); }
    .port-img { width: 100%; height: 180px; object-fit: cover; }
    .port-info { padding: 15px; font-weight: 600; text-align: center; }

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
        padding: 18px 30px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 800;
        display: block;
        text-align: center;
        box-shadow: 0 10px 20px rgba(37, 211, 102, 0.2);
    }

    /* Style du formulaire Streamlit */
    [data-testid="stForm"] {
        background: rgba(255, 255, 255, 0.8) !important;
        border-radius: 30px !important;
        padding: 30px !important;
        border: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. JAVASCRIPT HYBRIDE (SOURIS PC + GYRO MOBILE) ---
st.components.v1.html("""
    <script>
    const app = window.parent.document.querySelector('.stApp');
    
    // MODE PC (SOURIS)
    window.parent.addEventListener('mousemove', (e) => {
        let x = e.clientX / window.parent.innerWidth;
        let y = e.clientY / window.parent.innerHeight;
        let angle = (x + y) * 180;
        app.style.background = `linear-gradient(${angle}deg, #73A3BF 0%, #FCE1BB 100%)`;
    });

    // MODE MOBILE (GYROSCOPE)
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

# --- 3. HERO SECTION ---
col_1, col_2 = st.columns([5, 5])

with col_1:
    st.write("<br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 3.2rem; line-height: 1.1;'>Digitalisez avec Élégance 🌊</h1>", unsafe_allow_html=True)
    st.markdown("### Aly Momar Diallo | Expert Solutions QR")
    st.write("Le futur de votre commerce commence ici avec une interface fluide et moderne.")
    st.info("✨ **Interactif :** Bougez votre souris sur PC ou inclinez votre téléphone.")

with col_2:
    st.markdown("""<img src="https://images.unsplash.com/photo-1595079676339-1534801ad6cf?q=80&w=1000" class="hero-img">""", unsafe_allow_html=True)

st.divider()

# --- 4. NOS RÉALISATIONS (PORTFOLIO) ---
st.markdown("<h2 style='text-align: center; margin-bottom: 30px;'>Nos Réalisations ✨</h2>", unsafe_allow_html=True)
realisations = [
    {"nom": "KFC Sénégal", "url": "https://kfctest.streamlit.app/", "img": "https://images.unsplash.com/photo-1513639776629-7b61b0ac49cb?q=80&w=400"},
    {"nom": "La Brioche Dorée", "url": "https://menuqrcode.streamlit.app/", "img": "https://images.unsplash.com/photo-1509440159596-0249088772ff?q=80&w=400"}
]

p_col1, p_col2, p_col3 = st.columns([1, 2, 1])
with p_col2:
    sub_col1, sub_col2 = st.columns(2)
    for i, site in enumerate(realisations):
        with (sub_col1 if i==0 else sub_col2):
            st.markdown(f"""
                <a href="{site['url']}" target="_blank" class="port-card">
                    <img src="{site['img']}" class="port-img">
                    <div class="port-info">{site['nom']} <br> <span style="font-size:0.7rem; color:#73A3BF;">Voir le projet →</span></div>
                </a>
            """, unsafe_allow_html=True)

st.write("<br>")

# --- 5. FORMULAIRE DE DEVIS (REDIRECT WHATSAPP) ---
st.markdown("<h2 style='text-align: center;'>Demander mon devis 📝</h2>", unsafe_allow_html=True)
f_col1, f_col2, f_col3 = st.columns([1, 2, 1])

with f_col2:
    with st.form("devis_form"):
        etablissement = st.text_input("Nom de votre établissement", placeholder="Ex: Restaurant Le Terrou-Bi")
        choix_pack = st.selectbox("Pack souhaité", ["Pack FLASH (3 500 F)", "Pack STARTER (15 000 F)", "Pack BUSINESS (35 000 F)", "Pack PREMIUM (Sur Devis)"])
        precision = st.text_area("Précisions (Optionnel)", placeholder="Ex: Menu avec 20 photos...")
        
        btn_submit = st.form_submit_button("Préparer mon message WhatsApp")
        
        if btn_submit:
            if etablissement:
                message_wa = f"Bonjour Aly ! Je suis le responsable de {etablissement}. Je suis intéressé par le {choix_pack}. {precision}"
                url_wa = f"https://wa.me/221776938761?text={urllib.parse.quote(message_wa)}"
                st.markdown(f'<a href="{url_wa}" target="_blank" class="btn-whatsapp">🚀 ENVOYER SUR WHATSAPP</a>', unsafe_allow_html=True)
            else:
                st.warning("Veuillez entrer le nom de votre établissement.")

st.write("<br>")

# --- 6. NOS OFFRES (GRILLE DE PRIX) ---
st.markdown("<h2 style='text-align: center; margin-bottom: 30px;'>Nos Offres Digitales 💳</h2>", unsafe_allow_html=True)
o1, o2, o3, o4 = st.columns(4)

packs = [
    {"n": "Pack FLASH", "p": "3 500 F", "d": "Le QR Code simple", "c": "#73A3BF"},
    {"n": "Pack STARTER", "p": "15 000 F", "d": "Menu (Max 15 art.)", "c": "#5a8ba8"},
    {"n": "Pack BUSINESS", "p": "35 000 F", "d": "Commande WhatsApp", "c": "#4a768e"},
    {"n": "Pack PREMIUM", "p": "Sur Devis", "d": "Luxe & Sur-mesure", "c": "#b08d57"}
]

for i, p in enumerate(packs):
    with (o1 if i==0 else o2 if i==1 else o3 if i==2 else o4):
        st.markdown(f"""
        <div class="canva-card">
            <div style="background:{p['c']}; color:white; padding:5px 15px; border-radius:20px; font-size:0.7rem; font-weight:bold; display:inline-block; margin-bottom:15px;">{p['n']}</div>
            <h2 style="margin:0; color:#1e293b;">{p['p']}</h2>
            <p style="font-size:0.85rem; color:#636e72; margin-top:10px;">{p['d']}</p>
        </div>
        """, unsafe_allow_html=True)

# --- 7. FOOTER ---
st.write("<br><br>")
st.markdown("<p style='text-align: center; color: #777; font-size: 0.75rem;'>© 2026 | ALY MOMAR DIALLO | DAKAR, SÉNÉGAL 🇸🇳</p>", unsafe_allow_html=True)
