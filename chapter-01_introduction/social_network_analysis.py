"""
Chapter 1 - Introduction
Social Network Data Modeling and Analysis
"""

from collections import Counter, defaultdict

# -----------------------
# Users Data
# -----------------------

users = [
    {"id": 0, "name": "Iron Man"},
    {"id": 1, "name": "Captain America"},
    {"id": 2, "name": "Thor"},
    {"id": 3, "name": "Hulk"},
    {"id": 4, "name": "Black Widow"},
    {"id": 5, "name": "Spider-Man"},
    {"id": 6, "name": "Doctor Strange"},
    {"id": 7, "name": "Black Panther"},
    {"id": 8, "name": "Scarlet Witch"},
    {"id": 9, "name": "Loki"},
]

friendship_pairs = [
    (0, 1), (0, 2), (1, 3), (1, 4),
    (2, 5), (3, 6), (4, 7), (5, 8),
    (6, 9), (7, 8), (8, 9)
]

# -----------------------
# Build Friendship Graph
# -----------------------

friendships = {user["id"]: [] for user in users}

for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)

# -----------------------
# Network Metrics
# -----------------------

def number_of_friends(user):
    return len(friendships[user["id"]])

total_connections = sum(number_of_friends(user) for user in users)
avg_connections = total_connections / len(users)

# -----------------------
# Friends of Friends
# -----------------------

def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]
        for foaf_id in friendships[friend_id]
        if foaf_id != user_id
        and foaf_id not in friendships[user_id]
    )

# -----------------------
# Interests Data
# -----------------------

interests = [
    (0, "technology"), (0, "ai"),
    (1, "leadership"), (1, "strategy"),
    (2, "space"), (2, "mythology"),
    (3, "strength training"), (3, "science"),
    (4, "espionage"), (4, "martial arts"),
    (5, "photography"), (5, "web design"),
    (6, "magic"), (6, "time travel"),
    (7, "wakanda technology"), (7, "politics"),
    (8, "telekinesis"), (8, "energy manipulation"),
    (9, "mischief"), (9, "illusions"),
]

user_ids_by_interest = defaultdict(list)
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)
    interests_by_user_id[user_id].append(interest)

def most_common_interests_with(user):
    return Counter(
        other_user_id
        for interest in interests_by_user_id[user["id"]]
        for other_user_id in user_ids_by_interest[interest]
        if other_user_id != user["id"]
    )

# -----------------------
# Word Frequency Analysis
# -----------------------

words_and_counts = Counter(
    word
    for _, interest in interests
    for word in interest.lower().split()
)

if __name__ == "__main__":
    print("Average Connections:", avg_connections)
    print("Friends of Friends (Hulk):", friends_of_friends(users[3]))
    print("Common Interests with Iron Man:", most_common_interests_with(users[0]))
    print("Most Common Interest Words:", words_and_counts.most_common(5))
