import sys
from collections import defaultdict


def BFS(initial_state, isGoal, successors):
    assert initial_state, "Provide a Valid Initial State"
    assert isGoal, "Provide a Valid isGoal function"
    assert successors, "Provide a Valid Successor function"

    Que = [initial_state]
    parents = defaultdict(lambda: None)

    done = False

    while not done:
        state = Que.pop()

        if isGoal(state):
            print("Goal Found! Building Path")
            return build_path(state, parents)

        for child in successors(state):
            if not parents[child]:
                parents[child] = state
                Que.append(child)

        done = len(Que) == 0

def build_path(state, parents):
    path  = [state]

    while parents[state]:
        path.append(parents[state])
        state = parents[state]

    print("Built path! Now returning it")
    return reversed(path)
