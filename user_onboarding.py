class RestaurantReviewSystem:
    def __init__(self, restaurant_reviews):
        self.restaurant_reviews = restaurant_reviews
        self.user_data = {"positive": {}, "negative": {}}

    def display_restaurants(self):
        print("Available Restaurants:")
        for restaurant in self.restaurant_reviews.keys():
            print("-", restaurant)

    def get_user_choice(self):
        return input("Enter the name of a restaurant you like or dislike: ").strip()

    def select_favorite_restaurant(self):
        self.display_restaurants()
        user_choice = self.get_user_choice()

        if user_choice in self.restaurant_reviews:
            preference = input("Do you like or dislike this restaurant? (like/dislike): ").lower()
            if preference == "like":
                self.update_user_data(user_choice, "positive")
            elif preference == "dislike":
                self.update_user_data(user_choice, "negative")
            else:
                print("Invalid preference. Please choose 'like' or 'dislike'.")
        else:
            print("Invalid restaurant name. Please try again.")

    def update_user_data(self, restaurant, preference):
        keywords_count = self.restaurant_reviews[restaurant][preference]
        sorted_keywords = sorted(keywords_count.items(), key=lambda x: x[1], reverse=True)
        top_keywords = {keyword: count for keyword, count in sorted_keywords[:5]}
        if restaurant not in self.user_data[preference]:
            self.user_data[preference][restaurant] = top_keywords
        else:
            existing_keywords = self.user_data[preference][restaurant]
            for keyword, count in top_keywords.items():
                existing_keywords[keyword] = existing_keywords.get(keyword, 0) + count

    def display_user_data(self):
        print("\nYour Data:")
        for preference, data in self.user_data.items():
            print(f"{preference.capitalize()} Keywords:")
            for restaurant, keywords in data.items():
                print(f"{restaurant}: {keywords}")

# Example usage
if __name__ == "__main__":
    restaurant_reviews = {
        "Restaurant1": {"positive": {"tasty": 10, "service": 8, "ambiance": 6, "price": 4, "variety": 7},
                        "negative": {"slow-service": 3, "overpriced": 5, "bland": 2, "dirty": 1, "limited-menu": 4}},
        "Restaurant2": {"positive": {"service": 9, "tasty": 7, "price": 5, "ambiance": 6, "cleanliness": 8},
                        "negative": {"poor-service": 2, "tasteless": 4, "expensive": 5, "unpleasant": 3, "messy": 1}},
        "Restaurant3": {"positive": {"ambiance": 9, "variety": 8, "tasty": 7, "service": 6, "price": 5},
                        "negative": {"crowded": 3, "limited-options": 4, "bad-service": 2, "expensive": 5, "unappealing": 1}}
    }

    review_system = RestaurantReviewSystem(restaurant_reviews)

    while True:
        review_system.select_favorite_restaurant()
        review_system.display_user_data()

        another_choice = input("Do you want to add another favorite restaurant? (yes/no): ")
        if another_choice.lower() != "yes":
            break
