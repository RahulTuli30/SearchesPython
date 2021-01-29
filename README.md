# SearchesPython
A clean implementation of generic Breadth First Search with test usage shown using [unitest](https://docs.python.org/3/library/unittest.html)

To perform BFS all we need is an initial state, a goal state, and some set of actions that modify the state, these actions when applied to each state give us it's successors aka children. As we proceed we keep appending the successors in a Que for processing them later, If we ever reach the goal state, we are done, else the we keep generating next generation of children unless no new states are produced, which we keep track of using a visited or parents dictionary, this dictionary also helps us build the path that led to this goal state later!

## Time and Complexity

Because we never do not know the total number of nodes before-hand the terminology needs to change,

Let's assume we that we reach the goal at depth *d*
At each state the possible number of children will be at-most the number of actions applied, aka the *branching factor* let's call this number *b*

Thus the total number of nodes we visited is *O(b^(d))*

Thus the Time Complexity will be *O(b^(d))*,

Because we also keep track of each visited state in the parents dictionary,
the Asymptotic space complexity is also *O(b^(d))*


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
