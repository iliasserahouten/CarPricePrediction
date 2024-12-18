import streamlit as st
import pandas as pd
import joblib
import base64


# Charger le modèle sauvegardé
model = joblib.load('best_model_pipeline.pkl')

def add_bg_from_local(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Mapper les colonnes catégoriques
def preprocess_input(data):
    mappings = {
        'Emission_class': {'Euro 6': 1, 'Euro 6d-TEMP': 2, 'Euro 6d': 3, 'Euro 5': 0},
        'Doors': {'4/5 doors': 1, '2/3 doors': 0},
        'Drive_type': {'4x2': 0, '4x4': 1},
        'Fuel': {'Diesel': 0, 'Petrol': 1, 'Electric': 3, 'Hybrid': 2},
        'Transmission': {'Automatic': 0, 'Manual': 1}
    }

    for column, mapping in mappings.items():
        if column in data:
            data[column] = data[column].map(mapping)
    
    return data

# Ajouter l'image d'arrière-plan
add_bg_from_local("close-up-hand-holding-car-keys.jpg")

# Interface utilisateur avec Streamlit
st.title("Prédiction du Prix de Voitures")

# Entrée des caractéristiques
st.header("Entrez les caractéristiques de la voiture :")

Mileage = st.number_input("Kilométrage (Mileage)", min_value=0, step=1000)
Power = st.number_input("Puissance (Power en chevaux)", min_value=0, step=10)
Transmission = st.selectbox("Transmission", options=['Automatic', 'Manual'])
Fuel = st.selectbox("Type de carburant", options=['Diesel', 'Petrol', 'Electric', 'Hybrid'])
Drive_type = st.selectbox("Type de transmission", options=['4x2', '4x4'])
Doors = st.selectbox("Nombre de portes", options=['4/5 doors', '2/3 doors'])
Seats = st.selectbox("Nombre de sièges", options=[2, 3, 4, 5, 6, 7])
CO2_emissions = st.number_input("Émissions de CO2 (en g/km)", min_value=0, step=1)
Engine_capacity = st.number_input("Cylindrée (Engine capacity en litres)", min_value=0.0, step=0.1)
Emission_class = st.selectbox("Classe d'émission", options=['Euro 6', 'Euro 6d-TEMP', 'Euro 6d', 'Euro 5'])
Year = st.number_input("Année de fabrication", min_value=2011, max_value=2024, step=1)
Make = st.selectbox("Marque de la voiture (Make)", value="Audi",options=['Abarth', 'Alfa Romeo','Aston Martin', 'Audi', 'BMW', 'Bentley','Chevrolet', 'Citroën', 'Cupra', 'DR Automobiles', 'DS Automobiles','Dacia','Ferrari', 'Fiat', 'Ford', 'Honda', 'Hyundai', 'Jaguar','Jeep','Kia', 'Lamborghini', 'Lancia', 'Land Rover', 'Lexus','Lynk & Co', 'MG','MINI', 'Maserati', 'Mazda', 'Mercedes-Benz','Mitsubishi', 'Nissan', 'Opel', 'Peugeot', 'Polestar', 'Porsche','Renault', 'Seat', 'Smart', 'SsangYong', 'Subaru', 'Suzuki','Tesla', 'Toyota', 'Volkswagen', 'Volvo', 'Škoda'])
Body = st.selectbox("Type de carrosserie (Body)", value="SUV / offroad",options=['SUV / offroad', 'Hatchback', 'Station Wagon', 'Sedans / saloons','MPV/VAN', 'MPV', 'Pick-up', 'Cargo VAN', 'Coupe'])
Interior_material = st.selectbox("Matériau de l'intérieur", value="Full leather interior",options=['Part leather interior','Cloth interior', 'Full leather interior','Other interior material', 'Velour interior'])

# Bouton pour effectuer la prédiction
if st.button("Prédire le Prix"):
    # Préparer les données
    input_data = pd.DataFrame([{
        'Mileage': Mileage,
        'Power': Power,
        'Transmission': Transmission,
        'Fuel': Fuel,
        'Drive_type': Drive_type,
        'Doors': Doors,
        'Seats': Seats,
        'CO2_emissions': CO2_emissions,
        'Engine_capacity': Engine_capacity,
        'Emission_class': Emission_class,
        'Year': Year,
        'Make': Make,
        'Body': Body,
        'Interior_material': Interior_material
    }])

    # Prétraitement des données
    input_data = preprocess_input(input_data)

    # Effectuer la prédiction
    prediction = model.predict(input_data)

    # Afficher le résultat
    st.success(f"Prix prédit : {prediction[0]:,.2f} €")
