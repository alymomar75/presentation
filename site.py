import streamlit as st
import urllib.parse

# Configuration de la page
st.set_page_config(page_title="Aly Momar Diallo | Digital Pro", layout="wide", page_icon="📲")

# --- STYLE CSS (CANVA PRO : ÉLÉGANT & COLORÉ) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;600;800&display=swap');

    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Outfit', sans-serif;
        color: #ffffff;
    }

    /* Cartes Pro */
    .pro-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        border-radius: 25px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        text-align: center;
        transition: all 0.3s ease;
        height: 100%;
    }
    
    .pro-card:hover {
        background: rgba(255, 255, 255, 0.2);
        transform: translateY(-10px);
    }

    .icon-box {
        font-size: 3rem;
        margin-bottom: 15px;
    }

    h1, h2, h3 {
        font-weight: 800 !important;
        color: #ffffff !important;
    }

    /* Image Hero avec bords arrondis */
    .hero-img {
        border-radius: 30px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.3);
        width: 100%;
        max-height: 400px;
        object-fit: cover;
    }

    /* Bouton WhatsApp */
    .whatsapp-link {
        background: #25D366;
        color: white !important;
        padding: 18px 35px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 600;
        display: inline-block;
        transition: 0.3s;
        box-shadow: 0 10px 20px rgba(37, 211, 102, 0.3);
        margin-top: 10px;
    }
    .whatsapp-link:hover {
        transform: scale(1.05);
        box-shadow: 0 15px 30px rgba(37, 211, 102, 0.5);
    }

    /* Formulaire */
    .contact-box {
        background: white; 
        padding: 30px; 
        border-radius: 25px; 
        color: #2d3436;
    }
    input, textarea {
        background: #f1f2f6 !important;
        border-radius: 12px !important;
        border: 1px solid #dfe6e9 !important;
        color: #2d3436 !important;
        width: 100%;
        padding: 12px;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# --- SECTION HERO ---
col_hero_text, col_hero_img = st.columns([5, 5])

with col_hero_text:
    st.write("<br><br>", unsafe_allow_html=True)
    st.markdown("# Modernisez votre commerce en un Scan ⚡")
    st.markdown("### Aly Momar Diallo accompagne les entrepreneurs de Dakar dans leur transition digitale.")
    st.write("Dites adieu aux menus papier et offrez une expérience fluide, propre et rapide à vos clients.")

with col_hero_img:
    st.markdown("""
        <img src="https://images.unsplash.com/photo-1595079676339-1534801ad6cf?q=80&w=1000&auto=format&fit=crop" class="hero-img">
    """, unsafe_allow_html=True)

st.write("<br>", unsafe_allow_html=True)
st.divider()

# --- ARGUMENTS ---
st.markdown("<h2 style='text-align: center;'>Une solution pensée pour vous</h2>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""<div class="pro-card"><div class="icon-box">🛡️</div><h3>Hygiène Maximale</h3><p>Solution "Zero-Contact" idéale. Plus de manipulation de menus physiques.</p></div>""", unsafe_allow_html=True)
with c2:
    st.markdown("""<div class="pro-card"><div class="icon-box">💎</div><h3>Image de Marque</h3><p>Positionnez votre enseigne comme moderne et innovante.</p></div>""", unsafe_allow_html=True)
with c3:
    st.markdown("""<div class="pro-card"><div class="icon-box">📈</div><h3>Gestion Agile</h3><p>Mise à jour instantanée de vos tarifs et stocks en un clic.</p></div>""", unsafe_allow_html=True)

# --- CONTACT ---
st.write("<br><br>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Démarrons votre projet aujourd'hui</h2>", unsafe_allow_html=True)

contact_left, contact_right = st.columns(2)

with contact_left:
    # Formulaire propre
    st.markdown(f"""
    <div class="contact-box">
        <h3 style="color: #667eea !important; margin-top:0;">Demander une démo</h3>
        <form action="https://formsubmit.co/alymomardiallo75@gmail.com" method="POST">
            <input type="text" name="name" placeholder="Nom de votre commerce" required>
            <input type="text" name="contact" placeholder="Votre Téléphone ou Email" required>
            <textarea name="message" rows="4" placeholder="Votre besoin (ex: Menu Dibiterie)"></textarea>
            <button type="submit" style="width:100%; background: #764ba2; color: white; border: none; padding: 15px; border-radius: 12px; font-weight: bold; cursor: pointer;">ENVOYER MA DEMANDE</button>
        </form>
    </div>
    """, unsafe_allow_html=True)

with contact_right:
    # Section WhatsApp propre
    whatsapp_msg = urllib.parse.quote("Bonjour Aly ! Je souhaite avoir une démo pour mon commerce.")
    whatsapp_url = f"https://wa.me/221776938761?text={whatsapp_msg}"
    
    st.markdown(f"""
        <div style="text-align: center; padding: 30px; background: rgba(255,255,255,0.1); border-radius: 25px; height: 100%;">
            <p style="font-size: 1.3rem; font-weight:600;">Besoin d'une réponse rapide ?</p>
            <p>Discutez en direct avec moi pour votre projet.</p>
            <a href="{whatsapp_url}" class="whatsapp-link" target="_blank">
                💬 PARLER SUR WHATSAPP
            </a>
            <p style="margin-top: 25px; font-size: 0.9rem; opacity: 0.8;">Réponse garantie sous 24h</p>
        </div>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.write("<br><br>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; border-top: 1px solid rgba(255,255,255,0.2); padding-top: 20px;'><p>Aly Momar Diallo | Expert en Digitalisation | Dakar 2026</p></div>", unsafe_allow_html=True)
