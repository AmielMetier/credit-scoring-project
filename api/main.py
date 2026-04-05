from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

# Initialisation de l'API
app = FastAPI(title="API de Credit Scoring", description="API pour prédire le risque de défaut de paiement")

#Chargement du modèle et du scaler
try:
    modele = joblib.load("../data/modele_credit_scoring.joblib")
    scaler = joblib.load("../data/scaler_credit_scoring.joblib")
except FileNotFoundError:
    print("ERREUR")
    print("Fichiers du modèle introuvables")

#Données uniquement en list de float
class ClientData(BaseModel):
    features: list[float]

#Page d'acceuil
@app.get("/")
def page_d_accueil():
    return {"Le serveur est opérationnel. "}

#Prediction
@app.post("/predict")
def predict_score(client: ClientData):
    try:
        #List transformer en tableau 2D pour sklearn
        donnees_client = np.array(client.features).reshape(1, -1)
        
        #Mise à l'échelle
        donnees_scaled = scaler.transform(donnees_client)
        
        #Calcul de la probabilité d'être un mauvais payeur 
        probabilite = modele.predict_proba(donnees_scaled)[0][1]
        
        #On coupe à 50% de probabilité
        verdict = "Refusé" if probabilite > 0.50 else "Accepté"
        
        return {
            "probabilite_defaut": float(probabilite),
            "decision": verdict
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erreur lors de la prédiction : {str(e)}")