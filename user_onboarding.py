class RestaurantReviewSystem:
    def __init__(self, restaurant_reviews):
        self.restaurant_reviews = restaurant_reviews
        self.user_data = {}

    def display_restaurants(self):
        print("Available Restaurants:")
        for restaurant in self.restaurant_reviews.keys():
            print("-", restaurant)

    def select_favorite_restaurant(self):
        self.display_restaurants()
        user_choice = input("Enter the name of your favorite restaurant: ")

        if user_choice in self.restaurant_reviews:
            top_keywords = self.get_top_keywords(user_choice)
            self.add_to_user_data(user_choice, top_keywords)
            print(f"Added top 5 keywords for {user_choice} to your data.")
        else:
            print("Invalid restaurant name. Please try again.")

    def get_top_keywords(self, restaurant):
        keywords_count = self.restaurant_reviews[restaurant]
        sorted_keywords = sorted(keywords_count.items(), key=lambda x: x[1], reverse=True)
        top_keywords = [keyword for keyword, count in sorted_keywords[:5]]
        return top_keywords

    def add_to_user_data(self, restaurant, top_keywords):
        if restaurant not in self.user_data:
            self.user_data[restaurant] = top_keywords
        else:
            self.user_data[restaurant].extend(top_keywords[:5])

    def display_user_data(self):
        print("\nYour Data:")
        for user, data in self.user_data.items():
            print(f"{user}: {data}")

# Example usage
if __name__ == "__main__":
    # TODO samples
    restaurant_reviews = {
        "Restaurant1": {"tasty": 10, "service": 8, "ambiance": 6, "price": 4, "variety": 7},
        "Restaurant2": {"service": 9, "tasty": 7, "price": 5, "ambiance": 6, "cleanliness": 8},
        "Restaurant3": {"ambiance": 9, "variety": 8, "tasty": 7, "service": 6, "price": 5}
    }

    review_system = RestaurantReviewSystem(restaurant_reviews)

    while True:
        review_system.select_favorite_restaurant()
        review_system.display_user_data()

        another_choice = input("Do you want to add another favorite restaurant? (yes/no): ")
        if another_choice.lower() != "yes":
            break
