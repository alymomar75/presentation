import streamlit as st
import urllib.parse

# Configuration
st.set_page_config(page_title="Aly Momar Diallo | Digital Fluid", layout="wide", page_icon="📲")

# --- STYLE CSS & JAVASCRIPT (EFFET FLUIDE GYROSCOPIQUE) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');

    /* Masquage Streamlit */
    #MainMenu, footer, header {{visibility: hidden;}}
    [data-testid="stToolbar"] {{visibility: hidden !important;}}
    stDeployButton {{display:none;}}

    /* Fond de base avec tes couleurs */
    .stApp {{
        background: linear-gradient(135deg, #73A3BF 0%, #FCE1BB 100%);
        background-attachment: fixed;
        transition: background 0.1s ease-out;
        font-family: 'Poppins', sans-serif;
        color: #1e293b;
    }

    /* Cartes Canva Style */
    .canva-card {{
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(10px);
        padding: 25px;
        border-radius: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        color: #2D3436;
        text-align: center;
        margin-bottom: 15px;
        border: 1px solid rgba(255, 255, 255, 0.3);
    }

    .hero-img {{
        border-radius: 40px;
        box-shadow: 0 15px 45px rgba(0,0,0,0.2);
        width: 100%;
        max-height: 350px;
        object-fit: cover;
    }

    .btn-whatsapp {{
        background-color: #25D366;
        color: white !important;
        padding: 18px 30px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 800;
        display: block;
        text-align: center;
        margin: 10px 0;
    }
    </style>

    <script>
    // Script pour le mouvement fluide des couleurs
    const doc = document.querySelector('.stApp');
    
    function handleOrientation(event) {{
        let x = event.beta;  // Inclinaison avant/arrière (-180 to 180)
        let y = event.gamma; // Inclinaison gauche/droite (-90 to 90)
        
        // On normalise pour obtenir un pourcentage
        let percentageX = (x + 90) / 1.8;
        let percentageY = (y + 90) / 1.8;
        
        doc.style.background = `linear-gradient(${{percentageX + percentageY}}deg, #73A3BF 0%, #FCE1BB 100%)`;
    }

    // Demande d'autorisation pour iOS 13+
    function requestAccess() {{
        if (typeof DeviceOrientationEvent.requestPermission === 'function') {{
            DeviceOrientationEvent.requestPermission()
                .then(permissionState => {{
                    if (permissionState === 'granted') {{
                        window.addEventListener('deviceorientation', handleOrientation);
                    }}
                }})
                .catch(console.error);
        }} else {{
            window.addEventListener('deviceorientation', handleOrientation);
        }}
    }
    
    // On active au premier clic sur la page
    window.addEventListener('click', requestAccess, {{once: true}});
    </script>
""", unsafe_allow_html=True)

# --- CONTENU ---
col_text, col_img = st.columns([5, 5])

with col_text:
    st.write("<br>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 2.8rem;'>Le Digital en Mouvement 🌊</h1>", unsafe_allow_html=True)
    st.markdown("### Par Aly Momar Diallo")
    st.write("Une solution moderne et hygiénique pour booster votre commerce à Dakar.")
    st.warning("📱 **Conseil :** Inclinez votre téléphone pour voir le fond bouger !")

with col_img:
    st.markdown("""<img src="https://images.unsplash.com/photo-1595079676339-1534801ad6cf?q=80&w=1000&auto=format&fit=crop" class="hero-img">""", unsafe_allow_html=True)

st.write("<br>", unsafe_allow_html=True)

# --- PACKS TARIFS ---
st.markdown("<h2 style='text-align: center;'>Nos Offres 💳</h2>", unsafe_allow_html=True)
p1, p2, p3, p4 = st.columns(4)

packs = [
    {"n": "Pack FLASH", "p": "3 500 F", "d": "Le QR Code simple", "c": "#73A3BF"},
    {"n": "Pack STARTER", "p": "15 000 F", "d": "Menu (Max 15 art.)", "c": "#5a8ba8"},
    {"n": "Pack BUSINESS", "p": "35 000 F", "d": "Commande WhatsApp", "c": "#4a768e"},
    {"n": "Pack PREMIUM", "p": "Sur Devis", "d": "Luxe Sur-mesure", "c": "#b08d57"}
]

for i, p in enumerate(packs):
    with (p1 if i==0 else p2 if i==1 else p3 if i==2 else p4):
        st.markdown(f"""
        <div class="canva-card">
            <span style="background:{p['c']}; color:white; padding:5px 15px; border-radius:20px; font-size:0.7rem; font-weight:bold;">{p['n']}</span>
            <h2 style="margin:15px 0;">{p['p']}</h2>
            <p style="font-size:0.8rem; color:#636e72;">{p['d']}</p>
        </div>
        """, unsafe_allow_html=True)

# --- CONTACT ---
st.write("<br>", unsafe_allow_html=True)
c_left, c_right = st.columns(2)

with c_left:
    st.markdown(f"""
    <div style="background: white; padding: 30px; border-radius: 30px; color: #2D3436; border: 1px solid #ddd;">
        <h3 style="margin-top:0;">M'envoyer un mail 📧</h3>
        <form action="https://formsubmit.co/alymomardiallo75@gmail.com" method="POST">
            <input type="text" name="commerce" placeholder="Votre Commerce" required style="width:100%; padding:12px; margin-bottom:10px; border-radius:15px; border:1px solid #eee;">
            <input type="text" name="contact" placeholder="Téléphone ou Email" required style="width:100%; padding:12px; margin-bottom:10px; border-radius:15px; border:1px solid #eee;">
            <button type="submit" style="width:100%; background: #73A3BF; color: white; border: none; padding: 15px; border-radius: 15px; font-weight: bold; cursor: pointer;">ENVOYER</button>
        </form>
    </div>
    """, unsafe_allow_html=True)

with c_right:
    whatsapp_msg = urllib.parse.quote("Bonjour Aly ! Je suis intéressé par votre solution digitale.")
    whatsapp_url = f"https://wa.me/221776938761?text={whatsapp_msg}"
    st.markdown(f"""
        <div style="text-align: center; padding: 20px;">
            <p style="font-size:1.1rem; font-weight:bold;">Besoin d'une réponse rapide ?</p>
            <a href="{whatsapp_url}" class="btn-whatsapp" target="_blank">
                💬 WHATSAPP DIRECT
            </a>
            <p style="font-size:0.8rem; opacity:0.8;">Réponse sous 24h</p>
        </div>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<p style='text-align: center; color: #555; font-size: 0.7rem; margin-top:40px;'>© 2026 | ALY MOMAR DIALLO | DAKAR 🇸🇳</p>", unsafe_allow_html=True)
