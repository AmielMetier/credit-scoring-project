import streamlit as st
import requests

#Configuration de la page
st.set_page_config(page_title="Dashboard Credit Scoring")

st.title("Outil d'évaluation de risque de crédit")
st.write("Ce tableau de bord permet d'interroger notre modèle d'IA pour aider les conseillers bancaires dans leurs décisions.")
st.divider()

#Client test
donnees_client_test = {
  "features": [396899.0, 1.0, 157500.0, 770292.0, 30676.5, 688500.0, 0.010147, -13506.0, -105.0, -2876.0, -4402.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 3.0, 2.0, 2.0, 17.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5059979305057544, 0.5943267272127163, 0.4276573700350293, 0.0876, 0.0763, 0.9816, 0.0, 0.1379, 0.1667, 0.0481, 0.0745, 0.0036, 0.084, 0.0746, 0.9816, 0.0, 0.1379, 0.1667, 0.0458, 0.0731, 0.0011, 0.0864, 0.0758, 0.9816, 0.0, 0.1379, 0.1667, 0.0487, 0.0749, 0.0031, 0.0688, 1.0, 0.0, 1.0, 0.0, -428.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,0.0, 0.0, 0.0, 0.0, 0.0]
}

st.subheader("Dossier en cours : Client N° 396899")

#Bouton d'action
if st.button("Lancer l'analyse", use_container_width=True):
    
    #API local dans ../API
    url_api = "http://127.0.0.1:8000/predict" #Démarrer API avant de lancer la page
    
    with st.spinner("Analyse du dossier en cours..."):
        
        try:
            reponse = requests.post(url_api, json=donnees_client_test)
            
            if reponse.status_code == 200:
                resultat = reponse.json()
                
                decision = resultat["decision"]
                probabilite = resultat["probabilite_defaut"] * 100 
                
                st.write("---")

                if decision == "Accepté":
                    st.success(f"Verdict : Prêt {decision} ")
                else:
                    st.error(f"Verdict : Prêt {decision}")
                
                st.metric(label="Probabilité de défaut de paiement", value=f"{probabilite:.1f} %")
                
            else:
                st.error(f"Erreur de l'API : {reponse.text}")
                
        except requests.exceptions.ConnectionError:
            st.error("API non lançée")