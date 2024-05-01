import streamlit as st
from joblib import load

# Charger le modèle à partir du fichier spécifié
model = load(r"data\best_logistic_regression_model.joblib")

def inverse_category(num):
    if num == 0:
        return 'LE PEN, ZEMMOUR'
    elif num == 1:
        return 'MACRON'
    elif num == 2:
        return 'HIDALGO, HAMON'
    elif num == 3:
        return 'MÉLENCHON, ROUSSEL'
    elif num == 4:
        return 'FILLON, PÉCRESSE'
    else:
        return 'Catégorie inconnue'

st.title("PredictVote : L'outil de référence en prédiction de vote")

# Créer un formulaire pour entrer les valeurs des caractéristiques
with st.form(key='input_form'):
    # Entrées pour chaque caractéristique attendue par le modèle
    feature1 = st.number_input('Entrez la valeur pour la caractéristique 1', format="%.2f")
    feature2 = st.number_input('Entrez la valeur pour la caractéristique 2', format="%.2f")
    feature3 = st.number_input('Entrez la valeur pour la caractéristique 3', format="%.2f")
    feature4 = st.number_input('Entrez la valeur pour la caractéristique 4', format="%.2f")
    feature5 = st.number_input('Entrez la valeur pour la caractéristique 5', format="%.2f")
    feature6 = st.number_input('Entrez la valeur pour la caractéristique 6', format="%.2f")
    feature7 = st.number_input('Entrez la valeur pour la caractéristique 7', format="%.2f")
    feature8 = st.number_input('Entrez la valeur pour la caractéristique 8', format="%.2f")
    feature9 = st.number_input('Entrez la valeur pour la caractéristique 9', format="%.2f")
    feature10 = st.number_input('Entrez la valeur pour la caractéristique 10', format="%.2f")
    feature11 = st.number_input('Entrez la valeur pour la caractéristique 11', format="%.2f")
    feature12 = st.number_input('Entrez la valeur pour la caractéristique 12', format="%.2f")
    feature13 = st.number_input('Entrez la valeur pour la caractéristique 13', format="%.2f")
    feature14 = st.number_input('Entrez la valeur pour la caractéristique 14', format="%.2f")
    feature15 = st.number_input('Entrez la valeur pour la caractéristique 15', format="%.2f")
    feature16 = st.number_input('Entrez la valeur pour la caractéristique 16', format="%.2f")
    feature17 = st.number_input('Entrez la valeur pour la caractéristique 17', format="%.2f")
    feature18 = st.number_input('Entrez la valeur pour la caractéristique 18', format="%.2f")
    feature19 = st.number_input('Entrez la valeur pour la caractéristique 19', format="%.2f")

    submit_button = st.form_submit_button(label='Prédire')

if submit_button:
    # Rassembler toutes les valeurs des caractéristiques dans un tableau
    input_features = [feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, feature9, feature10, 
                      feature11, feature12, feature13, feature14, feature15, feature16, feature17, feature18, feature19]

    # Faire une prédiction avec le modèle
    prediction = model.predict([input_features])
    st.write(f'Prédiction: {inverse_category(prediction[0])}')
