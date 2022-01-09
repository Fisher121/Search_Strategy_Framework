from problems.ClassicGraphSearchProblem import ClassicGraphSearchProblem
from strategies.uninformed.BDS import BDS
from strategies.uninformed.BFS import BFS
from strategies.uninformed.Backtracking import Backtracking
from strategies.uninformed.DFS import DFS
from strategies.uninformed.Random import Random
from strategies.uninformed.UCS import UCS

problem = ClassicGraphSearchProblem()
number = 0
bk = UCS()
print(bk.run(problem))
