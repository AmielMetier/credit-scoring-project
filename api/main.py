from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

# Initialisation de l'API
app = FastAPI(title="API de Credit Scoring", description="API pour prédire le risque de défaut de paiement")

#Chemin vers le dossier data (marche peu importe d'où on lance l'API)
DOSSIER_DATA = Path(__file__).resolve().parent.parent / "data"

#Seuil de décision : au dessus on refuse le prêt
SEUIL = 0.50

#Chargement du modèle et du scaler
try:
    modele = joblib.load(DOSSIER_DATA / "modele_credit_scoring.joblib")
    scaler = joblib.load(DOSSIER_DATA / "scaler_credit_scoring.joblib")
except FileNotFoundError:
    raise RuntimeError("Fichiers du modèle introuvables, lancer d'abord le notebook 02_modelisation")

#Données uniquement en liste de float
class ClientData(BaseModel):
    features: list[float]

#Page d'accueil
@app.get("/")
def page_d_accueil():
    return {"message": "Le serveur est opérationnel."}

#Prédiction
@app.post("/predict")
def predict_score(client: ClientData):
    #Vérification du nombre de variables
    nb_attendu = scaler.n_features_in_
    if len(client.features) != nb_attendu:
        raise HTTPException(status_code=400, detail=f"Le modèle attend {nb_attendu} variables, reçu {len(client.features)}")

    try:
        #Liste transformée en tableau 2D pour sklearn
        donnees_client = np.array(client.features).reshape(1, -1)

        #Mise à l'échelle
        donnees_scaled = scaler.transform(donnees_client)

        #Score de risque d'être un mauvais payeur
        probabilite = modele.predict_proba(donnees_scaled)[0][1]

        verdict = "Refusé" if probabilite > SEUIL else "Accepté"

        return {
            "probabilite_defaut": float(probabilite),
            "decision": verdict
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erreur lors de la prédiction : {str(e)}")
