# Credit Scoring & Risk Analysis Dashboard

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn%20%7C%20LightGBM-orange)
![Streamlit](https://img.shields.io/badge/Dashboard-Streamlit-red)
![Finance](https://img.shields.io/badge/Domain-Retail%20Banking-green)

## Contexte du Projet

Ce projet a été réalisé dans le cadre d'un projet personnel de 3 semaines. En tant qu'étudiant Ingénieur en Mathématiques Appliquées, l'objectif est d'illustrer mes compétences en **Data Analyse et Machine Learning appliquées aux problématiques bancaires**. 

L'octroi de crédit est au cœur du métier de la banque de détail. Ce projet vise à construire un modèle prédictif capable d'évaluer le risque de défaut de paiement d'un client, tout en garantissant l'**explicabilité** de la décision (une exigence réglementaire et métier stricte en finance).

## Objectifs

1. **Analyse Exploratoire (EDA) :** Comprendre les variables socio-démographiques et financières qui influencent le défaut de paiement.
2. **Modélisation Prédictive :** Développer un modèle de classification robuste (optimisé sur le score AUC-ROC pour gérer le déséquilibre des classes).
3. **Explicabilité (SHAP) :** Interpréter les décisions du modèle pour comprendre le poids de chaque variable dans le score final.
4. **Déploiement :** Créer une interface interactive (Dashboard) permettant à un conseiller bancaire de simuler une demande de crédit en temps réel.

## Données

Les données proviennent de la compétition Kaggle **[Home Credit Default Risk](https://www.kaggle.com/c/home-credit-default-risk/data)**. 
*Note : Pour des raisons de taille et de confidentialité, les datasets bruts ne sont pas versionnés sur ce dépôt.*

## Stack Technique & Méthodologie

* **Langage :** Python
* **Manipulation & Analyse :** Pandas, NumPy
* **Data Visualisation :** Matplotlib, Seaborn, Plotly
* **Machine Learning :** Scikit-Learn, LightGBM / Random Forest
* **Interprétabilité :** SHAP (SHapley Additive exPlanations)
* **Web App & Déploiement :** Streamlit

## Structure du Projet

├── app/ # Code source du dashboard Streamlit
├── data/ # Données brutes et processées (ignorées par Git)
├── notebooks/ # Notebooks Jupyter (EDA et modélisation)
├── src/ # Scripts Python (nettoyage, feature engineering)
├── README.md # Description du projet
└── requirements.txt # Dépendances du projet
