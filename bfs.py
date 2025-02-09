def bfs(self):
        # Initialize the queue with the initial state
        queue = [(self.getCurrentState(), [])]
        # Initialize a set to keep track of visited states
        visited = set()
        while queue:
            # Dequeue the next state and move
            state, moves = queue.pop(0)
            if state not in visited:
                visited.add(state)
                # If this is the goal state, return the moves that led to it
                if self.isGoalState(state):
                    return moves