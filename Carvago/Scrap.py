from bs4 import BeautifulSoup
import warnings
import requests
import re
import time
import pandas as pd
start_time = time.time()
#la liste des attributs :
Mileage = []
First_registration = []
Power = []
Transmission = []
Fuel = []
Drive_type = []
Location = []
Vehicle_ID = []
Make = []
Body_color = []
Type_of_finish = []
Interior_color = []
Interior_material = []
Body = []
Doors = []
Seats = []
Consumption  = []
CO2_emissions = []
Engine_capacity = []
Emission_class = []
Speeds = []
price = []
price_without_vat = []

def connect_page(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup

def get_Links_from_page():
  links = []
  # loop over the pages
  for k in range(0, 1501):
    soup = connect_page(f"https://carvago.com/cars?page={k}")
    # Find all divs with the specific data-testid attribute
    for div in soup.find_all('div', {'data-testid': 'feature.car.card'}):
        # Find the 'a' tags within those divs and get the href attributes
        for link in div.find_all('a', href=True):
            links.append(link['href'])
  return links

def get_data_from_link(links):
    for link in links:
      soup = connect_page(f"https://carvago.com{link}")
      #Extraire les données pour chaque attribut:
      #Milelage
      mileage_element = soup.find('p', text='Mileage')
      if mileage_element:
          mileage_value = mileage_element.find_next('p').text.strip()  # Aller à l'élément <p> suivant contenant la valeur
          mileage_value = mileage_value.replace("\u00a0", "")  # Retirer les espaces insécables pour obtenir un nombre pur
          Mileage.append(mileage_value)
      else:
          Mileage.append('NaN')
      #First_Rigestration
      first_registration_element = soup.find('p', text='First registration')
      if first_registration_element:
          first_registration_value = first_registration_element.find_next('p').text.strip()
          First_registration.append(first_registration_value)
      else:
          First_registration.append('NaN')     
      #Power
      power_element = soup.find('p', text='Power')
      if power_element:
          power_value = power_element.find_next('p').text.strip()
          Power.append(power_value)
      else:
          Power.append('NaN')
      #Transmission
      transmission_element = soup.find('p', text='Transmission')
      if transmission_element:
          transmission_value = transmission_element.find_next('p').text.strip()
          Transmission.append(transmission_value)
      else:
          Transmission.append('NaN')
      #Fuel
      fuel_element = soup.find('p', text='Fuel')
      if fuel_element:
          fuel_value = fuel_element.find_next('p').text.strip()
          Fuel.append(fuel_value)
      else:
          Fuel.append('NaN')

      # Drive_type
      drive_type_element = soup.find('p', text='Drive type')
      if drive_type_element:
          drive_type_value = drive_type_element.find_next('p').text.strip()
          Drive_type.append(drive_type_value)
      else:
          Drive_type.append('NaN')

      # Location
      location_element = soup.find('p', text='Location')
      if location_element:
          location_value = location_element.find_next('p').text.strip()
          Location.append(location_value)
      else:
          Location.append('NaN')
      # Vehicle_ID
      vehicle_id_element = soup.find('p', text='Vehicle ID')
      if vehicle_id_element:
          vehicle_id_value = vehicle_id_element.find_next('p').text.strip()
          Vehicle_ID.append(vehicle_id_value)
      else:
          Vehicle_ID.append('NaN')
      # Make
      make_element = soup.find('p', text='Make')
      if make_element:
          make_value = make_element.find_next('p').text.strip()
          Make.append(make_value)
      else:
          Make.append('NaN')
      # Body_color
      body_color_element = soup.find('p', text='Body color')
      if body_color_element:
          body_color_value = body_color_element.find_next('p').text.strip()
          Body_color.append(body_color_value)
      else:
          Body_color.append('NaN')

      # Type_of_finish
      type_of_finish_element = soup.find('p', text='Type of finish')
      if type_of_finish_element:
          type_of_finish_value = type_of_finish_element.find_next('p').text.strip()
          
          Type_of_finish.append(type_of_finish_value)
      else:
          Type_of_finish.append('NaN')
      # Interior_color
      interior_color_element = soup.find('p', text='Interior color')
      if interior_color_element:
          interior_color_value = interior_color_element.find_next('p').text.strip()
          
          Interior_color.append(interior_color_value)
      else:
          Interior_color.append('NaN')
      # Interior_material
      interior_material_element = soup.find('p', text='Interior material')
      if interior_material_element:
          interior_material_value = interior_material_element.find_next('p').text.strip()
          
          Interior_material.append(interior_material_value)
      else:
          Interior_material.append('NaN')
      # Body
      body_element = soup.find('p', text='Body')
      if body_element:
          body_value = body_element.find_next('p').text.strip()
          
          Body.append(body_value)
      else:
          Body.append('NaN')
      # Doors
      doors_element = soup.find('p', text='Doors')
      if doors_element:
          doors_value = doors_element.find_next('p').text.strip()
          
          Doors.append(doors_value)
      else:
          Doors.append('NaN')
      # Seats
      seats_element = soup.find('p', text='Seats')
      if seats_element:
          seats_value = seats_element.find_next('p').text.strip()
          
          Seats.append(seats_value)
      else:
          Seats.append('NaN')

      # Consumption
      consumption_element = soup.find('p', text='Consumption')
      if consumption_element:
          consumption_value = consumption_element.find_next('p').text.strip()
          
          Consumption.append(consumption_value)
      else:
          Consumption.append('NaN')
      # CO2_emissions
      co2_emissions_element = soup.find('p', text='CO2 emissions')
      if co2_emissions_element:
          co2_emissions_value = co2_emissions_element.find_next('p').text.strip()
          
          CO2_emissions.append(co2_emissions_value)
      else:
          CO2_emissions.append('NaN')
      # Engine_capacity
      engine_capacity_element = soup.find('p', text='Engine capacity')
      if engine_capacity_element:
          engine_capacity_value = engine_capacity_element.find_next('p').text.strip()
          
          Engine_capacity.append(engine_capacity_value)
      else:
          Engine_capacity.append('NaN')

      # Emission_class
      emission_class_element = soup.find('p', text='Emission class')
      if emission_class_element:
          emission_class_value = emission_class_element.find_next('p').text.strip()
          
          Emission_class.append(emission_class_value)
      else:
          Emission_class.append('NaN')

      # Speeds
      speeds_element = soup.find('p', text='Speeds')
      if speeds_element:
          speeds_value = speeds_element.find_next('p').text.strip()
          
          Speeds.append(speeds_value)
      else:
          Speeds.append('NaN')
      # price
      # Extraction du prix
      price_element = soup.find('dt', class_='chakra-text css-105xw8a', text='Car price')
      if price_element:
          price_value = price_element.find_next('dd', class_='chakra-text css-105xw8a').text.strip()
          price.append(price_value)
      else:
          price.append('NaN')

      # Extraction du prix sans TVA
      price_without_vat_element = soup.find('dt', class_='chakra-text css-1potdld', text='Price without VAT')
      if price_without_vat_element:
          price_without_vat_value = price_without_vat_element.find_next('dd', class_='chakra-text css-1potdld').text.strip()
          price_without_vat.append(price_without_vat_value)
      else:
          price_without_vat.append('NaN')

     

car_links = get_Links_from_page()

get_data_from_link(car_links)

print("--- %s seconds ---" % (time.time() - start_time))
df = pd.DataFrame({'Mileage': Mileage, 'First_registration': First_registration, 'Power': Power, 'Transmission': Transmission, 'Fuel': Fuel, 'Drive_type': Drive_type, 'Location': Location, 'Vehicle_ID': Vehicle_ID, 'Make': Make, 'Body_color': Body_color, 'Type_of_finish': Type_of_finish, 'Interior_color': Interior_color, 'Interior_material': Interior_material, 'Body': Body, 'Doors': Doors, 'Seats': Seats, 'Consumption': Consumption, 'CO2_emissions': CO2_emissions, 'Engine_capacity': Engine_capacity, 'Emission_class': Emission_class, 'Speeds': Speeds, 'price': price, 'price_without_vat': price_without_vat})
df.to_csv('Carvago.csv', index=False,mode='a')
df.head()









