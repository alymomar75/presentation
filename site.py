# --- SECTION TARIFS (PACKS RAISONNABLES) ---
st.divider()
st.markdown("<h2 style='text-align: center; color: white !important;'>Nos Offres Digitales 💳</h2>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

p1, p2, p3 = st.columns(3)

with p1:
    st.markdown("""
    <div class="pro-card">
        <h3 style="color: #FFD700 !important;">Pack STARTER</h3>
        <p style="font-size: 1.5rem; font-weight: bold;">15 000 F CFA</p>
        <p style="font-size: 0.9rem; opacity: 0.8;">Idéal pour : Salons de coiffure, Boutiques</p>
        <hr style="opacity: 0.2;">
        <ul style="text-align: left; font-size: 0.9rem; list-style: none; padding: 0;">
            <li>✅ Menu/Catalogue Digital (Max 15 articles)</li>
            <li>✅ 1 QR Code personnalisé à imprimer</li>
            <li>✅ Mise à jour mensuelle gratuite</li>
            <li>✅ Assistance WhatsApp</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with p2:
    st.markdown("""
    <div class="pro-card" style="border: 2px solid #38bdf8; background: rgba(56, 189, 248, 0.1);">
        <div style="background: #38bdf8; color: #0f172a; font-size: 0.7rem; font-weight: bold; border-radius: 10px; padding: 2px 10px; display: inline-block; margin-bottom: 10px;">RECOMMANDÉ</div>
        <h3 style="color: #38bdf8 !important;">Pack BUSINESS</h3>
        <p style="font-size: 1.5rem; font-weight: bold;">35 000 F CFA</p>
        <p style="font-size: 0.9rem; opacity: 0.8;">Idéal pour : Dibiteries, Fast-food</p>
        <hr style="opacity: 0.2;">
        <ul style="text-align: left; font-size: 0.9rem; list-style: none; padding: 0;">
            <li>✅ Menu Illimité + Catégories</li>
            <li>✅ <b>Intégration Commande WhatsApp</b></li>
            <li>✅ 3 QR Codes autocollants offerts</li>
            <li>✅ Formation à l'utilisation</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with p3:
    st.markdown("""
    <div class="pro-card">
        <h3 style="color: #A29BFE !important;">Pack PREMIUM</h3>
        <p style="font-size: 1.5rem; font-weight: bold;">Sur Devis</p>
        <p style="font-size: 0.9rem; opacity: 0.8;">Idéal pour : Restaurants, Chaînes</p>
        <hr style="opacity: 0.2;">
        <ul style="text-align: left; font-size: 0.9rem; list-style: none; padding: 0;">
            <li>✅ Multi-établissements</li>
            <li>✅ Statistiques de consultation</li>
            <li>✅ Design sur-mesure (Couleurs de marque)</li>
            <li>✅ Support VIP 24h/7j</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
