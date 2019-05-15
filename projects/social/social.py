import random
import statistics


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    # Time Complexity: O(numUsers ^ 2)
    # Space Complexity: O(numUsers ^ 2)
    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}

        # Add users
        # Time Complexity: O(numUsers)
        # Space Complexity: O(numUsers)
        for i in range(numUsers):
            self.addUser(f"User {i + 1}")

        # Create friendships
        # avgFriendships = totalFriendships / numUsers
        # totalFriendships = avgFriendships * numUsers
        # Time Complexity: O(numUsers ^ 2)
        # Space Complexity: O(numUsers ^ 2)
        possibleFriendships = []
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append((userID, friendID))

        # Time Complexity: O(numUsers ^ 2)
        # Space Complexity: O(1)
        random.shuffle(possibleFriendships)

        # Time Complexity: O(avgFriendships * numUsers // 2)
        # Space Complexity: O(avgFriendships * numUsers // 2)
        for friendship_index in range(avgFriendships * numUsers // 2):
            friendship = possibleFriendships[friendship_index]
            self.addFriendship(friendship[0], friendship[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        for i in self.users:
            marked = []
            queue = [[userID]]

            while queue:
                path = queue.pop(0)
                node = path[-1]
                if node not in marked:
                    if node == userID:
                        visited[userID] = [userID]
                    for neighbour in self.friendships[node]:
                        new_path = list(path)
                        new_path.append(neighbour)
                        queue.append(new_path)
                        if neighbour == i:
                            visited[i] = new_path
                            queue = []

                    marked.append(node)

        length = []
        for i in visited:
            length.append(len(visited[i]))
        print(statistics.mean(length))
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(1000, 5)
    # print('Friendships: ', sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print('Connections: ', connections)
