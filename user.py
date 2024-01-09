import json

class User:
    def __init__(self, name, user_id, liked_rest, user_keyword, location, friends):
        self.name = name
        self.user_id = user_id
        self.liked_rest = liked_rest
        self.user_keyword = user_keyword
        self.location = location
        self.friends = friends

    
    # def join_group(group_id):
    #     if group_id

    
class Group:
    def __init__(self, users, group_id, avg_rest, rec_rest):
        self.users = users
        self.group_id = group_id
        self.group_data = {"like": {"4": {}, "5": {}}, "dislike": {"1": {}, "2": {}}}
        self.avg_rest = avg_rest
        self.rec_rest = rec_rest

    def combine_keyword():
        for user in self.users:
            for preference, categories in user.user_keyword.items():
                if restaurant not in self.user_data[preference][category]:
                    self.group_data[preference][category][restaurant] = top_keywords
                else:
                    existing_keywords = self.user_data[preference][category][restaurant]
                    for keyword, count in top_keywords.items():
                        existing_count = existing_keywords.get(keyword, 0)
                        existing_keywords[keyword] = existing_count + count
            
            for category, data in categories.items():
                print(f"Category {category} Keywords:")
                for restaurant, keywords in data.items():
                    print(f"{restaurant}: {keywords}")
            
