# Searches

Clean implementation of Breadth-First Search Algorithm.
Test usage is shown using [unitest](https://docs.python.org/3/library/unittest.html)

To perform BFS, all we need is an initial state, a goal state, and some actions that modify the state, these actions when applied to each state, it's successors, aka children. As we proceed, we keep appending the successors in a Que for processing them later. If we ever reach the goal state, we found a solution! Hurray. Else the algorithm keeps generating the next generation of children until no *new* states are produced.  We keep track of visited states using a visited or parents dictionary, and this dictionary also helps us build the path that led to this goal state later!

## Time and Complexity

Because we do not know the total number of nodes before-hand, the terminology needs to change,

Let's assume that we reach the goal at depth *d*
At each state, the possible number of children will be at most the number of actions applied, aka the *branching factor* let's call this number *b*

Thus the total number of nodes we visited is *O(b^(d))*

Thus the Time Complexity will be *O(b^(d))*,

Because we also keep track of each visited state in the *parents* dictionary, the Asymptotic space complexity is also *O(b^(d))*


## Example Usage

```python
from BFS import *

class TestBfsForWaterJugs(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def successors(self, state):
        actions = [self.fill3, self.fill5, self.empty3, self.empty5, self.empty3in5, self.empty5in3]
        children = [action(state) for action in actions if action(state)]
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

```

The BFS class itself is only about 60 lines of code with support for verbose message printing.
Feel free to use this as is, or as a base for your own implementation!

```python
class BFS:
    __slots__ = "initial_state", "goal_state", "successors", "ITERATION_LIMIT"

    def __init__(self, initial_state, goal_state, successors, iter_limit=1000):
        self.check_validity(initial_state, goal_state, successors, iter_limit)
        self.initial_state, self.goal_state, self.successors = initial_state, goal_state, successors
        self.ITERATION_LIMIT = iter_limit

    def setIterationLimit(self, newLimit):
        assert type(newLimit) == int, "INVALID ITERATION LIMIT"
        self.ITERATION_LIMIT = newLimit

    def start(self, verbose=False):
        Que = [self.initial_state]
        parents = defaultdict(lambda: None)
        done = False
        iterationNumber = 0

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

            iterationNumber += 1
            done = len(Que) == 0 or iterationNumber > self.ITERATION_LIMIT

        print("Solution NOT found, or Iteration Limit reached")
        return "FAILURE!"

    def isGoal(self, state):
        return state == self.goal_state

    def build_path(self, state, parents, verbose=False):
        path = [state]
        while parents[state]:
            path.append(parents[state])
            state = parents[state]

        path = [_ for _ in reversed(path)]

        if verbose:
            print("Built path! {} Now returning it".format(path))

        return path

    @staticmethod
    def check_validity(initial_state, goal_state, successors, iter_limit):
        assert initial_state, "Provide Initial State"
        assert goal_state, "Provide Valid Goal State"
        assert successors, "Provide a Valid Successor function"
        assert callable(successors), "Successors has to be a callable function"
        assert type(iter_limit) == int, "INVALID ITERATION LIMIT"

```


## License
[MIT](https://choosealicense.com/licenses/mit/)
