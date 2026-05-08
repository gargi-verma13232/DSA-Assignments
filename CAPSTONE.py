# =========================================================
#                DATA STRUCTURES CAPSTONE
#           SOCIAL NETWORK EXPLORER (SNE)
# =========================================================

# Student Name : Gargi Verma
# Roll Number  : 2501010223
# Course       : B.Tech CSE
# Section      : A
# Subject      : Data Structures
# Course Code  : ETCCDS202

# =========================================================
# AIM
# =========================================================
# To implement a Social Network Explorer using
# Data Structures like Graphs, Hash Tables,
# BFS, DFS, Sorting and Lists.
# =========================================================


from collections import deque


# =========================================================
# SOCIAL NETWORK CLASS
# =========================================================

class SocialNetwork:

    def __init__(self):

        # USER PROFILES
        self.profiles = {}

        # GRAPH (ADJACENCY LIST)
        self.network = {}

    # =====================================================
    # ADD USER
    # =====================================================

    def add_user(self, username, age, interests):

        if username in self.profiles:
            print("User already exists!")
            return

        self.profiles[username] = {
            "age": age,
            "interests": interests
        }

        self.network[username] = []

        print(f"{username} added successfully!")

    # =====================================================
    # UPDATE PROFILE
    # =====================================================

    def update_profile(self, username, age=None, interests=None):

        if username not in self.profiles:
            print("User not found!")
            return

        if age:
            self.profiles[username]["age"] = age

        if interests:
            self.profiles[username]["interests"] = interests

        print(f"{username}'s profile updated!")

    # =====================================================
    # SHOW PROFILE
    # =====================================================

    def show_profile(self, username):

        if username not in self.profiles:
            print("User not found!")
            return

        print("\n===== PROFILE =====")

        print("Username :", username)
        print("Age      :", self.profiles[username]["age"])
        print("Interests:", ", ".join(self.profiles[username]["interests"]))

    # =====================================================
    # ADD FRIEND
    # =====================================================

    def add_friend(self, user1, user2):

        if user1 not in self.network or user2 not in self.network:
            print("User not found!")
            return

        if user2 not in self.network[user1]:
            self.network[user1].append(user2)

        if user1 not in self.network[user2]:
            self.network[user2].append(user1)

        print(f"{user1} and {user2} are now friends!")

    # =====================================================
    # REMOVE FRIEND
    # =====================================================

    def remove_friend(self, user1, user2):

        if user2 in self.network[user1]:
            self.network[user1].remove(user2)

        if user1 in self.network[user2]:
            self.network[user2].remove(user1)

        print(f"Friendship removed between {user1} and {user2}")

    # =====================================================
    # SHOW FRIENDS
    # =====================================================

    def show_friends(self, username):

        if username not in self.network:
            print("User not found!")
            return

        print(f"\nFriends of {username}:")

        for friend in self.network[username]:
            print(friend)

    # =====================================================
    # BFS SHORTEST PATH
    # =====================================================

    def bfs_shortest_path(self, start, goal):

        if start not in self.network or goal not in self.network:
            print("User not found!")
            return

        queue = deque([[start]])

        visited = set()

        while queue:

            path = queue.popleft()

            node = path[-1]

            if node == goal:

                print("\nShortest Path:")
                print(" -> ".join(path))

                return

            if node not in visited:

                visited.add(node)

                for neighbor in self.network[node]:

                    new_path = list(path)

                    new_path.append(neighbor)

                    queue.append(new_path)

        print("No path found!")

    # =====================================================
    # DFS EXPLORATION
    # =====================================================

    def dfs_explore(self, start, depth):

        visited = set()

        print(f"\nDFS Exploration from {start} up to depth {depth}:")

        self._dfs_helper(start, visited, depth)

    def _dfs_helper(self, node, visited, depth):

        if depth < 0 or node in visited:
            return

        print(node)

        visited.add(node)

        for neighbor in self.network[node]:
            self._dfs_helper(neighbor, visited, depth - 1)

    # =====================================================
    # FRIEND RECOMMENDATION SYSTEM
    # =====================================================

    def recommend_friends(self, username):

        if username not in self.network:
            print("User not found!")
            return

        recommendations = []

        user_interests = set(self.profiles[username]["interests"])

        for other_user in self.profiles:

            if other_user == username:
                continue

            if other_user in self.network[username]:
                continue

            other_interests = set(self.profiles[other_user]["interests"])

            common_interests = len(user_interests & other_interests)

            mutual_friends = len(
                set(self.network[username]) &
                set(self.network[other_user])
            )

            score = common_interests + mutual_friends

            recommendations.append((other_user, score))

        recommendations.sort(key=lambda x: x[1], reverse=True)

        print(f"\nFriend Recommendations for {username}:")

        for user, score in recommendations:

            if score > 0:
                print(f"{user} (Score: {score})")

    # =====================================================
    # DISPLAY NETWORK
    # =====================================================

    def display_network(self):

        print("\n===== SOCIAL NETWORK =====")

        for user in self.network:
            print(user, "->", self.network[user])


# =========================================================
# OBJECT CREATION
# =========================================================

sn = SocialNetwork()


# =========================================================
# ADD USERS
# =========================================================

sn.add_user("Aman", 20, ["Coding", "Music", "Gaming"])
sn.add_user("Riya", 21, ["Music", "Travel"])
sn.add_user("Karan", 22, ["Gaming", "Sports"])
sn.add_user("Priya", 20, ["Coding", "Reading"])
sn.add_user("Rahul", 23, ["Travel", "Sports"])
sn.add_user("Sneha", 19, ["Coding", "Music"])
sn.add_user("Arjun", 21, ["Gaming", "Movies"])
sn.add_user("Neha", 22, ["Reading", "Travel"])


# =========================================================
# UPDATE PROFILES
# =========================================================

sn.update_profile("Aman", interests=["Coding", "AI", "Music"])

sn.update_profile("Riya", age=22)


# =========================================================
# FRIEND CONNECTIONS
# =========================================================

sn.add_friend("Aman", "Riya")
sn.add_friend("Aman", "Karan")
sn.add_friend("Riya", "Priya")
sn.add_friend("Karan", "Rahul")
sn.add_friend("Priya", "Sneha")
sn.add_friend("Sneha", "Neha")
sn.add_friend("Rahul", "Arjun")
sn.add_friend("Arjun", "Neha")
sn.add_friend("Aman", "Sneha")
sn.add_friend("Priya", "Neha")


# =========================================================
# REMOVE FRIENDSHIP
# =========================================================

sn.remove_friend("Rahul", "Arjun")


# =========================================================
# SHOW PROFILES
# =========================================================

sn.show_profile("Aman")
sn.show_profile("Riya")
sn.show_profile("Sneha")


# =========================================================
# SHOW FRIENDS
# =========================================================

sn.show_friends("Aman")


# =========================================================
# DISPLAY COMPLETE NETWORK
# =========================================================

sn.display_network()


# =========================================================
# BFS SHORTEST PATH
# =========================================================

sn.bfs_shortest_path("Aman", "Neha")

sn.bfs_shortest_path("Karan", "Sneha")


# =========================================================
# DFS EXPLORATION
# =========================================================

sn.dfs_explore("Aman", 2)

sn.dfs_explore("Aman", 3)


# =========================================================
# FRIEND RECOMMENDATIONS
# =========================================================

sn.recommend_friends("Aman")

sn.recommend_friends("Karan")


# =========================================================
# COMPLEXITY NOTES
# =========================================================

print("\n===== COMPLEXITY NOTES =====")

print("""
1. Add User
   Complexity: O(1)

2. Add Friend
   Complexity: O(1)

3. BFS Traversal
   Complexity: O(V + E)

4. DFS Traversal
   Complexity: O(V + E)

5. Hash Table Search
   Average Complexity: O(1)

6. Recommendation System
   Complexity: O(n log n) after sorting
""")


# =========================================================
# END OF PROJECT
# =========================================================

print("\n===== PROJECT COMPLETED SUCCESSFULLY =====")