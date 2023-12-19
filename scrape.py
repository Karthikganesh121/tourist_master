
import csv
import random
# List of Cities in Kerala
cities = [
    "Thiruvananthapuram (Trivandrum)",
    "Kochi (Cochin)",
    "Kozhikode (Calicut)",
    "Munnar",
    "Alappuzha (Alleppey)",
    "Wayanad",
    "Kumarakom",
    "Thekkady",
    "Kannur",
    "Thrissur"
]

# List of Hotel Chains
hotels = [
    "Taj Hotels",
    "The Leela",
    "The Lalit",
    "Radisson Blu",
    "Marriott International",
    "Ramada by Wyndham",
    "ITC Hotels",
    "Vivanta by Taj",
    "Hyatt Regency",
    "Holiday Inn",
    "Le Méridien",
    "The Gateway Hotel (by Taj)",
    "Novotel",
    "Crowne Plaza",
    "Hilton Hotels & Resorts"
]

amenities = ['Free WiFi', 'Swimming Pool', 'Spa', 'Gym', 'Restaurant', 'Parking']

# Function to generate random pricing
def generate_pricing():
    return round(random.uniform(1200, 5000), 2)

# Function to generate a random set of amenities
def generate_amenities():
    return ', '.join(random.sample(amenities, random.randint(2, len(amenities))))

# Generate dataset
data = []
for city in cities:
    for _ in range(15):  # Generate 5 hotels per city
        hotel_data = {
            'City': city,
            'Hotel Name': random.choice(hotels),
            'Price per Night (INR)': generate_pricing(),
            'Amenities': generate_amenities()
        }
        data.append(hotel_data)

# Write data to a CSV file
with open('kerala_tourist_accommodation_details.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

print("Dataset created successfully!")
