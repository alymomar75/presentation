import streamlit as st
import urllib.parse

# Configuration de la page
st.set_page_config(page_title="Aly Momar Diallo | Digitalisation de Proximité", layout="wide", page_icon="🚀")

# --- STYLE CSS ---
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
    .service-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        height: 250px;
    }
    .badge {
        background-color: #38bdf8;
        color: #0f172a;
        padding: 5px 15px;
        border-radius: 20px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown("<span class='badge'>INNOVATION DAKAR 2026</span>", unsafe_allow_html=True)
st.title("Digitalisez votre Commerce avec Aly Momar Diallo")
st.subheader("La solution QR Code : Moderne, Économique et Hygiénique.")

st.divider()

# --- ARGUMENTS FORTS (INCLUANT L'HYGIÈNE) ---
st.header("Pourquoi passer au digital ?")
arg1, arg2, arg3, arg4 = st.columns(4)

with arg1:
    st.markdown("### 🧼 Hygiène Top")
    st.write("Zéro contact physique. Vos clients scannent avec leur propre téléphone. Plus de menus sales ou déchirés.")
with arg2:
    st.markdown("### ⚡ Rapidité")
    st.write("Le menu est disponible instantanément. Vos serveurs se concentrent sur le service, pas sur la prise de commande.")
with arg3:
    st.markdown("### 📉 Économie")
    st.write("Modifiez vos prix et produits en un clic sans jamais rien réimprimer. Gain d'argent immédiat.")
with arg4:
    st.markdown("### 🇸🇳 Proximité")
    st.write("Une solution pensée pour le marché sénégalais : Dibiteries, Salons, Fast-food et Boutiques.")

# --- SECTION CONTACT DYNAMIQUE ---
st.divider()
st.header("📲 Contactez-moi pour une démo")

col_left, col_right = st.columns(2)

with col_left:
    st.write("Vous souhaitez moderniser votre commerce ? Remplissez ces informations et je vous contacterai pour une démonstration gratuite.")
    
    # Formulaire via FormSubmit (pour recevoir sur ton email)
    # Note : Le premier envoi demandera une confirmation par email de ta part.
    contact_form = f"""
    <form action="https://formsubmit.co/alymomardiallo75@gmail.com" method="POST" style="background:rgba(255,255,255,0.1); padding:20px; border-radius:15px;">
        <input type="text" name="name" placeholder="Nom du Commerce" style="width:100%; margin-bottom:10px; border-radius:5px; border:none; padding:10px;" required>
        <input type="text" name="contact" placeholder="Votre Téléphone ou Email" style="width:100%; margin-bottom:10px; border-radius:5px; border:none; padding:10px;" required>
        <textarea name="message" placeholder="Dites-moi quel est votre secteur (ex: Dibiterie)" style="width:100%; margin-bottom:10px; border-radius:5px; border:none; padding:10px;" required></textarea>
        <button type="submit" style="background-color:#38bdf8; color:white; border:none; padding:10px 20px; border-radius:5px; cursor:pointer; width:100%; font-weight:bold;">ENVOYER MA DEMANDE</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

with col_right:
    st.write("--- OU ---")
    st.write("Discutez directement avec moi sur WhatsApp pour une réponse instantanée :")
    
    # Bouton WhatsApp Direct
    whatsapp_msg = urllib.parse.quote("Bonjour Aly, je suis intéressé par votre solution de menu QR Code pour mon commerce.")
    whatsapp_url = f"https://wa.me/221776938761?text={whatsapp_msg}"
    
    st.markdown(f"""
        <a href="{whatsapp_url}" target="_blank" style="text-decoration:none;">
            <div style="background-color:#25D366; color:white; padding:20px; border-radius:15px; text-align:center; font-weight:bold; font-size:1.2rem;">
                💬 CONTACTER ALY SUR WHATSAPP
            </div>
        </a>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#94a3b8;'>Aly Momar Diallo - Projet Académique 2026 - Dakar, Sénégal</p>", unsafe_allow_html=True)
