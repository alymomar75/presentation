import streamlit as st
import urllib.parse

# --- CONFIGURATION ---
st.set_page_config(page_title="Aly Digital | Solutions QR Sénégal", layout="wide", page_icon="📲")

# --- 1. STYLE CSS (PRO, PROPRE & ACCESSIBLE) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');

    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stToolbar"] {visibility: hidden !important;}
    .stDeployButton {display:none;}

    .stApp {
        background: linear-gradient(135deg, #73A3BF 0%, #FCE1BB 100%);
        background-attachment: fixed;
        font-family: 'Poppins', sans-serif;
        color: #1e293b;
    }

    .service-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        border-bottom: 4px solid #73A3BF;
        height: 100%;
    }

    .price-card {
        background: rgba(255, 255, 255, 0.9);
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }

    .btn-wa-pro {
        background-color: #25D366;
        color: white !important;
        padding: 15px 30px;
        border-radius: 10px;
        text-decoration: none;
        font-weight: 800;
        display: inline-block;
        box-shadow: 0 5px 15px rgba(37, 211, 102, 0.2);
        margin-top: 10px;
    }

    .port-item {
        background: white;
        border-radius: 15px;
        overflow: hidden;
        text-decoration: none;
        display: block;
        color: #1e293b;
        box-shadow: 0 5px 10px rgba(0,0,0,0.05);
    }
    .port-img { width: 100%; height: 140px; object-fit: cover; }
    
    /* Style inputs formulaire */
    input, select, textarea {
        border-radius: 8px !important;
        border: 1px solid #ddd !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. HERO SECTION ---
c1, c2 = st.columns([6, 4])
with c1:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 2.8rem; line-height:1.2;'>Modernisez votre Commerce 🇸🇳</h1>", unsafe_allow_html=True)
    st.write("Solutions QR simples pour **Restaurants, Salons, Boutiques et Parfumeries**.")
    st.markdown("### Hygiénique • Économique • Moderne")
with c2:
    st.image("https://images.unsplash.com/photo-1595079676339-1534801ad6cf?w=500", use_container_width=True)

st.divider()

# --- 3. ARGUMENTS DE VENTE ---
st.markdown("<h3 style='text-align: center;'>Pourquoi passer au Digital ?</h3>", unsafe_allow_html=True)
a1, a2, a3, a4 = st.columns(4)
with a1:
    st.markdown('<div class="service-card">🛡️<br><b>Sanitaire</b><br><small>Zéro contact physique avec le menu papier.</small></div>', unsafe_allow_html=True)
with a2:
    st.markdown('<div class="service-card">⚡<br><b>Mise à jour</b><br><small>Changez vos prix instantanément sans réimprimer.</small></div>', unsafe_allow_html=True)
with a3:
    st.markdown('<div class="service-card">💸<br><b>Moins cher</b><br><small>Économisez sur les frais d\'impression réguliers.</small></div>', unsafe_allow_html=True)
with a4:
    st.markdown('<div class="service-card">📈<br><b>Image Pro</b><br><small>Attirez plus de clients avec un service moderne.</small></div>', unsafe_allow_html=True)

st.write("<br>", unsafe_allow_html=True)

# --- 4. RÉALISATIONS ---
st.markdown("<h3 style='text-align: center;'>Nos clients satisfaits 🤝</h3>", unsafe_allow_html=True)
r1, r2, r3, r4 = st.columns([1, 1.5, 1.5, 1])
with r2:
    st.markdown('<a href="https://kfctest.streamlit.app/" target="_blank" class="port-item"><img src="https://images.unsplash.com/photo-1513639776629-7b61b0ac49cb?w=400" class="port-img"><div style="padding:10px; text-align:center; font-weight:bold;">KFC Sénégal</div></a>', unsafe_allow_html=True)
with r3:
    st.markdown('<a href="https://menuqrcode.streamlit.app/" target="_blank" class="port-item"><img src="https://images.unsplash.com/photo-1509440159596-0249088772ff?w=400" class="port-img"><div style="padding:10px; text-align:center; font-weight:bold;">La Brioche Dorée</div></a>', unsafe_allow_html=True)

st.write("<br>", unsafe_allow_html=True)

# --- 5. TARIFS ---
st.markdown("<h3 style='text-align: center;'>Nos Offres Accessibles 💳</h3>", unsafe_allow_html=True)
o1, o2, o3, o4 = st.columns(4)
packs = [
    {"n": "Pack FLASH", "p": "3 500 F", "d": "Le QR Code simple", "c": "#73A3BF"},
    {"n": "Pack STARTER", "p": "15 000 F", "d": "Menu complet (Max 15 art.)", "c": "#5a8ba8"},
    {"n": "Pack BUSINESS", "p": "35 000 F", "d": "Commandes via WhatsApp", "c": "#4a768e"},
    {"n": "Pack PREMIUM", "p": "Sur Devis", "d": "Solution sur-mesure", "c": "#b08d57"}
]
for i, p in enumerate(packs):
    with (o1 if i==0 else o2 if i==1 else o3 if i==2 else o4):
        st.markdown(f'<div class="price-card"><div style="color:{p["c"]}; font-weight:bold; font-size:0.8rem;">{p["n"]}</div><h2 style="margin:10px 0;">{p["p"]}</h2><p style="font-size:0.85rem; color:#636e72;">{p["d"]}</p></div>', unsafe_allow_html=True)

st.divider()

# --- 6. SECTION CONTACT (WHATSAPP OU EMAIL) ---
st.markdown("<h2 style='text-align: center;'>Contactez-nous pour votre projet ✉️</h2>", unsafe_allow_html=True)
f1, f2, f3 = st.columns([1, 2, 1])

with f2:
    tab1, tab2 = st.tabs(["💬 Via WhatsApp", "📧 Via Email"])
    
    with tab1:
        st.write("Recevez un lien direct pour discuter.")
        nom_wa = st.text_input("Nom de l'établissement (WA)", key="nom_wa")
        num_wa = st.text_input("Votre numéro WhatsApp", placeholder="77 XXX XX XX")
        pack_wa = st.selectbox("Pack choisi", [p['n'] for p in packs], key="p_wa")
        
        if st.button("Générer le lien WhatsApp"):
            if nom_wa and num_wa:
                msg = f"Bonjour Aly ! Je suis le gérant de {nom_wa}. Je souhaite le {pack_wa}. Mon contact : {num_wa}"
                url = f"https://wa.me/221776938761?text={urllib.parse.quote(msg)}"
                st.markdown(f'<div style="text-align:center;"><a href="{url}" target="_blank" class="btn-wa-pro">DÉMARRER SUR WHATSAPP</a></div>', unsafe_allow_html=True)
            else:
                st.error("Merci de remplir tous les champs.")

    with tab2:
        st.write("Envoyez votre demande directement par mail.")
        # Formulaire HTML relié à ton adresse email
        st.markdown(f"""
            <form action="https://formsubmit.co/alymomardiallo75@gmail.com" method="POST" style="background:white; padding:20px; border-radius:10px;">
                <input type="hidden" name="_subject" value="Nouvelle Demande Portfolio">
                <label>Nom de votre Commerce</label><br>
                <input type="text" name="commerce" style="width:100%; padding:10px; margin-bottom:15px;" required><br>
                <label>Numéro de téléphone</label><br>
                <input type="text" name="telephone" style="width:100%; padding:10px; margin-bottom:15px;" required><br>
                <label>Pack souhaité</label><br>
                <select name="pack" style="width:100%; padding:10px; margin-bottom:15px;">
                    <option>Pack FLASH</option>
                    <option>Pack STARTER</option>
                    <option>Pack BUSINESS</option>
                    <option>Pack PREMIUM</option>
                </select><br>
                <button type="submit" style="width:100%; background:#73A3BF; color:white; border:none; padding:15px; border-radius:8px; font-weight:bold; cursor:pointer;">
                    ENVOYER MA DEMANDE PAR EMAIL
                </button>
            </form>
        """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><p style='text-align: center; color: #777; font-size: 0.8rem;'>© 2026 | ALY DIGITAL | DAKAR, SÉNÉGAL 🇸🇳</p>", unsafe_allow_html=True)
