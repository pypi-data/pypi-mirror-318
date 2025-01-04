p1='''
goalState = {'A': '0', 'B': '0'}
cost = 0
roomStates = {'A': '0', 'B': '0'}

# Initial input
location = input("Enter the starting location of vacuum (A/B) = ")

for room in roomStates:
    action = input("Enter the state of " + room + " (0 for clean /1 for dirty): ")
    roomStates[room] = action

# General Outputs
print("\nCurrent State: " + str(roomStates))
print("Goal state: " + str(goalState))
print("Vacuum is placed in location " + location)

if roomStates != goalState:
    if location == 'A':
        if roomStates['A'] == '1':  # if dirty
            roomStates['A'] = '0'
            cost += 1
            print("Location A was dirty. Location A has been cleaned. Cost for cleaning is 1.")
        
        if roomStates['B'] == '1':  # if B is dirty
            print("\nMoving A -> B. Cost for moving within rooms is 1.")
            cost += 1
            roomStates['B'] = '0'
            cost += 1
            print("Location B was dirty. Location B has been cleaned. Cost for cleaning is 1.")
            
    elif location == 'B':
        if roomStates['B'] == '1':  # if dirty
            roomStates['B'] = '0'
            cost += 1
            print("Location B was dirty. Location B has been cleaned. Cost for cleaning is 1.")
        
        if roomStates['A'] == '1':  # if A is dirty
            print("\nMoving B -> A. Cost for moving within rooms is 1.")
            cost += 1
            roomStates['A'] = '0'
            cost += 1
            print("Location A was dirty. Location A has been cleaned. Cost for cleaning is 1.")
            
    print("Goal state has been met.")
    print("Performance Measurement: " + str(cost))
    
else:
    print("\nAll rooms are already clean.")
    print("Performance Measurement: " + str(cost))

'''

p2='''
from collections import defaultdict

def input_graph():
    n = int(input("Enter Number of Nodes: "))
    e = int(input("Enter Number of Edges: "))

    graph = defaultdict(list)

    for _ in range(e):
        u, v = map(int, input("Enter Edge (u v): ").split())
        graph[u].append(v)
    
    return graph

def dfs(v, goal, limit, graph):
    if v == goal:
        return True

    if limit <= 0:
        return False

    for i in graph[v]:
        if dfs(i, goal, limit - 1, graph):
            return True

    return False

def main():
    graph = input_graph()
    goal = int(input("Enter Goal Node: "))
    limit = int(input("Enter Depth Limit: "))

    if dfs(0, goal, limit, graph):
        print("Goal found within depth limit")
    else:
        print("Goal not found within depth limit")

if __name__ == "__main__":
    main()

'''

p3='''
from collections import deque

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()

def move_blank(board, direction):
    new_board = [row.copy() for row in board]
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:  # Find the blank tile
                if direction == 'up' and i > 0:
                    new_board[i][j], new_board[i - 1][j] = new_board[i - 1][j], new_board[i][j]
                    return new_board
                elif direction == 'down' and i < 2:
                    new_board[i][j], new_board[i + 1][j] = new_board[i + 1][j], new_board[i][j]
                    return new_board
                elif direction == 'left' and j > 0:
                    new_board[i][j], new_board[i][j - 1] = new_board[i][j - 1], new_board[i][j]
                    return new_board
                elif direction == 'right' and j < 2:
                    new_board[i][j], new_board[i][j + 1] = new_board[i][j + 1], new_board[i][j]
                    return new_board
    return None

def is_goal(board):
    return board == [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

def bfs(initial_board):
    visited = set()
    queue = deque([(initial_board, [])])

    while queue:
        current_board, path = queue.popleft()
        if is_goal(current_board):
            return path
        visited.add(tuple(map(tuple, current_board)))

        for direction in ['up', 'down', 'left', 'right']:
            new_board = move_blank(current_board, direction)
            if new_board and tuple(map(tuple, new_board)) not in visited:
                new_path = path + [direction]
                queue.append((new_board, new_path))

    return None

if __name__ == "__main__":
    initial_state = [[1, 2, 0], [4, 5, 3], [7, 8, 6]]  # Example initial state
    print("Initial State:")
    print_board(initial_state)

    solution_path = bfs(initial_state)

    if solution_path:
        print("Solution Path:")
        for step, direction in enumerate(solution_path, 1):
            print(f"Step {step}: Move {direction}")
    else:
        print("No solution found.")

'''

p4='''
from collections import defaultdict

def aStarAlgo(start_node, stop_node):     
    open_set = set([start_node]) 
    closed_set = set()
    g = {}  # store distance from starting node
    parents = {}  # parents contains an adjacency map of all nodes

    # Distance of starting node from itself is zero
    g[start_node] = 0
    # Start_node is root node i.e it has no parent nodes
    # So start_node is set to its own parent node
    parents[start_node] = start_node
             
    while len(open_set) > 0:
        n = None

        # Node with the lowest f() is found
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
             
        if n is None:
            print('Path does not exist!')
            return None
             
        if n == stop_node:
            # Reconstruct the path from stop_node to start_node
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Path found: {}'.format(path))
            return path

        for (m, weight) in get_neighbors(n):
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n

                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)

        open_set.remove(n)
        closed_set.add(n)
 
    print('Path does not exist!')
    return None
         
#define function to return neighbor and its distance from the passed node
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return []

# Heuristic function returns heuristic distance for all nodes
def heuristic(n):
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0
    }
    return H_dist[n]

# Describe your graph here  
Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': [],
    'E': [('D', 6)],
    'D': [('G', 1)]
}

# Execute the algorithm
aStarAlgo('A', 'G')

'''

p6='''
def And(a, b):
    return a and b

def Or(a, b):
    return a or b

def Not(a):
    return not a

def Implies(a, b):
    return not a or b

def evaluate(expression, assignment):
    values = dict(assignment)
    p = values.get('p', False)
    q = values.get('q', False)
    r = values.get('r', False)
    return expression(p, q, r)

def kb(p, q, r):
    return And(Implies(p, q), Implies(q, r))

def query(p, q, r):
    return Implies(p, r)

def generate_truth_assignments():
    return [
        [('p', True), ('q', True), ('r', True)],
        [('p', True), ('q', True), ('r', False)],
        [('p', True), ('q', False), ('r', True)],
        [('p', True), ('q', False), ('r', False)],
        [('p', False), ('q', True), ('r', True)],
        [('p', False), ('q', True), ('r', False)],
        [('p', False), ('q', False), ('r', True)],
        [('p', False), ('q', False), ('r', False)]
    ]

def check_entailment(kb, query):
    truth_assignments = generate_truth_assignments()
    for assignment in truth_assignments:
        kb_result = evaluate(kb, assignment)
        query_result = evaluate(query, assignment)
        if kb_result and not query_result:
            return False
    return True

if check_entailment(kb, query):
    print("The knowledge base entails the query.")
else:
    print("The knowledge base does not entail the query.")

'''
p8='''
from sympy import symbols, Or, And, Not, Implies, to_cnf

def convert_to_cnf(statement):
    # Define symbols
    p, q, r = symbols('p q r')

    # Convert the statement to CNF
    cnf_statement = to_cnf(statement)

    return cnf_statement

# Example usage
if __name__ == "__main__":
    # Define symbols
    p, q, r = symbols('p q r')

    # Define the logical statement
    statement = And(Implies(p, q), Implies(q, p))

    cnf = convert_to_cnf(statement)
    print("Original statement:", statement)
    print("CNF:", cnf)

'''

p9='''
def is_variable(term):
    return isinstance(term, str) and term.islower()

def substitute(theta, term):
    if term in theta:
        return theta[term]
    return term

def unify(term1, term2, theta):
    if term1 == term2:
        return theta
    if is_variable(term1):
        if term1 in theta:
            return unify(substitute(theta, term1), term2, theta)
        theta[term1] = term2
        return theta
    if is_variable(term2):
        return unify(term2, term1, theta)
    if isinstance(term1, tuple) and isinstance(term2, tuple) and len(term1) == len(term2):
        for t1, t2 in zip(term1, term2):
            theta = unify(t1, t2, theta)
            if theta is None:
                return None
        return theta
    return None

term1 = ('father', 'john', 'jane')
term2 = ('father', 'x', 'y')
theta = {}
result = unify(term1, term2, theta)

if result is not None:
    print(f"Unification succeeded: {result}")
else:
    print("Unification failed")

'''