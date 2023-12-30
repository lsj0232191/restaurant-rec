import json

def create_filtered_reviews(filtered_restaurants_file, reviews_file, output_file):
    # Load filtered restaurants from JSON file
    with open(filtered_restaurants_file, 'r', encoding='utf-8') as f:
        filtered_restaurants = json.load(f)

    # Load reviews from JSON file line by line
    reviews = []
    with open(reviews_file, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                review = json.loads(line)
                reviews.append(review)
            except json.JSONDecodeError:
                print(f"Failed to decode JSON from line: {line}")

    # Create a dictionary to store reviews by business_id
    reviews_by_business = {restaurant['business_id']: [] for restaurant in filtered_restaurants}

    # Populate the reviews_by_business dictionary
    for review in reviews:
        business_id = review.get('business_id')
        if business_id in reviews_by_business:
            reviews_by_business[business_id].append(review)

    # Create a new list of restaurants with their corresponding reviews
    filtered_reviews = []
    for restaurant in filtered_restaurants:
        business_id = restaurant.get('business_id')
        reviews_for_restaurant = reviews_by_business.get(business_id, [])
        restaurant['reviews'] = reviews_for_restaurant
        filtered_reviews.append(restaurant)

    # Save the result to filtered_reviews.json
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(filtered_reviews, f, indent=2)

# Example usage
create_filtered_reviews('filtered_restaurants.json', 'data/yelp_dataset/yelp_academic_dataset_review.json', 'filtered_reviews.json')
