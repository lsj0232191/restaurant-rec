import json
from collections import defaultdict
import string
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def calculate_word_frequencies(reviews):
    word_freq_by_stars = {1: defaultdict(int), 2: defaultdict(int), 3: defaultdict(int), 4: defaultdict(int), 5: defaultdict(int)}
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    # # Define redundant words to ignore
    # redundant_words = {'awesome', 'good', 'great', 'poor', 'terrific', 'fantastic'}

    for review in reviews:
        text = review.get('text', '').lower()
        tokens = word_tokenize(text)
        pos_tags = pos_tag(tokens)

        tokens = [token for token, pos in pos_tags if token.isalpha() and token not in string.punctuation and token not in stop_words and pos != 'RB']  # Filter out adverbs
        filtered_tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]

        word_freq = defaultdict(int)
        for token in filtered_tokens:
            word_freq[token] += 1

        star_rating = review.get('stars')
        if star_rating:
            word_freq_by_stars[star_rating].update(word_freq)

    return word_freq_by_stars
    # for review in reviews:
    #     text = review.get('text', '').lower()
    #     tokens = word_tokenize(text)

    #     # Remove punctuation and filter out stop words
    #     tokens = [token for token in tokens if token.isalpha() and token not in string.punctuation and token not in stop_words]
    #     filtered_tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]

    #     # Count word frequencies by restaurant
    #     word_freq = defaultdict(int)
    #     for token in filtered_tokens:
    #         word_freq[token] += 1

    #     star_rating = review.get('stars')
    #     if star_rating:
    #         word_freq_by_stars[star_rating].update(word_freq)

    # return word_freq_by_stars


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

        # Sort the word frequencies by count within each star rating
        sorted_word_freq_by_stars = {star: sorted(word_freq.items(), key=lambda x: x[1], reverse=True) for star, word_freq in word_frequencies.items()}

        # Update the restaurant's data with sorted word frequencies by stars
        restaurant['word_frequencies'] = sorted_word_freq_by_stars
        filtered_reviews.append(restaurant)    


    # Save the result to filtered_reviews.json
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(filtered_reviews, f, indent=2)

# Example usage
create_filtered_reviews('filtered_restaurants.json', 'yelp_academic_dataset_review.json', 'filtered_reviews.json')
