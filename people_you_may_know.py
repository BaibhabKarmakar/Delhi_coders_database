# DESCRIPTION : Addig people you may know feature : 

import json

def load_data(filename):
    with open(filename , "r") as f:
        data = json.load(f)
    return data


def find_people_you_may_know(user_id, data):
    user_friends = {}
    for user in data["users"]:
        user_friends[user["id"]] = set(user["friends"])
    
    if user_id not in user_friends:
        return []
    
    direct_friends = user_friends[user_id]
    suggestions = {}
    
    for friend in direct_friends:
        # For all friends of friend
        for mutual in user_friends[friend]:
            # If mutual id is not the same user and not already a direct friend of user
            if mutual != user_id and mutual not in direct_friends:
                # Count mutual friends
                suggestions[mutual] = suggestions.get(mutual, 0) + 1
    
    sorted_suggestions = sorted(suggestions.items(), key=lambda x: x[1], reverse=True)
    return [user_id for user_id, _ in sorted_suggestions]

cleaned_data = load_data("raw_data.json")
user_id = int(input("Can you please give the user id ? :"))
recommendations = find_people_you_may_know(user_id, cleaned_data)
print(f"People You May Know for User {user_id}: {recommendations}")