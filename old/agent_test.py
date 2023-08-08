# fringe - struktura danych przechowująca wierzchołki do odwiedzenia
# explored - lista odwiedzonych stanów
# istate - stan początkowy2
# succ - funkcja następnika
# goaltest - test spełnienia celu
from collections import deque

matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [1, 1, 0, 0, 0, 1, 1, 0, 0],
          [0, 0, 1, 1, 0, 0, 1, 0, 0],
          [0, 0, 0, 1, 1, 1, 0, 0, 0],
          [0, 0, 0, 1, 0, 0, 0, 0, 0],
          [0, 1, 1, 0, 0, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]

def get_moves(node, moves):
    print(node.action)
    if node.action is None:
        return moves
    else:
        moves.append(node.action)
        get_moves(node.parent, moves)

def succ(state, direction):
    #print("------ITERATION------")
    states_L = {"L": "D",
              "R": "U",
              "U": "L",
              "D": "R"}
    states_R = {"L": "U",
              "R": "D",
              "U": "R",
              "D": "L"}

    states_move = {"L": [state[0] - 1, state[1]],
              "R": [state[0] + 1, state[1]],
              "U": [state[0], state[1] - 1],
              "D": [state[0], state[1] + 1]}
    childs = []
    for ruch in ["R", "L", "M"]:
        node1 = node(None, None)
        if ruch == "L":
            node1.action = "L"
            node1.state = state
            node1.direction = states_L.get(direction)
            childs.append([ruch, node1])
        if ruch == "R":
            node1.action = "R"
            node1.state = state
            node1.direction = states_R.get(direction)
            childs.append([ruch, node1])
        if ruch == "M":
            st = states_move.get(direction)
            if (st[0] not in [-1, 9]) and (st[1] not in [-1, 9]) and (matrix[st[0]][st[1]] != 1):
                    node1.action = "M"
                    node1.state = st
                    node1.direction = direction
                    childs.append([ruch, node1])

    return childs


def goaltest(state):
    return state == [2, 8]

def graphsearch(fringe, explored, istate, succ, goaltest, direction):
    fringe.append(node(istate, direction))

    while True:
        #print(fringe.count())
        if not fringe:
            return False

        elem = fringe.popleft()

        if goaltest(elem.state):
            #print(get_moves(elem, []))
            return elem

        explored.append(elem)

        for (action, state) in succ(elem.state, elem.direction):
            if state not in fringe and state not in explored:
                #print(f"action: {action}, state: {state.state}, direction: {state.direction}")
                x = node(state.state, state.direction)
                x.parent = elem
                x.action = action
                fringe.append(x)

class node:
    def __init__(self, state, direction):
        self.state = state
        self.parent = None
        self.action = None
        self.direction = direction

fringe = deque()


graphsearch(fringe, [], [0, 0], succ, goaltest, "R")