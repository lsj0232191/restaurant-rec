class RestaurantReviewSystem:
    def __init__(self, restaurant_reviews):
        self.restaurant_reviews = restaurant_reviews
        self.user_data = {"like": {"4": {}, "5": {}}, "dislike": {"1": {}, "2": {}}}

    def display_restaurants(self):
        print("Available Restaurants:")
        for restaurant in self.restaurant_reviews.keys():
            print("-", restaurant)

    def get_user_choice(self):
        return input("wich restaurant would you like to rate?(이름 받아오기)").strip()

    def select_favorite_restaurant(self):
        self.display_restaurants()
        user_choice = self.get_user_choice()

        if user_choice in self.restaurant_reviews:
            preference = input("Do you like or dislike this restaurant? (like/dislike): ").lower()
            if preference == "like":
                self.update_user_data(user_choice, "like")
            elif preference == "dislike":
                self.update_user_data(user_choice, "dislike")
            else:
                print("like/dislike 하나만 골라 확마")
        else:
            print("이름좀 똑바로 쓰라")

    def update_user_data(self, restaurant, preference):
        keywords_count = self.restaurant_reviews[restaurant]

        if preference == "like":
            categories_to_save = ["4", "5"]
        elif preference == "dislike":
            categories_to_save = ["1", "2"]
        else:
            print("Invalid preference. Please choose 'like' or 'dislike'.")
            return

        for category in categories_to_save:
            sorted_keywords = sorted(keywords_count[category].items(), key=lambda x: x[1], reverse=True)
            top_keywords = {keyword: count for keyword, count in sorted_keywords[:5]}
            
            if restaurant not in self.user_data[preference][category]:
                self.user_data[preference][category][restaurant] = top_keywords
            else:
                existing_keywords = self.user_data[preference][category][restaurant]
                for keyword, count in top_keywords.items():
                    existing_count = existing_keywords.get(keyword, 0)
                    existing_keywords[keyword] = existing_count + count

    def display_user_data(self):
        print("\ncurrent keyword list")
        for preference, categories in self.user_data.items():
            print(f"\n{preference.capitalize()} Restaurants:")
            for category, data in categories.items():
                print(f"Category {category} Keywords:")
                for restaurant, keywords in data.items():
                    print(f"{restaurant}: {keywords}")

    def matching_algorithm(self):
        restaurant_scores = {}

        for restaurant, categories in self.restaurant_reviews.items():
            score = 0

            for preference, user_categories in self.user_data.items():
                for category, user_data_keywords in user_categories.items():
                    for keyword, count in user_data_keywords.get(restaurant, {}).items():
                        score += count * categories[category].get(keyword, 0)

            restaurant_scores[restaurant] = score

        sorted_scores = sorted(restaurant_scores.items(), key=lambda x: x[1], reverse=True)
        return sorted_scores

# Example usage
if __name__ == "__main__":
    restaurant_reviews = {
        # TODO add examples
    }

    review_system = RestaurantReviewSystem(restaurant_reviews)

    while True:
        review_system.select_favorite_restaurant()
        review_system.display_user_data()

        another_choice = input("Do you want to rate another restaurant? (yes/no): ")
        if another_choice.lower() != "yes":
            break

    matching_results = review_system.matching_algorithm()
    print("\nMatching Results:")
    for restaurant, score in matching_results:
        print(f"{restaurant}: {score}")
