import streamlit as st
import urllib.parse

# 1. Configuration de la page
st.set_page_config(page_title="Aly Digital Pro", layout="wide", page_icon="📲")

# 2. Variable WhatsApp
whatsapp_url = f"https://wa.me/221776938761?text={urllib.parse.quote('Bonjour Aly, je souhaite une démo.')}"

# --- 3. STYLE CSS GLOBAL (PC + MOBILE + WATCH) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');

    /* Masquage technique */
    #MainMenu, footer, header, .stDeployButton {{ display:none !important; }}
    [data-testid="stToolbar"] {{ visibility: hidden !important; }}

    /* FOND FLUIDE PC & MOBILE */
    .stApp {{
        background: linear-gradient(135deg, #73A3BF 0%, #FCE1BB 100%);
        background-attachment: fixed;
        font-family: 'Poppins', -apple-system, sans-serif;
        transition: background 0.6s ease;
    }}

    /* DESIGN DES CARTES (LOOK CANVA LUXE) */
    .main-card {{
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        border-radius: 30px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.4);
        text-align: center;
        margin-bottom: 20px;
        color: #1e293b;
    }}

    .hero-img {{
        border-radius: 30px;
        width: 100%;
        max-height: 350px;
        object-fit: cover;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
    }}

    /* BOUTON ADAPTÉ APPLE WATCH */
    .btn-action {{
        background: #25D366;
        color: white !important;
        padding: 20px;
        border-radius: 20px;
        display: block;
        text-decoration: none;
        font-weight: bold;
        font-size: 1.1rem;
        text-align: center;
        box-shadow: 0 10px 20px rgba(37, 211, 102, 0.2);
    }}

    /* --- OPTIMISATION SPÉCIFIQUE APPLE WATCH --- */
    @media (max-width: 300px) {{
        .stApp {{ background: #73A3BF !important; }} /* Couleur fixe pour la Watch */
        .hero-img {{ display: none !important; }}
        .main-card {{ padding: 15px; border-radius: 15px; background: white; }}
        h1 {{ font-size: 1.2rem !important; }}
        .btn-action {{ padding: 15px; font-size: 0.9rem; }}
    }}
    </style>
""", unsafe_allow_html=True)

# --- 4. SCRIPT HYBRIDE (PC/MOBILE) ---
# Ce script ne s'exécute pas sur Watch pour éviter le chargement infini
st.components.v1.html("""
    <script>
    const app = window.parent.document.querySelector('.stApp');
    if (window.innerWidth > 310) {
        // Mouvement Souris (PC)
        window.parent.addEventListener('mousemove', (e) => {
            let x = e.clientX / window.parent.innerWidth;
            app.style.background = `linear-gradient(${x * 360}deg, #73A3BF 0%, #FCE1BB 100%)`;
        });
        // Mouvement Gyro (Mobile)
        window.parent.addEventListener('deviceorientation', (e) => {
            app.style.background = `linear-gradient(${135 + e.gamma}deg, #73A3BF 0%, #FCE1BB 100%)`;
        });
    }
    </script>
""", height=0)

# --- 5. CONTENU DE LA PAGE ---
col1, col2 = st.columns([5, 5])

with col1:
    st.markdown("<h1 style='color:#1e293b;'>Digital Pro 🌊</h1>", unsafe_allow_html=True)
    st.markdown("### Par Aly Momar Diallo")
    st.write("Modernisez votre commerce à Dakar avec nos solutions de menus QR Code hygiéniques et élégantes.")
    st.markdown(f'<a href="{whatsapp_url}" class="btn-action">CONTACT WHATSAPP</a>', unsafe_allow_html=True)

with col2:
    # L'image ne s'affichera pas sur Watch grâce au CSS
    st.markdown('<img src="https://images.unsplash.com/photo-1595079676339-1534801ad6cf?w=600" class="hero-img">', unsafe_allow_html=True)

st.write("<br>", unsafe_allow_html=True)

# SECTION PRIX
st.markdown("<h2 style='text-align:center;'>Nos Tarifs</h2>", unsafe_allow_html=True)
p1, p2, p3 = st.columns(3)

for col, name, price, desc in zip([p1, p2, p3], 
                                  ["Pack FLASH", "Pack STARTER", "Pack BUSINESS"], 
                                  ["3 500 F", "15 000 F", "35 000 F"],
                                  ["Le QR Code simple", "Menu Digital Pro", "Commande WhatsApp"]):
    with col:
        st.markdown(f"""
        <div class="main-card">
            <h3 style="color:#73A3BF;">{name}</h3>
            <h2 style="margin:10px 0;">{price}</h2>
            <p style="font-size:0.8rem; color:#64748b;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

# FOOTER
st.markdown("<p style='text-align:center; font-size:0.7rem; margin-top:50px;'>© 2026 | ALY MOMAR DIALLO | DAKAR</p>", unsafe_allow_html=True)
