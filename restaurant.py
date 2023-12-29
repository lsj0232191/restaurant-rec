import json

class Business:
    def __init__(self, name, business_id, latitude, longitude, categories):
        self.name = name
        self.business_id = business_id
        self.latitude = latitude
        self.longitude = longitude
        self.categories = categories

    def to_dict(self):
        return {
            'name': self.name,
            'business_id': self.business_id,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'categories': self.categories
        }

def extract_businesses_by_coord(file_name, target_latitude, target_longitude, radius_km=150):
    try:
        businesses = []

        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                business_data = json.loads(line)
                if 'latitude' in business_data and 'longitude' in business_data and 'categories' in business_data:
                    lat = business_data['latitude']
                    lon = business_data['longitude']
                    distance = ((lat - target_latitude) ** 2 + (lon - target_longitude) ** 2) ** 0.5
                    # Assuming 1 degree of latitude and longitude is approximately 111 kilometers
                    if distance * 111 <= radius_km and business_data['categories'] is not None and 'Restaurants' in business_data['categories']:
                        business = Business(business_data['name'], business_data['business_id'], lat, lon, business_data['categories'])
                        businesses.append(business.to_dict())

        return businesses

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return []


# Example coordinates (Santa Barbara, CA)
target_lat = 39.2903
target_lon = -76.61219

file_name = 'yelp_academic_dataset_business.json'  # Replace with your JSON file name or path
output_file = 'filtered_restaurants.json'  # Output JSON file name

filtered_restaurants = extract_businesses_by_coord(file_name, target_lat, target_lon)

# Writing the extracted restaurants into a new JSON file
if filtered_restaurants:
    with open(output_file, 'w', encoding='utf-8') as output:
        json.dump(filtered_restaurants, output, indent=4)
        print(f"Filtered restaurants written to '{output_file}'")
else:
    print("No restaurants found within the specified criteria.")
