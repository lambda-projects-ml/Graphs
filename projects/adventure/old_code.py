# def reversePath():
# adds to the path list the the opposite of the last direction that was walked


# def walkBackwards():
# moves the player back one room so that room can be checked

# keep track of prev room and update the direction for prev room and current room
def bft(starting_rooom):
    graph = {}
    # Create an empty Queue
    queue = []
    # path = []
    # Create an empty Visited set
    visited = []
    # Add the starting vertex to the queue
    queue.append(starting_rooom)
    visited.append(starting_rooom)
    # exits = player.currentRoom.getExits()
    print(player.currentRoom.getExits())
    for i in player.currentRoom.getExits():
        graph[starting_rooom].update({i: None})
    print(graph)

    # while no ? are in a room
    # while queue:
    for i in player.currentRoom.getExits():
        player.travel(i)
        graph[starting_rooom].update({i: player.currentRoom.id})
        if i == "n":
            player.travel('s')
        elif i == "s":
            player.travel('n')
        elif i == "e":
            player.travel('w')
        elif i == "w":
            player.travel('e')

    print("Current Graph: ", graph)
    print("Graph Keys for 0: ", graph[0].keys())
    print("Queue :", queue)

    # While the queue is not empty...
    # while len(queue) > 0:
    #     # Dequeue the first vertex
    #     v = q.dequeue()
    #     # If it has not been visited...
    #     if v not in visited:
    #         # Mark it as visited (print it and add it to the visited set)
    #         print(v)
    #         visited.add(v)
    #         # Then enqueue each of its neighbors in the queue
    #         for neighbor in self.vertices[v]:
    #             q.enqueue(neighbor)


bft(player.currentRoom.id)
# TRAVERSAL TEST
# visited_rooms = set()
# player.currentRoom = world.startingRoom
# visited_rooms.add(player.currentRoom)

# for move in traversalPath:
#     player.travel(move)
#     visited_rooms.add(player.currentRoom)

# if len(visited_rooms) == len(roomGraph):
#     print(
#         f"TESTS PASSED: {len(traversalPath)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(roomGraph) - len(visited_rooms)} unvisited rooms")


===============================================
# def bft(starting_room, queue={}, path=[], visited={}):
#     queue = queue
#     path = path
#     visited = visited

#     # Add the starting vertex to the queue
#     exits = player.currentRoom.getExits()
#     queue[starting_room] = exits
#     # gets the first room listed in the queue
#     first_item = list(queue.keys())[0]
#     # gets the length of the list for the room/index
#     print("Length of values in room: ", len(queue[0]))
#     # gets list of all items in the room queue
#     print(queue[first_item])
#     return queue
#     while len(q) > 0:
#         # Dequeue the first vertex
#         v = list(queue.keys())[0]
#         # If it has not been visited...
#         if v not in visited:
#             # Mark it as visited and add list of exits to the dictionary
#             exits = player.currentRoom.getExits()
#             visited[v] = exits
#             # Then enqueue each of its neighbors in the queue
#             for neighbor in self.vertices[v]:
#                 q.enqueue(neighbor)


# starting_room = player.currentRoom.id
# bft(starting_room)
# # print(player.currentRoom.getRoomInDirection('n'))
# # # Room 1

# # #    (3,6)

# # # Exits: [n, s]

# # exits = player.currentRoom.getExits()
# # print(exits) # produces a list
