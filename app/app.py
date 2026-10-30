from pathlib import Path

import streamlit as st
import requests
import pandas as pd

#Configuration de la page
st.set_page_config(page_title="Dashboard Credit Scoring", layout="centered")

URL_API = "http://127.0.0.1:8000/predict"
CHEMIN_CSV = Path(__file__).resolve().parent.parent / "data" / "echantillon_clients.csv"

@st.cache_data #permet de charger le fichier une seule fois en mémoire
def charger_donnees():
    #l'index du fichier correspond au numéro client (SK_ID_CURR)
    return pd.read_csv(CHEMIN_CSV, index_col=0)

df_clients = charger_donnees()

st.title("Outil d'évaluation du risque de crédit")
st.write("Ce tableau de bord permet d'interroger le modèle de scoring via l'API.")
st.divider()

liste_id_clients = df_clients.index.tolist()
client_id = st.selectbox("Rechercher un numéro de dossier client :", liste_id_clients)

st.subheader(f"Dossier en cours : Client N° {client_id}")

donnees_client_brutes = df_clients.loc[client_id].values
client_propre = [float(valeur) for valeur in donnees_client_brutes]

donnees_pour_api = {
    "features": client_propre
}

# bouton d'action
if st.button("Lancer l'analyse de risque", use_container_width=True):

    with st.spinner(f"Analyse du dossier {client_id} en cours..."):
        try:
            reponse = requests.post(URL_API, json=donnees_pour_api)

            if reponse.status_code == 200:
                resultat = reponse.json()
                decision = resultat["decision"]
                probabilite = resultat["probabilite_defaut"] * 100

                st.write("---")
                if decision == "Accepté":
                    st.success(f"Verdict : Prêt {decision}")
                else:
                    st.error(f"Verdict : Prêt {decision}")

                st.metric(label="Score de risque de défaut", value=f"{probabilite:.1f} %")

            else:
                st.error(f"Erreur de l'API : {reponse.text}")

        except requests.exceptions.ConnectionError:
            st.error("Impossible de joindre l'API. Il faut lancer l'API avant le dashboard.")

#Graphique
st.divider()
st.subheader("Analyse détaillée du profil")
st.write("Comparez ce client avec la médiane des clients de l'échantillon :")

liste_colonnes = [col for col in df_clients.columns if col != "SK_ID_CURR"]
colonne_choisie = st.selectbox("Sélectionnez le critère à analyser :", liste_colonnes)

valeur_client = df_clients.loc[client_id, colonne_choisie]
valeur_mediane = df_clients[colonne_choisie].median()

df_graphique = pd.DataFrame({"Valeur": [valeur_client, valeur_mediane]}, index=[f"Client {client_id}", "Médiane des clients"])

st.bar_chart(df_graphique)
