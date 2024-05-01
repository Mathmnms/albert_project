import streamlit as st

# Titre de l'application
st.title('PredictVote')

# Ajout d'un sélecteur de diapositives
slide_value = st.slider("Nombre de cotiseurs: ", min_value=0, max_value=100, value=50)

# Affichage de la valeur sélectionnée
st.write(f"La valeur sélectionnée est : {slide_value}")

# Si vous souhaitez ajouter des diapositives avec des images ou du contenu spécifique, ajoutez-le ici
