from problems.ClassicGraphSearchProblem import ClassicGraphSearchProblem
from strategies.uninformed.BFS import BFS
from strategies.uninformed.Backtracking import Backtracking
from strategies.uninformed.DFS import DFS
from strategies.uninformed.Random import Random

problem = ClassicGraphSearchProblem()
number = 0
bk = Random()
print(bk.run(problem))
