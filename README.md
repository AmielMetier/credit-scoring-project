# Credit Scoring & Risk Analysis Dashboard

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![API](https://img.shields.io/badge/API-FastAPI-009688)
![Streamlit](https://img.shields.io/badge/Dashboard-Streamlit-red)
![Finance](https://img.shields.io/badge/Domain-Retail%20Banking-green)

## Contexte du projet

Projet personnel réalisé en tant qu'étudiant ingénieur en Mathématiques Appliquées (Polytech Nice Sophia, spécialité IMAFA).

L'objectif est de construire un modèle qui estime le risque de défaut de paiement d'un client qui demande un crédit. Le modèle doit rester **explicable**, car en banque il faut pouvoir justifier un refus.

## Objectifs

1. **Analyse exploratoire :** comprendre les données et les variables liées au défaut de paiement.
2. **Modélisation :** comparer plusieurs modèles de classification avec l'AUC-ROC (les classes sont très déséquilibrées).
3. **Explicabilité :** regarder les coefficients de la régression logistique pour voir quelles variables pèsent le plus.
4. **Déploiement :** mettre le modèle dans une API et créer un dashboard pour qu'un conseiller puisse analyser un dossier client.

## Données

Les données viennent de la compétition Kaggle **[Home Credit Default Risk](https://www.kaggle.com/c/home-credit-default-risk/data)** (fichier `application_train.csv`, environ 307 000 clients et 122 variables).

Les données brutes sont trop lourdes pour GitHub. Il faut les télécharger et les mettre dans `data/dataset/`.

## Résultats

| Modèle | AUC | Recall (mauvais payeurs) |
|---|---|---|
| **Régression logistique** (retenue) | **0.75** | **67 %** |
| Random Forest | 0.73 | 61 % |

La régression logistique est meilleure ici, plus rapide, et plus facile à expliquer. C'est donc le modèle utilisé dans l'API.

<!-- Ajouter une capture du dashboard ici : ![Dashboard](images/dashboard.png) -->

## Stack technique

* **Langage :** Python
* **Analyse :** Pandas, NumPy
* **Visualisation :** Matplotlib, Seaborn
* **Machine Learning :** Scikit-Learn (régression logistique, Random Forest)
* **API :** FastAPI
* **Dashboard :** Streamlit

## Structure du projet

```
├── api/
│   └── main.py          # API FastAPI qui renvoie le score d'un client
├── app/
│   └── app.py           # Dashboard Streamlit
├── data/
│   ├── dataset/         # Données brutes Kaggle (non versionnées)
│   ├── echantillon_clients.csv          # 50 clients de test pour le dashboard
│   ├── modele_credit_scoring.joblib     # Modèle entraîné
│   └── scaler_credit_scoring.joblib     # Scaler entraîné
├── notebooks/
│   ├── 01_exploration_nettoyage_encodage.ipynb
│   └── 02_modelisation.ipynb
├── requirements.txt
└── README.md
```

## Lancer le projet

1. Installer les dépendances :
```bash
pip install -r requirements.txt
```

2. Lancer l'API (dans un premier terminal) :
```bash
uvicorn api.main:app --reload
```

3. Lancer le dashboard (dans un deuxième terminal) :
```bash
streamlit run app/app.py
```

Le modèle entraîné est déjà dans `data/`, donc pas besoin de relancer les notebooks pour tester le dashboard. Pour réentraîner le modèle, il faut télécharger les données Kaggle puis lancer les deux notebooks dans l'ordre.

## Limites et pistes d'amélioration

* Le score renvoyé n'est pas une vraie probabilité de défaut (à cause du `class_weight='balanced'`). Il faudrait le calibrer.
* Le seuil de 50 % est arbitraire. En vrai, il faudrait le choisir selon le coût d'un mauvais payeur accepté vs un bon client refusé.
* Les valeurs manquantes sont remplacées par la médiane avant la séparation train/test. Il faudrait le faire seulement sur le train.
* Seul le fichier `application_train` est utilisé. Les autres tables Kaggle (historique de crédit, etc.) pourraient améliorer le modèle.
* Tester d'autres modèles (LightGBM) et utiliser SHAP pour expliquer chaque décision individuellement.

## Auteur

Amiel Metier – [GitHub](https://github.com/AmielMetier)
