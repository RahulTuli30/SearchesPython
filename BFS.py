import sys
from collections import defaultdict
import random


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

    def start(self, verbose=False):
        Que = [self.initial_state]
        parents = defaultdict(lambda: None)

        done = False
        i = 0
        while not done:
            state = Que.pop()
            if verbose:
                print("current state is {} and Que is {}".format(state, Que))
            if self.isGoal(state):
                if verbose:
                    print("Goal Found! Building Path")
                return self.build_path(state, parents, verbose)

            for child in self.successors(state):
                if not parents[child] and child != self.initial_state:
                    parents[child] = state
                    Que.append(child)
            i += 1
            done = len(Que) == 0 or i > self.ITERATION_LIMIT

        print("Solution NOT found, or Iteration Limit reached")
        return "FAILURE!"

    def isGoal(self, state):
        return state == self.goal_state

    def build_path(self, state, parents, verbose=False):
        path = [state]
        # print(parents)
        while parents[state]:
            # print(parents[state])
            path.append(parents[state])
            state = parents[state]
        path = [_ for _ in reversed(path)]
        if verbose:
            print("Built path! {} Now returning it".format(path))
        return path

import unittest


class TestBfsForWaterJugs(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def successors(self, state):
        actions = [self.fill3, self.fill5, self.empty3, self.empty5, self.empty3in5, self.empty5in3]

        children = [action(state) for action in actions if action(state)]
        # print("Successors of {} are {}".format(state, children))

        return children

    def fill3(self, state):
        return 3, state[1]

    def fill5(self, state):
        return state[0], 5

    def empty3(self, state):
        return 0, state[1]

    def empty5(self, state):
        return state[0], 5

    def empty3in5(self, state):
        space = 5 - state[1]

        if space >= state[0]:
            return 0, state[1] + state[0]

        return state[0] - space, state[1] + space

    def empty5in3(self, state):
        space = 3 - state[0]

        if space >= state[1]:
            return state[0] + space, 0

        return state[0] + space, state[1] - space

    def test_water_jugs(self):
        initial_state = (0, 0)
        goal_state = (3, 5)
        bfs = BFS(initial_state=initial_state, goal_state=goal_state, successors=self.successors)
        # print(bfs.start())
        self.assertEqual(bfs.start(verbose=True), [(0, 0), (0, 5), (3, 5)])


if __name__ == '__main__':
    unittest.main()
