import streamlit as st
import urllib.parse

# Configuration de la page
st.set_page_config(page_title="Aly Momar Diallo | Digital Pro", layout="wide", page_icon="📲")

# --- STYLE CSS (MASQUAGE GITHUB + DESIGN CANVA) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;600;800&display=swap');

    /* 1. CACHER LA BARRE GITHUB ET LE MENU STREAMLIT */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    stDeployButton {display:none;}
    [data-testid="stToolbar"] {visibility: hidden !important;}

    /* 2. FOND ET POLICE */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Outfit', sans-serif;
        color: #ffffff;
    }

    /* 3. CARTES PRO */
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

    .icon-box { font-size: 3rem; margin-bottom: 15px; }
    h1, h2, h3 { font-weight: 800 !important; color: #ffffff !important; }

    /* 4. IMAGE HERO */
    .hero-img {
        border-radius: 30px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.3);
        width: 100%;
        max-height: 450px;
        object-fit: cover;
    }

    /* 5. BOUTON WHATSAPP */
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
    }

    /* 6. FORMULAIRE */
    .contact-box {
        background: white; 
        padding: 35px; 
        border-radius: 30px; 
        color: #2d3436;
    }
    input, textarea {
        background: #f8f9fa !important;
        border-radius: 12px !important;
        border: 1px solid #e9ecef !important;
        color: #2d3436 !important;
        width: 100%;
        padding: 12px;
        margin-bottom: 15px;
    }

    ul { list-style: none; padding: 0; text-align: left; }
    li { margin-bottom: 10px; font-size: 0.9rem; }
    </style>
""", unsafe_allow_html=True)

# --- 1. SECTION HERO ---
col_text, col_img = st.columns([5, 5])

with col_text:
    st.write("<br><br>", unsafe_allow_html=True)
    st.markdown("# Modernisez votre commerce en un Scan ⚡")
    st.markdown("### Aly Momar Diallo digitalise les commerces de proximité à Dakar.")
    st.write("""
        Passez au digital dès aujourd'hui. Idéal pour les Fast-foods, Dibiteries, 
        Salons de coiffure et Boutiques. Une solution propre, moderne et rapide.
    """)
    st.markdown("<br>", unsafe_allow_html=True)
    st.success("✅ **Zéro papier, 100% Hygiénique, 100% Sénégalais.**")

with col_img:
    st.markdown("""
        <img src="https://images.unsplash.com/photo-1595079676339-1534801ad6cf?q=80&w=1000&auto=format&fit=crop" class="hero-img">
    """, unsafe_allow_html=True)

st.divider()

# --- 2. ARGUMENTS ---
st.markdown("<h2 style='text-align: center;'>Pourquoi choisir le Digital ?</h2>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

a1, a2, a3 = st.columns(3)
with a1:
    st.markdown("""<div class="pro-card"><div class="icon-box">🧼</div><h3>Hygiène Maximale</h3><p>Solution "Zero-Contact". Plus de menus sales ou déchirés qui circulent.</p></div>""", unsafe_allow_html=True)
with a2:
    st.markdown("""<div class="pro-card"><div class="icon-box">🚀</div><h3>Gain de temps</h3><p>Vos clients scannent et choisissent en toute autonomie. Service plus fluide.</p></div>""", unsafe_allow_html=True)
with a3:
    st.markdown("""<div class="pro-card"><div class="icon-box">💎</div><h3>Image Moderne</h3><p>Valorisez votre commerce avec une interface élégante et innovante.</p></div>""", unsafe_allow_html=True)

st.write("<br>", unsafe_allow_html=True)
st.divider()

# --- 3. LES TARIFS (PACKS CFA) ---
st.markdown("<h2 style='text-align: center;'>Nos Offres Digitales 💳</h2>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

p1, p2, p3, p4 = st.columns(4)

with p1:
    st.markdown("""
    <div class="pro-card">
        <h3 style="color: #FF9F43 !important;">Pack FLASH</h3>
        <p style="font-size: 1.8rem; font-weight: 800;">3 500 F CFA</p>
        <p style="font-size: 0.8rem; opacity: 0.8;">L'essentiel pour démarrer</p>
        <hr style="opacity: 0.2;">
        <ul>
            <li>✅ Création de votre QR Code</li>
            <li>✅ Redirection vers votre page</li>
            <li>✅ Fichier prêt à imprimer</li>
            <li>✅ Support WhatsApp</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with p2:
    st.markdown("""
    <div class="pro-card">
        <h3 style="color: #FFD700 !important;">Pack STARTER</h3>
        <p style="font-size: 1.8rem; font-weight: 800;">15 000 F CFA</p>
        <p style="font-size: 0.8rem; opacity: 0.8;">Salons & Boutiques</p>
        <hr style="opacity: 0.2;">
        <ul>
            <li>✅ Menu Digital (Max 15 articles)</li>
            <li>✅ 1 QR Code personnalisé</li>
            <li>✅ Mise à jour mensuelle</li>
            <li>✅ Assistance WhatsApp</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with p3:
    st.markdown("""
    <div class="pro-card" style="border: 2px solid #38bdf8; background: rgba(56, 189, 248, 0.1);">
        <h3 style="color: #38bdf8 !important;">Pack BUSINESS</h3>
        <p style="font-size: 1.8rem; font-weight: 800;">35 000 F CFA</p>
        <p style="font-size: 0.8rem; opacity: 0.8;">Dibiteries & Fast-food</p>
        <hr style="opacity: 0.2;">
        <ul>
            <li>✅ Menu Illimité + Photos</li>
            <li>✅ <b>Commande WhatsApp directe</b></li>
            <li>✅ 3 Stickers QR Codes offerts</li>
            <li>✅ Formation rapide</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with p4:
    st.markdown("""
    <div class="pro-card">
        <h3 style="color: #A29BFE !important;">Pack PREMIUM</h3>
        <p style="font-size: 1.8rem; font-weight: 800;">SUR DEVIS</p>
        <p style="font-size: 0.8rem; opacity: 0.8;">Restaurants & Chaînes</p>
        <hr style="opacity: 0.2;">
        <ul>
            <li>✅ Gestion Multi-sites</li>
            <li>✅ Design sur-mesure</li>
            <li>✅ Statistiques de visite</li>
            <li>✅ Support VIP 24h/7j</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.write("<br><br>", unsafe_allow_html=True)
st.divider()

# --- 4. SECTION CONTACT ---
st.markdown("<h2 style='text-align: center;'>Prêt pour le changement ? 🚀</h2>", unsafe_allow_html=True)

contact_l, contact_r = st.columns(2)

with contact_l:
    st.markdown(f"""
    <div class="contact-box">
        <h3 style="color: #764ba2 !important; margin-top:0;">Demander un devis</h3>
        <form action="https://formsubmit.co/alymomardiallo75@gmail.com" method="POST">
            <input type="text" name="commerce" placeholder="Nom de votre commerce" required>
            <input type="text" name="contact" placeholder="Votre numéro WhatsApp ou Email" required>
            <textarea name="message" rows="4" placeholder="Quel pack vous intéresse ?"></textarea>
            <button type="submit" style="width:100%; background: #764ba2; color: white; border: none; padding: 15px; border-radius: 12px; font-weight: bold; cursor: pointer;">ENVOYER MA DEMANDE</button>
        </form>
    </div>
    """, unsafe_allow_html=True)

with contact_r:
    whatsapp_msg = urllib.parse.quote("Bonjour Aly ! Je souhaite une démo pour mon commerce.")
    whatsapp_url = f"https://wa.me/221776938761?text={whatsapp_msg}"
    
    st.markdown(f"""
        <div style="text-align: center; padding: 40px; background: rgba(255,255,255,0.1); border-radius: 30px; height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center;">
            <p style="font-size: 1.4rem; font-weight:600;">Réponse immédiate sur WhatsApp</p>
            <p>Cliquez ci-dessous pour discuter de votre projet.</p>
            <br>
            <a href="{whatsapp_url}" class="whatsapp-link" target="_blank">
                💬 CONTACTER ALY SUR WHATSAPP
            </a>
            <p style="margin-top: 30px; font-size: 0.9rem; opacity: 0.8;">Service disponible 7j/7.</p>
        </div>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.write("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: center; border-top: 1px solid rgba(255,255,255,0.2); padding: 20px;">
        <p>© 2026 | Aly Momar Diallo | Expert Digital | Dakar, Sénégal 🇸🇳</p>
    </div>
""", unsafe_allow_html=True)
