import sys
from collections import defaultdict


class BFS:
    __slots__ = "initial_state", "goal_state", "successors", "ITERATION_LIMIT"

    def __init__(self, initial_state, goal_state, successors, iter_limit=1000):
        self.check_validity(initial_state, goal_state, successors, iter_limit)
        self.initial_state, self.goal_state, self.successors = initial_state, goal_state, successors
        self.ITERATION_LIMIT = iter_limit

    @staticmethod
    def check_validity(initial_state, goal_state, successors, iter_limit):
        assert initial_state, "Provide Initial State"
        assert goal_state, "Provide Valid Goal State"
        assert successors, "Provide a Valid Successor function"
        assert callable(successors), "Successors has to be a callable function"
        assert type(iter_limit) == int, "INVALID ITERATION LIMIT"

    def setIterationLimit(self, newLimit):
        assert type(newLimit) == int, "INVALID ITERATION LIMIT"
        self.ITERATION_LIMIT = newLimit

    def start(self):
        Que = [self.initial_state]
        parents = defaultdict(lambda: None)

        done = False
        i = 0
        while not done:
            state = Que.pop()

            if self.isGoal(state):
                print("Goal Found! Building Path")
                return self.build_path(state, parents)

            for child in self.successors(state):
                if not parents[child]:
                    parents[child] = state
                    Que.append(child)
            i += 1
            done = len(Que) == 0 or i > self.ITERATION_LIMIT

        print("Solution NOT found, or Iteration Limit reached")

    def isGoal(self, state):
        return state == self.goal_state

    def build_path(self, state, parents):
        path = [state]

        while parents[state]:
            path.append(parents[state])
            state = parents[state]

        print("Built path! Now returning it")
        return reversed(path)
