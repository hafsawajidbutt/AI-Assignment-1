# def bfs(self):
#         # Initialize the queue with the initial state
#         queue = [(self.getCurrentState(), [])]
#         # Initialize a set to keep track of visited states
#         visited = set()
#         while queue:
#             # Dequeue the next state and move
#             state, moves = queue.pop(0)
#             if state not in visited:
#                 visited.add(state)
#                 # If this is the goal state, return the moves that led to it
#                 if self.isGoalState(state):
#                     return moves
                

    
#     # def bfs(self):
#     #     # Initialize the queue with the initial state
#     #     queue = [(self.getCurrentState(), [])]
#     #     # Initialize a set to keep track of visited states
#     #     visited = set()
#     #     while queue:
#     #         # Dequeue the next state and move
#     #         state, moves = queue.pop(0)
#     #         if state not in visited:
#     #             visited.add(state)
#     #             # If this is the goal state, return the moves that led to it
#     #             if self.isGoalState(state):
#     #                 return moves
#     #             #i wanna display all the moves untill the cube is solved
#     #             for move in self.getMoves():
#     #                self.move(move)
#     #                self.draw()
#     #                pygame.display.update()
#     #                pygame.time.wait(1000)
#     #                state = self.getCurrentState()
#     #                print("Moved")
#     #                self.draw()
#     #                pygame.display.update()
#     #                statesEncountered.append(self.getCurrentState())
#     #                moves.append(move)
#     #             #Generate all possible next states
#     #             for move in self.getMoves():
#     #                 next_state = self.getNextState(state, move)
#     #                 if next_state not in visited:
#     #                     queue.append((next_state, moves + [move]))
#     #                     return None
#     #                 return None
#     #             return None
#     def bfs_solve(self):

#         initial_state = self.getCurrentState()  # Get the initial cube state
#         queue = deque([(initial_state, [])])  # Queue stores (state, path)
#         visited = set()
#         visited.add(initial_state)
    
#         states_expanded = 0  # Track number of states expanded
    
#         possible_moves = ["TC", "TA", "FC", "FA", "BC", "BA", "AC", "AA", "RA", "RC", "LC", "LA"]
    
#         while queue:
#             queue_size = len(queue)  # Track queue size
#             current_state, path = queue.popleft()
#             states_expanded += 1

#         # Load the current state into the cube
#             self.setState(current_state)

#             if self.heuristicScore() == 54:  # Check if the cube is solved
#                 print(f"Solution found! Total states expanded: {states_expanded}")
#                 return path

#             for move in possible_moves:
#                 if hasattr(self, f"move{move}"):
#                     getattr(self, f"move{move}")()  # Apply move
                
#                     new_state = self.getCurrentState()  # Get new state
                
#                     if new_state not in visited:
#                         visited.add(new_state)
#                         queue.append((new_state, path + [move]))

#                         # Visualization update
#                         self.draw()
#                         pygame.display.update()
#                         time.sleep(0.5)  # Add delay for better visualization

#                         print(f"Trying move: {move}")

#                     # Undo the move (backtracking in BFS context)
#                     reverse_move = move[:-1] + ('A' if move[-1] == "C" else "C")
#                     getattr(self, f"move{reverse_move}")()

#             print(f"Queue size: {queue_size}, States expanded: {states_expanded}")

#         print("No solution found.")
#         return None
              