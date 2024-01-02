import json
from collections import defaultdict
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def calculate_word_frequencies(reviews):
    word_freq_by_restaurant = defaultdict(lambda: defaultdict(int))
    stop_words = set(stopwords.words('english'))

    for review in reviews:
        # print(f"Review: {review}")
        text = review.get('text', '').lower()
        # print(f"Review Text: {text}")
        tokens = word_tokenize(text)

        # Remove punctuation and filter out stop words
        tokens = [token for token in tokens if token.isalpha() and token not in string.punctuation]
        filtered_tokens = [token for token in tokens if token not in stop_words]

        # Count word frequencies by restaurant
        word_freq = defaultdict(int)
        for token in filtered_tokens:
            word_freq[token] += 1

        # print(f"Word Frequencies: {word_freq}")

        # Update the word frequency dictionary for the respective restaurant
        business_id = review.get('business_id')
        word_freq_by_restaurant[business_id].update(word_freq)

    return word_freq_by_restaurant


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
        
        word_frequencies = calculate_word_frequencies(reviews_for_restaurant)

        # print(f"Business ID: {business_id}, Word Frequencies: {word_frequencies}")

        # Flatten the word frequency dictionary to a list of dictionaries
        flattened_word_freq = [{'word': word, 'count': count} for word_dict in word_frequencies.values() for word, count in word_dict.items()]

        restaurant['word_frequencies'] = flattened_word_freq

        filtered_reviews.append(restaurant)    


    # Save the result to filtered_reviews.json
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(filtered_reviews, f, indent=2)

# Example usage
create_filtered_reviews('filtered_restaurants.json', 'yelp_academic_dataset_review.json', 'filtered_reviews.json')
