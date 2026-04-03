import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Aly Momar Diallo | Digitalisation de Proximité",
    layout="wide",
    page_icon="🚀"
)

# --- STYLE CSS (FUTURISTE & ÉPURÉ) ---
st.markdown("""
    <style>
    @keyframes aurora {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .stApp {
        background: linear-gradient(-45deg, #0f172a, #1e293b, #334155, #0f172a);
        background-size: 400% 400%;
        animation: aurora 15s ease infinite;
        color: #f8fafc;
    }

    /* Titres et Textes */
    h1, h2 {
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        letter-spacing: -1px;
        color: #38bdf8 !important;
    }

    .subtitle {
        font-size: 1.5rem;
        color: #94a3b8;
        margin-bottom: 2rem;
    }

    /* Cartes de Service */
    .service-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        transition: 0.4s;
    }

    .service-card:hover {
        transform: translateY(-10px);
        background: rgba(255, 255, 255, 0.1);
        border-color: #38bdf8;
    }

    /* Badge Aly Diallo */
    .badge {
        background-color: #38bdf8;
        color: #0f172a;
        padding: 5px 15px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 0.8rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER / HERO SECTION ---
st.markdown("<span class='badge'>PROJET ACADÉMIQUE 2026</span>", unsafe_allow_html=True)
st.title("L'Avenir du Commerce de Proximité au Sénégal 🇸🇳")
st.markdown("<p class='subtitle'>Digitalisation par QR Code pour Fast-Foods, Dibiteries et Salons de Coiffure.</p>", unsafe_allow_html=True)

st.divider()

# --- VISION DU PROJET ---
col_vision, col_img = st.columns([6, 4])

with col_vision:
    st.header("Ma Vision")
    st.write("""
        Je suis **Aly Momar Diallo**, étudiant passionné par l'innovation technologique. 
        Mon projet consiste à briser la barrière entre le commerce traditionnel et le digital.
        
        L'objectif est simple : permettre à chaque commerce de quartier — qu'il s'agisse d'une dibiterie, d'un salon de coiffure ou d'une parfumerie — 
        de proposer une expérience client **moderne, rapide et sans contact** via un menu ou catalogue digital accessible par simple scan QR Code.
    """)
    st.info("💡 **Innovation :** Pas d'application à télécharger. Une interface web fluide, directement dans le navigateur du client.")

with col_img:
    # Illustration d'un QR code ou d'un smartphone (image générique)
    st.image("https://images.unsplash.com/photo-1595079676339-1534801ad6cf?q=80&w=500&auto=format&fit=crop", caption="Le futur est dans le scan")

# --- LES SECTEURS VISÉS ---
st.header("Des solutions pour chaque métier")
s1, s2, s3, s4 = st.columns(4)

with s1:
    st.markdown("""<div class="service-card"><h3>🍔</h3><h4>Fast-Food</h4><p>Menus interactifs avec prise de commande WhatsApp.</p></div>""", unsafe_allow_html=True)
with s2:
    st.markdown("""<div class="service-card"><h3>🥩</h3><h4>Dibiteries</h4><p>Affichage des tarifs du jour et disponibilités en temps réel.</p></div>""", unsafe_allow_html=True)
with s3:
    st.markdown("""<div class="service-card"><h3>✂️</h3><h4>Salons</h4><p>Catalogue des coiffures et tarifs des prestations.</p></div>""", unsafe_allow_html=True)
with s4:
    st.markdown("""<div class="service-card"><h3>✨</h3><h4>Parfumerie</h4><p>Galerie produit élégante pour une immersion totale.</p></div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- POURQUOI CETTE SOLUTION ? ---
st.divider()
st.header("Pourquoi se moderniser ?")
c1, c2, c3 = st.columns(3)

with c1:
    st.subheader("🚀 Rapidité")
    st.write("Réduction du temps d'attente. Le client consulte le catalogue dès son arrivée.")
with c2:
    st.subheader("💰 Économie")
    st.write("Plus besoin d'imprimer des menus papier coûteux qui changent tous les mois.")
with c3:
    st.subheader("🌍 Image")
    st.write("Valorisez votre commerce avec une image technologique et innovante.")

# --- CONTACT & FOOTER ---
st.divider()
st.markdown("<h2 style='text-align: center;'>Contactez-moi pour une démo</h2>", unsafe_allow_html=True)

# Formulaire de contact simulé
contact_col1, contact_col2, contact_col3 = st.columns([2, 2, 2])
with contact_col2:
    nom = st.text_input("Nom de votre commerce")
    email = st.text_input("Votre Email/WhatsApp")
    if st.button("Demander une étude gratuite"):
        st.success(f"Merci ! Aly reviendra vers {nom} très prochainement.")

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: center; color: #94a3b8; font-size: 0.8rem; padding: 20px;">
        Conçu avec ❤️ par Aly Momar Diallo | Étudiant en Géomatique & Développeur Passionné<br>
        © 2026 - Déployé sur Streamlit Cloud
    </div>
""", unsafe_allow_html=True)
