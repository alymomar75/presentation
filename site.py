import streamlit as st
import urllib.parse

# --- CONFIGURATION ---
st.set_page_config(page_title="Aly Digital | Menus QR pour Tous", layout="wide", page_icon="📲")

# --- 1. STYLE CSS (ACCESSIBLE & PRO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');

    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stToolbar"] {visibility: hidden !important;}
    .stDeployButton {display:none;}

    .stApp {
        background: linear-gradient(135deg, #73A3BF 0%, #FCE1BB 100%);
        background-attachment: fixed;
        transition: background 0.8s ease;
        font-family: 'Poppins', sans-serif;
        color: #1e293b;
    }

    /* Cartes de service claires */
    .service-card {
        background: white;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        text-align: center;
        margin-bottom: 20px;
        border-top: 5px solid #73A3BF;
    }

    /* Portfolio accessible */
    .port-card {
        background: white;
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        text-decoration: none;
        display: block;
        color: #1e293b;
        margin-bottom: 20px;
        transition: 0.3s;
    }
    .port-card:hover { transform: scale(1.02); }
    .port-img { width: 100%; height: 160px; object-fit: cover; }
    .port-info { padding: 12px; font-weight: 600; text-align: center; font-size: 0.9rem; }

    /* Bouton WhatsApp Officiel Vert */
    .btn-wa-click {
        background-color: #25D366;
        color: white !important;
        padding: 18px 30px;
        border-radius: 12px;
        text-decoration: none;
        font-weight: 800;
        display: inline-block;
        box-shadow: 0 8px 15px rgba(37, 211, 102, 0.2);
        font-size: 1.1rem;
        border: none;
    }

    /* Formulaire simplifié */
    [data-testid="stForm"] {
        background: white !important;
        border-radius: 20px !important;
        padding: 25px !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05) !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. JS MOUVEMENT (LÉGER) ---
st.components.v1.html("""
    <script>
    const app = window.parent.document.querySelector('.stApp');
    window.parent.addEventListener('mousemove', (e) => {
        let x = e.clientX / window.parent.innerWidth;
        app.style.background = `linear-gradient(${x * 360}deg, #73A3BF 0%, #FCE1BB 100%)`;
    });
    </script>
""", height=0)

# --- 3. HERO SECTION (MESSAGE SIMPLE) ---
col_1, col_2 = st.columns([6, 4])
with col_1:
    st.write("<br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 3rem;'>Votre Menu sur Smartphone 📲</h1>", unsafe_allow_html=True)
    st.markdown("### Aly Digital — Solutions QR à Dakar")
    st.write("Fini les menus papier déchirés. Proposez un menu digital simple, rapide et pas cher à vos clients.")
    st.success("✅ **Économique :** À partir de 3 500 F seulement.")
with col_2:
    st.markdown("""<img src="https://images.unsplash.com/photo-1595079676339-1534801ad6cf?w=600" style="border-radius:20px; width:100%;">""", unsafe_allow_html=True)

st.divider()

# --- 4. RÉALISATIONS (NOS CLIENTS) ---
st.markdown("<h3 style='text-align: center; margin-bottom: 25px;'>Ils nous font confiance 🤝</h3>", unsafe_allow_html=True)
realisations = [
    {"nom": "KFC Sénégal", "url": "https://kfctest.streamlit.app/", "img": "https://images.unsplash.com/photo-1513639776629-7b61b0ac49cb?w=400"},
    {"nom": "La Brioche Dorée", "url": "https://menuqrcode.streamlit.app/", "img": "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=400"}
]
r1, r2, r3, r4 = st.columns([1, 1.5, 1.5, 1])
with r2:
    st.markdown(f'<a href="{realisations[0]["url"]}" target="_blank" class="port-card"><img src="{realisations[0]["img"]}" class="port-img"><div class="port-info">{realisations[0]["nom"]}</div></a>', unsafe_allow_html=True)
with r3:
    st.markdown(f'<a href="{realisations[1]["url"]}" target="_blank" class="port-card"><img src="{realisations[1]["img"]}" class="port-img"><div class="port-info">{realisations[1]["nom"]}</div></a>', unsafe_allow_html=True)

# --- 5. NOS PACKS (ACCESSIBLES) ---
st.markdown("<h3 style='text-align: center; margin-top: 40px;'>Nos Tarifs Simples 💳</h3>", unsafe_allow_html=True)
o1, o2, o3, o4 = st.columns(4)

packs = [
    {"n": "Pack FLASH", "p": "3 500 F", "d": "Le QR Code simple", "c": "#73A3BF"},
    {"n": "Pack STARTER", "p": "15 000 F", "d": "Menu Complet", "c": "#5a8ba8"},
    {"n": "Pack BUSINESS", "p": "35 000 F", "d": "Commande Directe", "c": "#4a768e"},
    {"n": "Pack PREMIUM", "p": "Sur Devis", "d": "Sur-mesure", "c": "#b08d57"}
]

for i, p in enumerate(packs):
    with (o1 if i==0 else o2 if i==1 else o3 if i==2 else o4):
        st.markdown(f"""
        <div class="service-card">
            <div style="color:{p['c']}; font-weight:bold; font-size:0.8rem;">{p['n']}</div>
            <h2 style="margin:10px 0; color:#1e293b;">{p['p']}</h2>
            <p style="font-size:0.85rem; color:#636e72;">{p['d']}</p>
        </div>
        """, unsafe_allow_html=True)

# --- 6. FORMULAIRE DE DEVIS (EN DERNIER) ---
st.write("<br>")
st.markdown("<h3 style='text-align: center;'>Lancez votre projet maintenant ✍️</h3>", unsafe_allow_html=True)
f_col1, f_col2, f_col3 = st.columns([1, 2, 1])

with f_col2:
    with st.form("devis_form"):
        etablissement = st.text_input("Nom de votre Commerce", placeholder="Ex: Boutique Aly, Fast-Food...")
        choix_pack = st.selectbox("Quel service vous intéresse ?", ["Pack FLASH (3 500 F)", "Pack STARTER (15 000 F)", "Pack BUSINESS (35 000 F)", "Pack PREMIUM"])
        details = st.text_area("Besoin particulier ?", placeholder="Dites-moi en quelques mots ce qu'il vous faut...")
        
        btn_submit = st.form_submit_button("Valider ma demande")
        
        if btn_submit:
            if etablissement:
                msg = f"Bonjour Aly ! Je suis le responsable de {etablissement}. Je souhaite le {choix_pack}. Infos : {details}"
                url_wa = f"https://wa.me/221776938761?text={urllib.parse.quote(msg)}"
                st.markdown(f"""
                    <div style="text-align: center; margin-top: 15px;">
                        <a href="{url_wa}" target="_blank" class="btn-wa-click">
                             💬 ENVOYER SUR WHATSAPP
                        </a>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.error("Veuillez entrer le nom de votre commerce.")

# --- FOOTER ---
st.write("<br><br>")
st.markdown("<p style='text-align: center; color: #777; font-size: 0.8rem;'>© 2026 | ALY MOMAR DIALLO | DAKAR 🇸🇳</p>", unsafe_allow_html=True)
