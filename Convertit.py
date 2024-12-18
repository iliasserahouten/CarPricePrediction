import pandas as pd

# Charger le DataFrame d'origine
df = pd.read_csv('dataFinal.csv')

# Colonnes encodées
make_columns = ['Abarth', 'Alfa Romeo', 'Aston Martin', 'Audi', 'BMW', 'Bentley', 'Chevrolet', 'Citroën', 'Cupra', 
                'DR Automobiles', 'DS Automobiles', 'Dacia', 'Ferrari', 'Fiat', 'Ford', 'Honda', 'Hyundai', 'Jaguar', 
                'Jeep', 'Kia', 'Lamborghini', 'Lancia', 'Land Rover', 'Lexus', 'Lynk & Co', 'MG', 'MINI', 'Maserati', 
                'Mazda', 'Mercedes-Benz', 'Mitsubishi', 'Nissan', 'Opel', 'Peugeot', 'Polestar', 'Porsche', 'Renault', 
                'Seat', 'Smart', 'SsangYong', 'Subaru', 'Suzuki', 'Tesla', 'Toyota', 'Volkswagen', 'Volvo', 'Škoda']

interior_columns = [
    'Interior_material_Cloth interior', 'Interior_material_Full leather interior',
    'Interior_material_Other interior material', 'Interior_material_Part leather interior',
    'Interior_material_Velour interior'
]

body_columns = [
    'Body_Cargo VAN', 'Body_Coupe', 'Body_Hatchback', 'Body_MPV', 'Body_MPV/VAN', 'Body_Pick-up', 
    'Body_SUV / offroad', 'Body_Sedans / saloons', 'Body_Station Wagon'
]

# 1. Récupérer les noms des colonnes encodées
df['Make'] = df[make_columns].idxmax(axis=1)
df['Interior_material'] = df[interior_columns].idxmax(axis=1).str.replace('Interior_material_', '')
df['Body'] = df[body_columns].idxmax(axis=1).str.replace('Body_', '')

# 2. Créer le nouveau DataFrame avec 15 colonnes
selected_columns = [
    'Mileage', 'Power', 'Transmission', 'Fuel', 'Drive_type', 'Doors', 'Seats', 
    'CO2_emissions', 'Engine_capacity', 'Emission_class', 'Year', 
    'Make', 'Body', 'Interior_material', 'price'
]

df_final = df[selected_columns]

# Sauvegarder ou afficher le DataFrame final
df_final.to_csv('Cars.csv', index=False)
print(df_final.head())
