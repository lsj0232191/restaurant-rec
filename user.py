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

    def combine_keyword(self):
        for user in self.users:
            user_data = user.user_keyword
            
            for preference in ("like", "dislike"):
                for rating_key in ("4", "5", "1", "2"): 
                    user_data_keywords = user_data.get(preference, {}).get(rating_key, {})
                    for restaurant, keywords in user_data_keywords.items():
                        if restaurant not in self.group_data[preference][rating_key]:
                            self.group_data[preference][rating_key][restaurant] = keywords
                        else:
                            self.group_data[preference][rating_key][restaurant].update(keywords)

            
